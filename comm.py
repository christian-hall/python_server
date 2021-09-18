import os
import datetime
from shutil import copyfile
import socket
import smtplib
import ssl
from constant import *

# App info
app = 'COMMUNICATIONS'

class file:
    app = 'FILE MANAGEMENT'
    def append(filepath, message):
        try:
            with open(filepath, 'a') as file:
                file.write(message)
        except:
            print('error ' + filepath)

    def delete(filepath):
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            logging.info(app, filepath + ' did not exist')
            

    def copy(filepath, copy_filepath):
        try:
            if os.path.isfile(copy_filepath):
                file.delete(copy_filepath)
            copyfile(filepath, copy_filepath)
        except:
            logging.error(app, 'unable to copy to ' + copy_filepath + ' from ' + filepath)

class logging:
    app = 'LOGGING'
    def info(app, message):
        """Stored in PyLog.log"""
        file.append(logging_file, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

    def warning(app, message):
        """Stored in PyWarn.log, emailed once a week, Fridays at 6 PM"""
        file.append(warning_file, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

    def error(app, message):
        """Stored in PyError.log, emailed daily at 6 PM"""
        file.append(error_file, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

    def critical(app, message):
        """Stored in PyCrit.log, emailed every hour"""
        file.append(critical_file, (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n' + app + '\n' + message + '\n\n'))

    def run():
        """Logs when the server runs for simpler review"""
        file.append(run_log, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

class connectivity:
    app = 'CONNECTIVITY'
    def online():
        ip_address =socket.gethostbyname(socket.gethostname())
        if ip_address == "127.0.0.1":
            return False
        else:
            return True

class email:
    app = 'EMAIL'
    sender = 'alerts.halltech@gmail.com'
    password = '1!0vE2C0d3!'
    port = 465

    def alert(subject, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", email.port, context=context) as server:
            try:
                server.login(email.sender, email.password)
                try:
                    message = 'Subject: ' + subject + '\n\n' + message
                    server.sendmail(email.sender, master_email, message)
                except:
                    logging.error(app, 'unable to send email to ' + master_email)
            except:
                logging.error(app, 'unable to log in email ' + email.sender)
    
    def notify(subject, message, receiver):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", email.port, context=context) as server:
            try:
                server.login(email.sender, email.password)
                try:
                    message = 'Subject: ' + subject + '\n\n' + message
                    server.sendmail(email.sender, receiver, message)
                except:
                    logging.error(app, 'unable to send email to ' + receiver)
            except:
                logging.error(app, 'unable to log in email ' + email.sender)
