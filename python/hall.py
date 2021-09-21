import os
import datetime
from constant import ACTIVE
from filing import write_file, delete_file, clean_logs
from internet import online
import logging

app = os.path.basename(__file__)

app = 'HALLPY'

write_file(ACTIVE, datetime.datetime.now())
logging.info(app, 'hall.py is active')
clean_logs()

if online():
    pass
    # online scripts happen here
    # alert messages happen here, last

delete_file(ACTIVE)
logging.info(app, 'hall.py is inactive')


# create a def that will check all files and directories and make them if needed, including ini files
# for email, online, etc