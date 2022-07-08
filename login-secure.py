import logging
from ftplib import FTP

# Returns a tuple of (bool, string)
# If success it will be: (True, welcomeMessage, ftp object)
# If failure it will be: (False, Error message)
def login-secure(ftpAddr, usr, ftp):
    # log ftpAddr and username to log
    logging.info("Attempted login: " + ftpAddr + ", " + usr)

    # log into ftp server and return the login response from the server
    try:
        ftp.login(user=usr, passwd=input("enter pw: "))
        resp = (True, ftp.getwelcome(), ftp)
        logging.info(resp)
    # if an error occurs, return the error
    except Exception as err:
        resp = (False, err)
        logging.error(err)

    return resp