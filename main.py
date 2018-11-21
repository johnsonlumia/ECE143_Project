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

# process_data('school')
process_data('industry')

logger.info('Program ends.')