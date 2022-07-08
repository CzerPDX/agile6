import logging
from ftplib import FTP

def loginSecure(ftpAddr, usr):
    # Connect to ftp server
    ftp = FTP(ftpAddr)

    # log ftpAddr and username to log
    logging.info("Attempted login: " + ftpAddr + ", " + usr)

    # log into ftp server and return the login response from the server
    try:
        resp = ftp.login(user=usr, passwd=input("enter pw: "))
        logging.info(resp)
    # if an error occurs, return the error
    except Exception as err:
        resp = err
        logging.error(err)

    return resp