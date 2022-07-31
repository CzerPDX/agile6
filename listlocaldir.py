import logging
import os
from datetime import datetime
 
def listLocal():
    # Get the list of all files and directories
    path = os.getcwd()
    dir_list = os.listdir(path)
    
    now = datetime.now()
    logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: LIST FILES ON FTP SERVER: Local files listed")
    print("Files and directories in '", path, "' :")
    print(dir_list)
