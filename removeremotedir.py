import logging
from ftplib import FTP

def removeDir(ftp):
    toRemove = input("Enter Directory Name:")
    try:
        capture = ftp.rmd(toRemove)
        ret = (True, (capture))
        logging.info("Directory Removed")

    except Exception as err:
        ret = (False, err)
        logging.error(err)
    
    return ret