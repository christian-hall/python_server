# all connections and codes for the internet are here, including checking for online status
import os
import socket
import logging

app = os.path.basename(__file__)

def online():
    """checks internet connection status, returns True or False"""
    ip_address =socket.gethostbyname(socket.gethostname())
    if ip_address == "127.0.0.1":
        logging.error(app, 'Device is currently offline')
        return False
    else:
        logging.info(app, 'Application is online')
        return True
