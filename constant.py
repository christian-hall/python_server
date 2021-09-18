# THIS IS A CONSTANT FILE ALL PYTHON SCRIPTS WILL IMPORT FROM
import os


app_folder = os.path.dirname(os.path.abspath(__file__))

# logging files
logging_file = app_folder + '/PyLog.log'
warning_file = app_folder + '/PyWarn.log'
error_file = app_folder + '/PyError.log'
critical_file = app_folder + '/PyCritcl.log'
run_log = app_folder + '/PyMain.log'

# emails_list (later collected from an input file)
master_email = 'christian.hall395@gmail.com'