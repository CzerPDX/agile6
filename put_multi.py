import ftplib 
import logging
import os

def put_multi_file(ftp, path, filename, upload_path):
    #Has the user input the path to the file on their local machine.
    try:
        os.chdir(path)
        correct = True;
    except:
        print("That source doesn't exist on your local machine.")
        return False;

    #Changes to the upload path.
    try:
        ftp.cwd(upload_path);
        correct = True;

    except:
        print("That directory doesn't exist on this server")
        return False;
    
    #Uploads the file as a binary file this allows for more than text files.
    try:
        with open(filename, "rb") as file:
            ftp.storbinary(f"STOR {filename}", file)
    except:
        print("An error occured when putting the file on the server.")
        return False;