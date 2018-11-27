#
# main entry point of our program
#
# Nov 20, 2018 by Renjie Zhu
# 

from scripts.process_data import process_data
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

process_data('school')
process_data('industry')

import analyze_data
import analyze_data_department_only

# Visualization
logger.info('Visualization starts')
import Extent_of_overlap
import ucsd_ece_plot
import ucsd_cse_plot

logger.info('Program ends.')
