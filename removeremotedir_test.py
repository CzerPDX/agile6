import pytest
import os
import removeremotedir
import createremotedir
import connectftp
import loginsecure


## connected and in a valid directory ## 
def test_listRemote_valid_input(monkeypatch):
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

    # Create a test directory name
    testDir = "testDir"

    # Add a test directory to the ftp server
    createremotedir.createDir(ftp, testDir)

    #call list remote
    server_response = removeremotedir.removeDir(ftp, testDir)
    assert server_response[0] == True

# Close FTP connection
    ftp.quit()
