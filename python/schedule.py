import datetime
import os
from constant import *

# this file is used for regulating frequency of applications

app = os.path.basename(__file__)
now = datetime.datetime.now()

def weekly(weekday=0, hour=0, minutes=0):
    """Enter in weekday (monday = 0), hour (0-23), and minutes (0, 15, 30, 45)"""
    if now.weekday() == weekday and now.hour == hour and now.minute < minutes + 14 and now.minute >= minutes:
        return True
    else:
        return False

def daily(hour=0, minutes=0):
    """Enter in hour (0-23) and minutes (0, 15, 30, 45)"""
    if now.hour == hour and now.minute < minutes + 14 and now.minute >= minutes:
        return True
    else:
        return False

def hourly(minutes=0):
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
