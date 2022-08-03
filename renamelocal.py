import os
from os import path 
import logging

def renameLocal(old_name, new_name):
    ret = (False, "")
    # Absolute path of a file

    # Check if the old file actually exists
    if (os.path.exists(old_name) == False):
        errMsg = "Cannot rename. " + old_name + " does not exist."
        ret = (False, errMsg)
        logging.error(errMsg)
    # Check that the new file does NOT exist
    elif (os.path.exists(new_name) == True):
        errMsg = "Cannot rename. " + new_name + " already exists."
        ret = (False, errMsg)
        logging.error(errMsg)
    # Renaming the file
    else:
        try:
            os.rename(old_name, new_name)
            infoMsg = "Local file changed from" + old_name + " to" + new_name
            ret = (True, infoMsg)
        except Exception as err:
            errMsg = str(err)
            ret = (False, errMsg)
            logging.error(errMsg)

    return ret


