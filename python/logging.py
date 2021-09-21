# this script is responsible for regular logging. Utilizes its own append_file
import os
import datetime
from constant import INFO, ERROR, CRITICAL

app = os.path.basename(__file__)

def info(app, message):
    """Stored in LOGGING/INFO.LOG"""
    append_file(INFO, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

def error(app, message):
    """Stored in LOGGING/ERROR.LOG"""
    append_file(ERROR, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

def critical(app, message):
    """Stored in LOGGING/CRITICAL.LOG"""
    append_file(CRITICAL, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

# logging.py is the only script to get its own append_file to avoid circular imports. All other files must use filing
def append_file(filepath, message):
    """appends a file for logging purposes only. DO NOT USE"""
    try:
        with open(filepath, 'a') as file:
            file.write(message + '\n')
    except:
        print('error creating ' + filepath)