from operator import contains
import pytest
import os
import changepermissions
import connectftp
import loginsecure
import putfile
import deletefile


## connected and in a valid directory ## 
def test_change_permissions(monkeypatch):

    fp = open('fileToBeDeleted.txt', 'w')
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

# Passes password into loginSecure via input
    fileCheck = False
    putfile.put_file(ftp,'./', 'fileToBeDeleted.txt', '/')
    currDir = ftp.nlst() 

    fileToFind = "fileToBeDeleted.txt"
    if fileToFind in currDir:
        fileCheck = True 
    assert (fileCheck == True)
    server_response = changepermissions.changePermissions(ftp, "777", "fileToBeDeleted.txt")
    assert server_response, server_response.find("200 Permissions changed on fileToBeDeleted")
    deletefile.deleteFile(ftp,"fileToBeDeleted.txt")

# Close FTP connection
    ftp.quit()
    os.remove('./fileToBeDeleted.txt')

## connected to server that requires authentication but not logged in ##