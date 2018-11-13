raw_data_folder_name = input('Enter raw data folder path')

#raw_data_folder_name = r'C:\Users\asree\Documents\GitHub\ECE143_Project\ECE143_Project\asj\raw_data'

for i in get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    
    dict_single, dict_bigram = word_freq(i)
    
    ## TO DO : Renjie
    #Add dict_single,dict_bigram to the Database.db in root


def get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    '''
    Generator that returns rawdata file
    '''    
    import os    
    for i in os.listdir(raw_data_folder_name):
        if i.endswith('.txt'):
            yield i