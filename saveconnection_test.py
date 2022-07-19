import pytest
import os
import connectftp
import loginsecure

import saveconnection


# Able to save and append to file without issue
def test_saveConnection_valid(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    # Need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

    # Set up valid input for the save connection
    label = "test label"
    ftpAddr = "test.ftp.address"
    username = "testusername@test.ftp.address"

    # Test function
<<<<<<< HEAD
    result = saveconnection.saveConnection(label, ftpAddr, username, "testsavedconnections.txt")
    assert result[0] == True


# Tries to write to a directory with no write access (read access exists, however)
def test_saveConnection_not_valid(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    # Need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

    # Set up bad input for the save connection
    label = "test label"
    ftpAddr = "test.ftp.address"
    username = "testusername@test.ftp.address"

    # Test function
    result = saveconnection.saveConnection(label, ftpAddr, username, "test/testlog.txt")
    assert result[0] == False

# Tries to give a label, ftpAddr, or username that contains a comma (not allowed)
def test_saveConnection_not_valid(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    # Need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

    # Set up bad input for the save connection
    label = "test, label"
    ftpAddr = "test,ftp.address"
    username = "testusername@test,ftp.address"

    # Test function
    result = saveconnection.saveConnection(label, ftpAddr, username, "testsavedconnections.txt")
    assert result[0] == False
=======
    result = saveconnection.saveConnection(label, ftpAddr, username)
    assert result[0] == True


# NOTE: Not totally sure how to test not being allowed to write yet
>>>>>>> main
