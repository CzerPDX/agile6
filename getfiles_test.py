from operator import contains
import pytest
import os
import connectftp
import loginsecure
import getfiles

## connected and in a valid directory ## 
def test_getfiles_get_single(monkeypatch):
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

# getfiles get_single test:
    assert True == getfiles.get_single(ftp, "a.png", False)
    assert True == os.path.exists("a.png")

# Close FTP connection
    ftp.quit()
