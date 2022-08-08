import logging
import deletefile

from ftplib import FTP

from datetime import datetime


def removeDir(ftp, toRemove):
    ret = (False, "")

    try:
        server_response = ftp.cwd(toRemove)
        removeFilesRec(ftp)
        ftp.cwd("..")

        capture = ftp.rmd(toRemove)
        ret = (True, str(capture))

        logMsg = "Directory Removed. Response: " + str(capture)
        logging.info(logMsg)

    except Exception as err:
        ret = (False, err)
        logging.error(err)
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S ERROR: ") + str(err))

    return ret

# Recursively remove files from directories
def removeFilesRec(ftp):
    ret = (True, "")

    # Look through the list of items in this current directory.
    # If any of them are a directory, call removeFileRec
    fileList = ftp.nlst()

    # Check each to see if it's a directory
    for item in fileList:
        if ret[0] == False:
            break
        # Don't mess with hidden files (ones that start with a ".")
        elif item[0] != ".":
            try:
                # ftp.nlst will throw an exception if argument is not a directory
                ftp.nlst(item)
                
                # If item is a directory, cd into it
                ftp.cwd(item)
                # Recursively call removeFilesRec for the current working dir
                removeFilesRec(ftp)
                # Return to parent directory
                ftp.cwd("..")
                # Remove item
                resp = ftp.rmd(item)
                ret = (True, "")
            except Exception as err:
                server_response = deletefile.deleteFile(ftp, item)
                ret = (False, str(err))

