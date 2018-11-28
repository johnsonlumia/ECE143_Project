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

from scripts.SQLite import SQLite
from scripts.word_freq import word_freq
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_raw_data_filenames_in_txt_format(raw_data_folder_name):
    '''
    **Generator** that returns rawdata filename one at a time.

    argument
    --------

    raw_data_folder_name: a string containing the directory to our raw data
        type: string

    yield
    -----

    a file name in our raw data folder that can be passed to further manipulation
        type: string
    '''
    assert isinstance(raw_data_folder_name, str)
    for i in os.listdir(raw_data_folder_name):
        if i.endswith('.txt'):
            yield i



def process_data(dataset='school'):
    """
    process data of corresponding dataset.
    """

    assert isinstance(dataset, str)
    assert dataset == 'school' or dataset == 'industry'

    if dataset == 'school':
        # get the directory where all the raw files live
        folder_name = os.path.join('raw_data')

        # create a connection to a database where all our processed data live
        # for details please see `SQLite.py`
        # db = SQLite(os.path.join('processed_data','database.db'))
        db = SQLite(os.path.join('processed_data','school.db'))
    else:
        folder_name = os.path.join('industry_data')
        db = SQLite(os.path.join('processed_data','industry.db'))


    # calling the above generator, we work with the every raw data file in the folder
    for i in get_raw_data_filenames_in_txt_format(folder_name):

        # calling the word_freq function in another file.
        # this function gives back two dictionaries including
        # (1) single words and their frequencies
        # (2) bigram phrases and their frequencies
        # for more detail please see `word_freq.py`
        logger.info(f'Currently working on: {i}')
        # print("[process data] Currently working on :", i)
        dict_single, dict_bigram = word_freq(
            os.path.join(folder_name, i))

        # passing the two dictionaries into our database
        table_name = i.split('.txt')[0]
        table_name_single = table_name + '_single'
        table_name_bigram = table_name + '_bigram'

        # creating corresponding table and insert the dictionary into the table
        # err is an error code for debugging purposes, for details, please see
        # `SQLite.py`
        db.create_table(table_name_single)
        db.insert_dict(table_name_single, dict_single)

        db.create_table(table_name_bigram)
        db.insert_dict(table_name_bigram, dict_bigram)
