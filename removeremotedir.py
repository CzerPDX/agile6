import logging
from ftplib import FTP

from datetime import datetime


def removeDir(ftp, toRemove):
    ret = (False, "")

    try:
        capture = ftp.rmd(toRemove)
        ret = (True, str(capture))

        logMsg = "Directory Removed. Response: " + str(capture)
        logging.info(logMsg)

    except Exception as err:
        ret = (False, err)
        logging.error(err)

        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S RESPONSE: ") + str(err))

    return ret