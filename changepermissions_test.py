from operator import contains
import pytest
import os
import changepermissions
import connectftp
import loginsecure


## connected and in a valid directory ## 
def test_change_permissions(monkeypatch):
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

# Passes password into loginSecure via input
    server_response = changepermissions.changePermissions(ftp, "777", "noread")
    assert server_response, server_response.find("200 Permissions changed on noread")

# Close FTP connection
    ftp.quit()

## connected to server that requires authentication but not logged in ##