from fileinput import filename
import logging
from ftplib import FTP
import os

def changePermissions(ftp, chmodKey, fileName):

    try:
        #os.stat(fileName)
        ftpResponse = ftp.sendcmd("SITE CHMOD " + chmodKey +" "+ fileName)
        #os.stat(fileName)
        logging.info(ftpResponse)
        return ftpResponse
    except Exception as err:
        logging.error(err)



