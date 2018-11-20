import os
import sqlite3
import numpy as np
import pandas as pd

data = sqlite3.connect(os.path.join('processed_data', 'database.db'))
cursor = data.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablename = cursor.fetchall()
# Split tablename using _
tablename = list(map(lambda i: i[0].split('_'), tablename))
bigram_tablename = []
for name in tablename:
    if name[3] == 'bigram':
        bigram_tablename.append(name)
ece_toplist = {}
# ECE
for name in bigram_tablename:
    if name[1] == 'ece' and name[0] == 'ucsd':
        cursor.execute("SELECT * from "+str('_'.join(name)) + " order by freq DESC LIMIT 30;")
        dictname = name[2][0]+name[2][1]
        ece_toplist[dictname] = cursor.fetchall()
yearlist = list(ece_toplist.keys())
yearlist.sort()
sorted_ecelist = {}
for year in yearlist:
    sorted_ecelist[year] = ece_toplist[year]
ref_bigramlist = []
for value in sorted_ecelist.values():
    for name in value:
        if not name[0] in ref_bigramlist:
            ref_bigramlist.append(name[0])
frequency_table = np.zeros((len(ref_bigramlist), len(sorted_ecelist.keys())))
for key in list(sorted_ecelist.keys()):
    for value in sorted_ecelist[key]:
        frequency_table[ref_bigramlist.index(value[0]), int(key)-int(list(sorted_ecelist.keys())[0])] = value[1]
column_name = list(sorted_ecelist.keys())
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
frequency_dataframe = pd.DataFrame(frequency_table, index = ref_bigramlist, columns = column_name)
frequency_dataframe.to_excel('output.xls',sheet_name='ucsd')