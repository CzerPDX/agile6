from ftplib import FTP
import logging
from datetime import datetime

def createDir(ftp, newDir):

    #Ask for a the name of the new directory
    
    
    try:
        capture = ftp.mkd(newDir)
        ret = (True, (capture))
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: CREATE DIRECTORY ON FTP SERVER: Directory Created")
    
    except Exception as err:
        ret = (False, err)
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: CREATE DIRECTORY ON FTP SERVER: " + str(err))

    return ret

