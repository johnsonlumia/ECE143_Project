# This script merge all the job description data together
# The data is produced for our analysis to find the hot topic
# Output:
#   processed_data/industry_merged.db // Merged industry database
#   processed_data/Bigram_industry.xlsx // Merged bigram topics
#   processed_data/Single_industry.xlsx // Merged single words
import os
import sqlite3
import pandas as pd
import os

with sqlite3.connect(os.path.join('processed_data','industry.db')) as con:
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablename = cursor.fetchall()
    tablename = list(map(lambda i: i[0].split('_'), tablename))
    df_single = pd.DataFrame([])
    df_bigram = pd.DataFrame([])
    for name in tablename:
        if name[2] == 'single':
            df = pd.read_sql_query(
                "SELECT * FROM "+str('_'.join(name)), con=con)
            df_single = pd.concat([df_single, df], sort=False)
        if name[2] == 'bigram':
            df = pd.read_sql_query(
                "SELECT * FROM "+str('_'.join(name)), con=con)
            df_bigram = pd.concat([df_bigram, df], sort=False)
with sqlite3.connect(os.path.join('processed_data', 'industry_merged.db')) as con:
    cursor = con.cursor()
    df_single = df_single.groupby('word').sum()
    df_bigram = df_bigram.groupby('word').sum()
    df_single.to_sql('Single', con, if_exists='replace')
    df_bigram.to_sql('Bigram', con, if_exists='replace')
    df_bigram.to_excel(os.path.join('processed_data','Bigram_industry.xlsx'), sheet_name='result')
    df_single.to_excel(os.path.join('processed_data','Single_industry.xlsx'), sheet_name='result')
