import ftplib 
import logging
from datetime import datetime

def logoff(ftp):

    try:
        ftp.quit()
        resp = (True, ("You have successfully logged out." ) )
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: LOG OUT OF FTP SERVER: " + resp[1])

    except Exception as err :
        resp = (False, str(err))
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: LOG OUT OF FTP SERVER: " + str(err)) 

    return resp