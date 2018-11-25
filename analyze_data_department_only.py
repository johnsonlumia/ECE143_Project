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
import os
import sqlite3
import numpy as np
import pandas as pd

with sqlite3.connect('Analyzed_data.db') as con:
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablename = cursor.fetchall()
    tablename = list(map(lambda i: i[0].split('_'), tablename))
    df_dict = {}
    for name in tablename:
        if name[1] == 'cs':
            savename = 'cse'
        elif name[1] == 'mae':
            savename = 'me'
        elif name[1] == 'ee':
            savename = 'ece'
        else:
            savename = name[1]
        df = pd.read_sql_query("SELECT * FROM "+str('_'.join(name)), con=con)
        if savename in df_dict.keys():
            df_dict[savename] = pd.concat([df,df_dict[savename]],sort=False)
        else:
            df_dict[savename] = df
with sqlite3.connect('Analyzed_data_department_only.db') as con:
    cursor = con.cursor()
    for key in df_dict.keys():
        df_dict[key] = df_dict[key].groupby('index').sum()
        df_dict[key].to_sql(key, con)
        df_dict[key].to_excel(key+'.xlsx',sheet_name='result')
