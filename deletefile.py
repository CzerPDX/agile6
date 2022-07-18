import logging
from ftplib import FTP

def deleteFile(ftp, fileName):

    try:
        ftpResponse = ftp.delete(fileName);
        logging.info(ftpResponse)
    except Exception as err:
        logging.error(err)

   
