import ftplib 
import logging

def logoff(ftp):

    try:
        ftp.quit()
        resp = (True, ("\n You have successfully logged out." ) )
        logging.info(resp)

    except Exception as err :
        resp = (False, str(err))
        logging.error(err) 

    return resp