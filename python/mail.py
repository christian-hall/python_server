# all use of emails needs to be done through this script and this script alone.
import os
import smtplib
import ssl
from filing import append_file, copy_file
import logging
from constant import EMAILS, BACKUP_EMAILS

app = os.path.basename(__file__)

class account:
    # this will be a .dat file now, but will later be a mySQL script
    def __init__(self, name, address, password, port, description):
        self.name = name
        self.address = address
        self.password = password
        self.port = port
        self.description = description
    
    def to_string(self):
        return f'NAME: {self.name} ADDRESS: {self.address}'

    def get_email(name):
        """gets an email object based off it's name"""
        if os.path.isfile(EMAILS):
            logging.info(app, 'Found EMAILS file')
            with open(EMAILS, 'r') as file:
                for line in file:
                    if '#' not in line and name in line:
                        collected = line.split(';')
                        logging.info(app, f'Found {name}')
                        file.close()
                        return account(collected[0], collected[1], collected[2], int(collected[3]), collected[4])
            file.close()
            logging.error(app, f'Email with name of {name} has not been found')
            return None
        else:
            logging.critical(app, 'missing EMAIL.DAT, creating new one')
            check_email_dat()
            return None

def send_basic_email(subject, message, sender='master_alert', receiver='owner'):
    sender = account.get_email(sender)
    receiver = account.get_email(receiver)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", sender.port, context=context) as server:
        try:
            server.login(sender.address, sender.password)
            try:
                message = 'Subject: ' + subject + '\n\n' + message
                server.sendmail(sender.address, receiver.address, message)
            except:
                logging.error(app, 'unable to send email to ' + receiver.address)
        except:
            logging.error(app, 'unable to log in email ' + sender.address)


def check_email_dat():
    """checks for input/emails.dat and creates a new template file if it is not found"""
    if os.path.isfile(EMAILS):
        logging.info(app, 'EMAILS.DAT has been found')
    elif os.path.isfile(BACKUP_EMAILS):
        logging.error(app, 'EMAILS.DAT is missing, restoring backup')
        copy_file(BACKUP_EMAILS, EMAILS)
    else:
        logging.critical(app, 'all email addresses are missing')

        EMAIL_CREATE_TEXT = ['# NAME;ADDRESS;PASSWORD;PORT;DESC;',
        'NAME=(name you want use to get the email information)',
        '# ADDRESS=(name of the email address you want to use)',
        '# PASSWORD=(password of email account you want to use)',
        '# PORT = (port number you want to use)',
        '# DESC = any information you want to use',
        '# ";" must come after PORT even if you don\'t use a description',
        '# senders just need NAME;ADDRESS;;;',
        '#',
        '# needed emails:',
        '# master_alert - needed for sending alerts',
        '# owner - needed for receiving alerts',
        '#']
        for line in EMAIL_CREATE_TEXT:
            append_file(EMAILS, line)
