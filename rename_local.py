import os
import logging

def renameLocal(old_name, new_name):
    # Absolute path of a file

    if(os.path.isfile(old_name) and os.path.isfile(new_name)):
    # Renaming the file
        os.rename(old_name, new_name)
        logging.info("Local file changed from" + old_name + " to" + new_name)
        return True
    return False


