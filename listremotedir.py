import logging
from ftplib import FTP

def listRemote(ftp):
    print("Remote files and directories: ")
    try:
        capture = ftp.nlst()
        ret = (True, (capture))
        logging.info("Remote files listed")
        
    except Exception as err:
        ret = (False, err)
        logging.error(err)

<<<<<<< HEAD
    return ret
=======
    return ret
>>>>>>> c562f4c96af11a116b77883541c7c87456fa4998
