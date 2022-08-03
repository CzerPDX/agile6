import pytest
import os
import createremotedir
import removeremotedir
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

    # Set up a directory in a valid location
    testDir = "testDir"       # name of the test directory

    # Check if the directory exists already on the ftp server
    

    #   Delete the test directory if it already exists
    removeremotedir.removeDir(ftp, testDir)
    
    # Then use createremotedir function to create the testDir
    server_response = createremotedir.createDir(ftp, testDir)
    assert server_response[0] == True

    # Then delete the test directory
    exists = os.path.isdir(testDir)
    if (exists):
        ftp.rmd(ftp, testDir)
    exists = os.path.exists(testDir)
    assert exists == False, "Delete did not work. Test directory testDir still exists".format(type(ftpAddr))
    



# Close FTP connection
    ftp.quit()
