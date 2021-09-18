import datetime
import os
from comm import file, logging
from constant import *
now = datetime.datetime.now()
class frequency:
    app = 'FREQUENCY REGULATOR'

    def weekly(weekday, hour, minutes):
        """Enter in weekday (monday = 0), hour (0-23), and minutes (0, 15, 30, 45)"""
        if now.weekday() == weekday and now.hour == hour and now.minute < minutes + 14 and now.minute >= minutes:
            return True
        else:
            return False
    
    def daily(hour, minutes):
        """Enter in hour (0-23) and minutes (0, 15, 30, 45)"""
        if now.hour == hour and now.minute < minutes + 14 and now.minute >= minutes:
            return True
        else:
            return False

    def hourly(minutes):
        """Enter in minutes (0, 15, 30, 45)"""
        if now.minute < minutes + 14 and now.minute >= minutes:
            return True
        else:
            return False

    def half_hour(direction='V'):
        """Enter in 'V' for 0 and 30 minutes, 'H' for 15 and 45 minutes"""
        if direction.upper() == 'H':
            minutes_1, minutes_2 = 15, 45
        else:
            minutes_1, minutes_2 = 0, 30
        if (now.minute < minutes_1 + 14 and now.minute >= minutes_1) or (now.minute < minutes_2 + 14 and now.minute >= minutes_2):
            return True
        else:
            return False
    
    def quarter_hour():
        return True

class file_regulator:
    app='FILE REGULATOR'

    def size(filepath, size):
        if os.path.isfile(filepath):
            if os.path.getsize(filepath) > size:
                logging.info(file_regulator.app, filepath + ' is too over ' + str(size) + ', backing up and deleting')
                file.copy(filepath, filepath.split('.')[0] + '.bak')
                file.delete(filepath)
