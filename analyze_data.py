# This scrpt is used for generaring a more compavt bigram result from the data processed.
# It will automatically convert the database into a new database with schools and their
# department as seperate tables. Datas in tables show how each bigram changes through
# years
# Table example:
#           yr yr yr yr yr yr yr
#   bigram1 1  3  3  3  5  9  3
#   bigram2 2  2  1  1  0  1  2
#   bigram3 5  7  8  9  11 11 11
#   ...
# Script will only run if the Analyzed_data.db is not exsist
# Output Files:
#   processed_data/Analyzed_data.db //Databased containing reorganized topic frequency
#   processed_data/[university]_[department].xlsx //Same data but provided in Excel sheet
import os
import sqlite3
import numpy as np
import pandas as pd

with sqlite3.connect('school.db') as con0:
    cursor = con0.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablename = cursor.fetchall()
    # Split tablename using _
    tablename = list(map(lambda i: i[0].split('_'), tablename))
    global bigram_tablename
    bigram_tablename = []
    for name in tablename:
        if name[3] == 'bigram':
            bigram_tablename.append(name)


    def reorganize_data(school, department, cursor):
        """reorganize data and store it into a new database
        Args:
            school/department: extract from database derived before
            cursor: SQL cursor
        """
        assert isinstance(school, str)
        assert isinstance(department, str)
        toplist = {}
        for name in bigram_tablename:
            if name[1] == department and name[0] == school:
                cursor.execute("SELECT * from "+str('_'.join(name)
                                                    ) + " order by freq DESC LIMIT 60;")
                dictname = name[2][0]+name[2][1]
                toplist[dictname] = cursor.fetchall()
        yearlist = list(toplist.keys())
        yearlist.sort()
        sorted_ecelist = {}
        for year in yearlist:
            sorted_ecelist[year] = toplist[year]
        row_bigram = []
        for value in sorted_ecelist.values():
            for name in value:
                if not name[0] in row_bigram:
                    row_bigram.append(name[0])
        matrix_bigram = np.zeros((len(row_bigram), len(sorted_ecelist.keys())))
        for key in list(sorted_ecelist.keys()):
            for value in sorted_ecelist[key]:
                matrix_bigram[row_bigram.index(value[0]), int(
                    key)-int(list(sorted_ecelist.keys())[0])] = value[1]
        column_year = list(sorted_ecelist.keys())
        frequency_dataframe = pd.DataFrame(
            matrix_bigram, index=row_bigram, columns=column_year)
        frequency_dataframe.to_excel(os.path.join('processed_data',school+'_'+department+'.xlsx'),sheet_name='result')
        return frequency_dataframe
    with sqlite3.connect(os.path.join('processed_data','Analyzed_data.db')) as con1:
        save_cursor = con1.cursor()
        previous_set = []
        for element in bigram_tablename:
            if [element[0], element[1]] in previous_set:
                continue
            else:
                analyzed = reorganize_data(element[0], element[1], cursor)
                analyzed.to_sql(element[0]+"_"+element[1], con1,if_exists='replace')
                previous_set.append([element[0], element[1]])
