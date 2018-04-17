#!/usr/bin/python

import logging

#logging.basicConfig(format='%(asctime)s  %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
#logging.basicConfig(level=logging.INFO, filename='example.log', filemode='w')
logging.basicConfig(level=logging.INFO)

logging.debug('This is a debug')
logging.info('This is a info')
logging.warning('This is a warning')
