# This script will merge all the universities' topic frequency department
# by department
# Output Files:
#   processed_data/Analyzed_data_department_only.db //Databased containing department wise topic frequency
#   processed_data/[department].xlsx //Same data but provided in Excel sheet
import os
import sqlite3
import numpy as np
import pandas as pd

with sqlite3.connect(os.path.join('processed_data','Analyzed_data.db')) as con:
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
with sqlite3.connect(os.path.join('processed_data','Analyzed_data_department_only.db')) as con:
    cursor = con.cursor()
    for key in df_dict.keys():
        df_dict[key] = df_dict[key].groupby('index').sum()
        df_dict[key].to_sql(key, con, if_exists='replace')
        df_dict[key].to_excel(os.path.join('processed_data',key+'.xlsx'),sheet_name='result')
