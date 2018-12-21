#
# main entry point of our program
#
# Nov 20, 2018 by Renjie Zhu
# 

from scripts.process_data import process_data
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

assert not os.path.exists(os.path.join('processed_data','school.db')), 'School data has already been processed.'
process_data('school')
assert not os.path.exists(os.path.join('processed_data','industry.db')), 'Industry data has already been processed.'
process_data('industry')

import analyze_data
import analyze_data_by_department
import merge_industry

logger.info('Program ends.')
