import ftplib 
import logging
import os
from datetime import datetime

#Allows the user to upload a file from thier local system.
def put_file(ftp, path, filename, upload_path):
    ret = (True, "default")
    
    #Has the user input the path to the file on their local machine.
    try:
        os.chdir(path)
        #correct = True
    except Exception as err:
        ret = (False, str(err))
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RESPONSE: " + str(err))


    if (ret[0] == True):
        #Changes to the upload path.
        try:
            ftp.cwd(upload_path)
            #correct = True
        except Exception as err:
            ret = (False, str(err))
            now = datetime.now()
            logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RESPONSE: " + str(err))
            

    
    if (ret[0] == True):
        # Uploads the file as a binary file this allows for more than text files.
        try:
            with open(filename, "rb") as file:
                resp = ftp.storbinary(f"STOR {filename}", file)
                ret = (True, str(resp))
        except Exception as err:
            ret = (False, str(err))
            now = datetime.now()
            logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RESPONSE: " + str(err))

    
    return ret
