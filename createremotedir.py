from ftplib import FTP
import logging

def createDir(ftp):

    #Ask for a the name of the new directory
    newDir = input("What is the name of the new directory?")
    
    try:
        capture = ftp.mkd(newDir)
        ret = (True, (capture))
        logging.info("Directory Created")
    
    except Exception as err:
        ret = (False, err)
        logging.error(err)

    return ret

