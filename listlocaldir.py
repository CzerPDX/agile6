import logging
import os
from datetime import datetime
 
def listLocal(path):
    ret = (False, "")
    # Get the list of all files and directories

    try:
        dir_list = os.listdir(path)
        ret = (True, dir_list)
    except Exception as err:
        ret = (False, str(err))

        now = datetime.now()
        errMsg = now.strftime("%m/%d/%Y %H:%M:%S") + str(err)
        logging.err(errMsg)
      
    return ret