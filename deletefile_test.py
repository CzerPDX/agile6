from ftplib import FTP
import pytest
import os
import deletefile
import connectftp
import loginsecure
import putfile





## connected and in a valid directory ## 
def test_delete_file(monkeypatch):
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

    #delete file call
    fileCheck = False
    putfile.put_file(ftp,'./', 'fileToBeDeleted.txt', '/')
    currDir = ftp.nlst() 

    fileToFind = "fileToBeDeleted.txt"
    if fileToFind in currDir:
        fileCheck = True 
    assert (fileCheck == True)

    deletefile.deleteFile(ftp,"fileToBeDeleted.txt")

    currDir = ftp.nlst()
    if fileToFind in currDir:
        fileToFind = False
    assert (fileCheck == True)


# Close FTP connection
    ftp.quit()
    os.remove('./fileToBeDeleted.txt')
