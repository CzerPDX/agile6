from operator import contains
import pytest
import os
import connectftp
import loginsecure
import rename_local



## connected and in a valid directory ## 
def rename_local_file_test(monkeypatch):
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

    
    fp = open('test.txt', 'x')
    fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
    fp.close

    assert(rename_local.renameLocal('.test.txt','.newTest.txt') == True)

# Close FTP connection
    ftp.quit()