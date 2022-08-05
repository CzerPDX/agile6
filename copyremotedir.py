from ftplib import FTP
import logging
import getfiles
import os
from datetime import datetime

def copyDir(ftp, toCopy):

    try:
        localPath = os.getcwd()                     #Get local path
        ret = (True, "")
    
    except Exception as err:
        ret = (False, err)
        logging.error(err)

<<<<<<< HEAD
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))
=======

    getfiles.get_directory(ftp, toCopy)          #Download Copy
>>>>>>> d23f7b617d5d4ec64420bd16e366fe8f32c8e474

    if(ret[0]):

        try:
            remotePath = ftp.pwd()
            ret = (True, "")
    
        except Exception as err:
            ret = (False, err)
            logging.error(err)

            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))


    if(ret[0]):
        try:
            getfiles.get_directory(ftp, toCopy)          #Download Copy
            ret = (True, "")
    
        except Exception as err:
            ret = (False, err)
            logging.error(err)

            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))
        
        
    if(ret[0]):
        try:
            newlocalPath = os.path.join(localPath, toCopy)
            ret = (True, "")
    
        except Exception as err:
            ret = (False, err)
            logging.error(err)

            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))

    

    if(ret[0]):
        try:
            capture = os.chdir(newlocalPath)
            ret = (True, str(capture))
    
        except Exception as err:
            ret = (False, err)
            logging.error(err)

            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))

    if(ret[0]):
        try:
            newremotePath = remotePath + '/Copy of ' + toCopy
            ftp.mkd(newremotePath)
            ftp.cwd(newremotePath)

            ret = (True, "")
    
        except Exception as err:
            ret = (False, err)
            logging.error(err)

            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: " + str(err))
 


    newremotePath = remotePath + '/Copy of ' + toCopy
    ftp.mkd(newremotePath)
    ftp.cwd(newremotePath)
            
    files = os.listdir()
    for file in files:
        ftp.storbinary('STOR ' + file, open(file[0:], 'rb'))   #Upload Copy


    for file in files:
        toRemove = os.path.join(newlocalPath, file)     #Delete temp copy files
        os.remove(toRemove)
            
    os.rmdir(newlocalPath)
    os.rmdir(newlocalPath)                              #Delete temp copy directory



        





