import pytest
import os
import deletefile
import connectftp
import loginsecure
import rename_local


## connected and in a valid directory ## 
def test_delete_file(monkeypatch):
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

    test_file = 
    assert(rename_local.renameLocal())

# Close FTP connection
    ftp.quit()