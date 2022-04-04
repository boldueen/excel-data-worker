import logging
import time

from utils import make_report



def start():

    file = ''
    logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%I:%M:%S')
    logging.info("program has been started successfully")
    logging.info(make_report(file))



start()
