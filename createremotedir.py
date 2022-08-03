from ftplib import FTP
import logging
from datetime import datetime

def createDir(ftp, newDir):
    ret = (False, "")

    #Ask for a the name of the new directory
    try:
        capture = ftp.mkd(newDir)
        ret = (True, str(capture))

        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S INFO: ") + str(capture))

    except Exception as err:
        ret = (False, str(err))
        logging.error(err)

        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S ERROR: ") + str(err))

    return ret

