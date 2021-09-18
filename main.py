
from os import error
from constant import *
from comm import logging, connectivity
from maintnce import clean_logs, error_alerts

def __main__():
    app = 'HALLPY'
    logging.run()
    # offline scripts happen here
    clean_logs()

    if connectivity.online():
        logging.info(app, 'program is online')

        # online scripts happen here
        error_alerts() # this goes last
    else:
        logging.warning(app, 'program is not online at this time')

__main__()