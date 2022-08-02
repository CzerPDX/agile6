from fileinput import filename
import logging
from ftplib import FTP
import os
from datetime import datetime

def changePermissions(ftp, chmodKey, fileName):

    try:
        #os.stat(fileName)
        ftpResponse = ftp.sendcmd("SITE CHMOD " + chmodKey +" "+ fileName)
        #os.stat(fileName)
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: CHANGE PERMISSIONS ON FTP SERVER FILE: Server response: " + ftpResponse)
        return ftpResponse
    except Exception as err:
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: CHANGE PERMISSIONS ON FTP SERVER FILE: " + str(err))



