import pytest
import os
import renamefile
import connectftp
import loginsecure
import putfile
import deletefile


## connected and in a valid directory ## 
def test_listRemote_valid_input(monkeypatch):
    
    #create file to add to ftp server
    fp = open('fileToBeDeleted.txt', 'x')
    fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
    fp.close

    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    ##need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

    #add file to server
    fileCheck = False
    putfile.put_file(ftp,'./', 'fileToBeDeleted.txt', '/')

    #check that the file has been successfully added
    currDir = ftp.nlst() 
    fileToFind = "fileToBeDeleted.txt"
    if fileToFind in currDir:
        fileCheck = True 
    assert (fileCheck == True)

    #rename the file
    server_response = renamefile.renameFile(ftp, fileToFind, "newName.txt")

    #check that it has been renamed
    currDir = ftp.nlst()
    fileToFind = "newName.txt"
    if fileToFind in currDir:
        fileCheck = True 
    else:
        fileCheck = False

    assert (fileCheck == True)
    assert server_response[0] == True
    deletefile.deleteFile(ftp, "newName.txt")
    

# Close FTP connection
    ftp.quit()
    os.remove('./fileToBeDeleted.txt')
