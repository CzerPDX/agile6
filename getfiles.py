# Jonas Persson
# CS410 Agile Summer 2022 Portland State
import sys
import logging
from io import StringIO
from datetime import datetime
import os

def get_single(ftp, filename):
    ret = (False, "")
    try:
        file_to_get = "RETR " + filename
        # wb - indicates binary write mode
        server_response = ftp.retrbinary(file_to_get, open(filename, 'wb').write)       # author/source: https://pythontic.com/ftplib/ftp/retrbinary
        ret = (True, str(server_response))
    except Exception as err:
        now = datetime.now()
        errMsg = now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RETRIEVE FILE FROM FTP SERVER: " + filename + ": Server response was: " + str(err)
        logging.error(errMsg)
        ret = (False, errMsg)

    return ret

def get_directory(ftp, directory_name):
    localPath = os.getcwd()                     #Get local path
    remotePath = ftp.pwd()                      #Get remote path

    ftp.cwd(remotePath + directory_name)        #Change into directory to be copied

    newlocalPath = os.path.join(localPath, directory_name)
    
    os.mkdir(newlocalPath)                      #Make new directory in new path
    os.chdir(newlocalPath)                      #Change into the new directory

    files = ftp.nlst()                          #Get names of files in directory

    for file in files:
        if file[0:] != "." and file[0:] != "..":        #Ignores current folder and parent folder
            ftp.retrbinary("RETR "+file, open(file[0:], 'wb').write) 

    

def list_files(ftp, include_directories):

    orig_stdout = sys.stdout                    # Save the standard output identifier so it can be restored later
    sys.stdout = string_file = StringIO()       # Set standard output to the string file: string_file
    ftp.dir()                                   # Write the contents of the current remote directory to the string file
    string_file.seek(0)
    file_list = string_file.read()              # Read the contents of the string file into the string file_list
    sys.stdout = orig_stdout                    # Reset standard output to the original identifier
    final_ret_list = []                         # Final return list of files
    ret = (False, final_ret_list)

    return_file_list = []
    if include_directories:
        pass
    else:
        for line in file_list.splitlines():     # Check each file listing returned
            line_fields = line.split()
            if line_fields[0].startswith("-"):                      # If the file listing is a normal file add it's name to the list
                return_file_list.append((line_fields[8], False))
    
    # Collect the valid list entries into final_ret_list
    for entry in return_file_list:
        final_ret_list.append(entry[0])
    ret = (True, final_ret_list)

    return ret

def get_multiple(ftp, file_list):
    ret = (True, "")
    fileCnt = len(file_list)
    i = 0
    
    # Get each of the files
    while ((i < fileCnt) and (ret[0])):
        ret = get_single(ftp, file_list[i])
        i = i + 1


    # If unsuccessful, error should already be logged in get_single
    # If successful, create a good error message:
    if (ret[0]):
        successMsg = "Successfully downloaded: "
        for file in file_list:
            successMsg += " "
            successMsg += file
        ret = (True, successMsg)

        now = datetime.now()
        infoMsg = now.strftime("%m/%d/%Y %H:%M:%S ") + successMsg
    else:
        errMsg = "ERROR: get_single failed on filename: \"" + file_list[i -1] + "\""
        ret = (False, errMsg)

        now = datetime.now()
        errMsg = now.strftime("%m/%d/%Y %H:%M:%S") + errMsg
        logging.error(errMsg)

    return ret
    