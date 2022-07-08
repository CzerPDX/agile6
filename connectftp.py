import logging
from ftplib import FTP


def connectFTP(ftpAddr):
    # log FTP address from attempted connection
    logging.info("Attempted FTP conection to: " + ftpAddr)
    
    try: 
        resp = (True, FTP(ftpAddr))
    except Exception as err:
        resp = (False, err)
        logging.error(err)

    return resp 