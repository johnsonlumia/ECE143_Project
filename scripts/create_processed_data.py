#
# ECE 143 Group Project
#
# automatically process all raw data files
#
# by Ambareesh S J on Oct 24, 2018
#
# modified: 
#   Renjie: push to database
#

from SQLite import SQLite
import word_freq

raw_data_folder_name = input('Enter raw data folder path')

# raw_data_folder_name = r'C:\Users\asree\Documents\GitHub\ECE143_Project\ECE143_Project\asj\raw_data'

db = SQLite('database.db')

for i in get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    
    dict_single, dict_bigram = word_freq.word_freq(i)

    table_name = i.split('.txt')[0]
    table_name_single = table_name + '_sinlge'
    table_name_bigram = table_name + '_bigram'
    
    err = db.create_table(table_name_single)
    err = db.insert_dict(table_name_single, dict_single)

    err = db.create_table(table_name_bigram)
    err = db.insert_dict(table_name_bigram, dict_bigram)
    


def get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    '''
    Generator that returns rawdata file
    '''    
    import os    
    for i in os.listdir(raw_data_folder_name):
        if i.endswith('.txt'):
            yield i