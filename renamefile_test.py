import pytest
import os
import renamefile
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

    #call list remote
    server_response = renamefile.renameFile(ftp)
    assert server_response[0] == True

# Close FTP connection
    ftp.quit()
