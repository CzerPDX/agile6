import logging
from ftplib import FTP

def changePermissions(ftp, chmodKey, fileName):

    try:
        ftpResponse = ftp.sendcmd('SITE CHMOD ' + chmodKey +' '+ fileName)
    except Exception as err:
        logging.error(err)

    logging.info(ftpResponse)

