import logging
from ftplib import FTP
from datetime import datetime


def listRemote(ftp):
    print("Remote files and directories: ")
    try:
        capture = ftp.nlst()
        ret = (True, (capture))
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: LIST FILES ON FTP SERVER: Remote files listed")
        
    except Exception as err:
        ret = (False, err)
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: LIST FILES ON FTP SERVER: " + str(err))

    return ret
