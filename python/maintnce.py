from regulatr import file_regulator, frequency
from constant import *
from comm import logging, email, connectivity

app = 'MAINTENANCE'

def clean_logs():
    # look at all .log files in app_folder, backup and delete if over 500,000 bytes in app_folder
    if frequency.daily(0, 0):
        logging.info(app, 'Cleaning log files')
        for file in os.scandir(app_folder):
            if file.path.endswith('.log'):
                file_regulator.size(os.path.join(app, file), 2000000)

def error_alerts():
    if frequency.quarter_hour():
        if os.path.isfile(critical_file):
            logging.info(app, 'sending critical alert')
            email.alert('CRITICAL ALERT', 'Check PyCritcl.log for more details')
    if frequency.daily(18,0):
        if os.path.isfile(error_file):
            logging.info(app, 'sending error alert')
            email.alert('Error Alert', 'Check PyError.log for more details')
    if frequency.weekly(4,18,0):
        logging.info(app, 'sending warning alert')
        if os.path.isfile(warning_file):
            email.alert('warning alert', 'Check PyWarn.log for more details')