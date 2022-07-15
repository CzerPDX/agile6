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
    result = saveconnection.saveConnection(label, ftpAddr, username)
    assert result[0] == True


# NOTE: Not totally sure how to test not being allowed to write yet