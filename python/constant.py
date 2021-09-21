# THIS IS A CONSTANT FILE ALL PYTHON SCRIPTS WILL IMPORT FROM
import os

# FOLDERS
HALLPY = os.getcwd().rsplit('/', 0)[0] + '/'

# PYTHON files
PYTHON = HALLPY + 'python/'

# input files
INPUT = HALLPY + 'input/'
EMAILS = INPUT + 'emails.dat'
BACKUP_EMAILS = INPUT + 'emails_dat.bak'

# output files
OUTPUT = HALLPY + 'output/'

# logging files
LOGGING = HALLPY + 'logging/'
INFO = LOGGING + 'info.log'
OLDINFO = LOGGING + 'info.old'
ERROR = LOGGING + 'error.log'
OLDERROR = LOGGING + 'olderr.log'
CRITICAL = LOGGING + 'critical.log'
ACTIVE = LOGGING + 'active.dat'


