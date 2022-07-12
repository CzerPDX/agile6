import logging
import os
 
def listLocal():
    # Get the list of all files and directories
    path = os.getcwd()
    dir_list = os.listdir(path)
    
    logging.info("Local files listed")
    print("Files and directories in '", path, "' :")
    print(dir_list)
