import logging
from ftplib import FTP

def listRemote(ftp):    
    print("Remote files and directories: ")
    ftp.dir()
    logging.info("Remote files listed")
    
