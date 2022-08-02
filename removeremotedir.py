import logging
from ftplib import FTP

from datetime import datetime


def removeDir(ftp):
    toRemove = input("Enter Directory Name:")
    try:
        capture = ftp.rmd(toRemove)
        ret = (True, (capture))

        logging.info("Directory Removed")

    except Exception as err:
        ret = (False, err)
        logging.error(err)

        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: DELETE DIRECTORY ON FTP SERVER: Directory Removed.")

    except Exception as err:
        ret = (False, err)
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: DELETE DIRECTORY ON FTP SERVER: " + str(err))
    
    return ret