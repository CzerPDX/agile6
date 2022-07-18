import logging
from ftplib import FTP

def deleteFile(ftp, fileName):

    try:
        ftpResponse = ftp.delete(fileName);

    except Exception as err:
        logging.error(err)

    logging.info(ftpResponse)
