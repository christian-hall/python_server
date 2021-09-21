# this script is used exclusively for writing and manipulation of files.
import os
from shutil import copyfile
import logging
from constant import *
from schedule import weekly

app = os.path.basename(__file__)

def write_file(filepath, message):
    """writes to a file, will overwrite any other work on the file"""
    try:
        with open(filepath, 'w') as file:
            file.write(message)
    except:
        logging.info(app, 'error creating ' + filepath)

def append_file(filepath, message):
    """appends an individual line in a file, does account for carriage returns"""
    try:
        with open(filepath, 'a') as file:
            file.write(message + '\n')
    except:
        logging.info(app, 'error creating ' + filepath)

def delete_file(filepath):
    if os.path.isfile(filepath):
        try_attempt = 0
        while try_attempt < 3:
            try_attempt += 1
            try:
                os.remove(filepath)
                break
            except:
                if try_attempt < 3:
                    logging.error(app, f'delete attempt {try_attempt}: failed to erase {filepath}')
                else:
                    logging.critical(app, f'completely failed to erase {filepath}')
    else:
        logging.info(app, f'{filepath} did not exist')

def copy_file(filepath, copy):
    if os.path.isfile(filepath):
        delete_file(copy)
        try_attempt = 0
        while try_attempt < 3:
            try_attempt += 1
            try:
                copyfile(filepath, copy)
                break
            except:
                if try_attempt < 3:
                    logging.error(app, f'copy attempt {try_attempt}: failed to copy {filepath} to {copy}')
                else:
                    logging.critical(app, f'completely failed to copy {filepath} to {copy}')

def clean_logs():
    if weekly(hour=4):
        logging.info(app, 'backing up and deleting info.log')
        copy_file(INFO, OLDINFO)
        delete_file(INFO)

        logging.info(app, 'backing up and deleting error.log')
        copy_file(ERROR, OLDERROR)
        delete_file(ERROR)

