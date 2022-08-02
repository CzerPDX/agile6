# Jonas Persson
# CS410 Agile Summer 2022 Portland State
import sys
import logging
from io import StringIO
from datetime import datetime

def get_single(ftp, filename, is_directory):

    if is_directory:
        get_directory(ftp, filename)
    else:
        try:
            file_to_get = "RETR " + filename
            ftp.retrbinary(file_to_get, open(filename, 'wb').write)       # author/source: https://pythontic.com/ftplib/ftp/retrbinary
            return True
        except Exception as err:                                                 # wb - indicates binary write mode
            now = datetime.now()
            logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RETRIEVE FILE FROM FTP SERVER: " + filename + ": Server response was: " + str(err))
            return False

    return False

def get_directory(ftp, directory_name):
    pass

def list_files(ftp, include_directories):

    orig_stdout = sys.stdout                    # Save the standard output identifier so it can be restored later
    sys.stdout = string_file = StringIO()       # Set standard output to the string file: string_file
    ftp.dir()                                   # Write the contents of the current remote directory to the string file
    string_file.seek(0)
    file_list = string_file.read()              # Read the contents of the string file into the string file_list
    sys.stdout = orig_stdout                    # Reset standard output to the original identifier

    return_file_list = []
    if include_directories:
        pass
    else:
        for line in file_list.splitlines():     # Check each file listing returned
            line_fields = line.split()
            if line_fields[0].startswith("-"):                      # If the file listing is a normal file add it's name to the list
                return_file_list.append((line_fields[8], False))

    return return_file_list

def get_multiple(ftp, file_list):
    success_flag = True
    for file in file_list:
        if get_single(ftp, file[0], file[1]) is False:
            success_flag = False
    return success_flag
    