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
import os



raw_data_folder_name = os.path.join(os.path.dirname(os.getcwd()),'raw_data')

db = SQLite('database.db')  # To do Renjie, make this parent Database in root, rather than scripts


def get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    '''
    Generator that returns rawdata file
    '''    
    import os    
    for i in os.listdir(raw_data_folder_name):
        if i.endswith('.txt'):
            yield i

for i in get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    
	print("Currently working on :",i) #To check status, remove later
	dict_single, dict_bigram = word_freq.word_freq(os.path.join(raw_data_folder_name,i))

	table_name = i.split('.txt')[0]
	table_name_single = table_name + '_sinlge'
	table_name_bigram = table_name + '_bigram'

	err = db.create_table(table_name_single)
	err = db.insert_dict(table_name_single, dict_single)

	err = db.create_table(table_name_bigram)
	err = db.insert_dict(table_name_bigram, dict_bigram)


