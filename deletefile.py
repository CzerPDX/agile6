import logging
from ftplib import FTP
from datetime import datetime

def deleteFile(ftp, fileName):

    try:
        ftpResponse = ftp.delete(fileName);
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: DELETE FILE ON FTP SERVER: " + ftpResponse)
        ret = (True, str(ftpResponse))
    except Exception as err:
        now = datetime.now()
        ret = (False, str(err))
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: DELETE FILE ON FTP SERVER: " + str(err))

    return ret
   
