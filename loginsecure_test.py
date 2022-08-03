import connectftp       # Use to create a valid connection
import loginsecure      # Module for testing

import pytest           # Python testing
import os               # Access environment variables
from ftplib import FTP  # Create ftp object

# References
# https://discuss.dizzycoding.com/how-to-test-a-function-with-input-call/
# https://www.geeksforgeeks.org/python-os-environ-object/



# Test with valid credentials
def test_loginSecure_valid_credentials(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    # Passes password into loginSecure via input
    monkeypatch.setattr('builtins.input', lambda _: password)
    serverResponse = loginsecure.loginSecure(ftp, usr)
    assert serverResponse[0] == True

    # Close FTP connection
    ftp.quit()

# Test with bad password
def test_loginSecure_bad_password(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]
    
    # Get valid username
    usr = os.environ['FTPUSR']

    # Passes bad password into loginSecure via input
    monkeypatch.setattr('builtins.input', lambda _: "bad_password")
    serverResponse = loginsecure.loginSecure(ftp, usr)
    assert serverResponse[0] == False

# Test with bad username
def test_loginSecure_bad_username(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Set up bad username
    usr = "bad_username"

    # Passes bad password into loginSecure via input
    #monkeypatch.setattr('builtins.input', lambda _: "bad_password")
    serverResponse = loginsecure.loginSecure(ftp, usr)
    assert serverResponse[0] == False
    # Close FTP connection
    ftp.quit()