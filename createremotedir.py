from ftplib import FTP
import logging
from datetime import datetime

def createDir(ftp):

    #Ask for a the name of the new directory
    newDir = input("What is the name of the new directory?")
    
    try:
        capture = ftp.mkd(newDir)
        ret = (True, (capture))
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: CHANGE DIRECTORY ON FTP SERVER: Directory Created")
    
    except Exception as err:
        ret = (False, err)
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: CHANGE DIRECTORY ON FTP SERVER: " + str(err))

    return ret

