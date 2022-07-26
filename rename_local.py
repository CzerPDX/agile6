import os
from os import path 
import logging

def renameLocal(old_name, new_name):
    # Absolute path of a file

    if(os.path.exists(old_name) and (os.path.exists(new_name) == False)):
    # Renaming the file
        try:
            os.rename(old_name, new_name)
        except Exception as err:
            print(err)
        logging.info("Local file changed from" + old_name + " to" + new_name)
        return True
    return False


