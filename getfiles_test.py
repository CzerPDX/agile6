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
    
# Cleanup. Close connection and delete test files.
    ftp.quit()
    os.remove("a.png")

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

# getfiles get_multiple test:
    test_list = [('a.png', False), ('tux.png', False)]
    
    assert True == getfiles.get_multiple(ftp, test_list)
    assert True == os.path.exists("a.png")
    assert True == os.path.exists("tux.png")

# Cleanup. Close connection and delete test files.
    ftp.quit()
    os.remove("a.png")
    os.remove("tux.png")
    