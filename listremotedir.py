import logging
from ftplib import FTP

<<<<<<< HEAD
def listRemote(ftp):
    print("Remote files and directories: ")
    try:
        capture = ftp.nlst()
        ret = (True, (capture))
        logging.info("Remote files listed")
        
    except Exception as err:
        ret = (False, err)
        logging.error(err)

    return ret
=======
def listRemote(ftp):    
    print("Remote files and directories: ")
    ftp.dir()
    logging.info("Remote files listed")
    
>>>>>>> 1e2347d9c921b7be8627d5afeffa2d429d16f3ea
