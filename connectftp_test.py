import os               # Access environment variables
import pytest           # python testing
from ftplib import FTP  # FTP library connections

import connectftp   # Module for testing

# Test with valid server
def test_connectftp_valid_server():
    # Get a valid server address
    ftpAddr = os.environ['FTPADDR']
    
    # Pass valid address to connectFTP function
    connectionResponse = connectftp.connectFTP(ftpAddr)

    # type(connectionResponse) should be a tuple
    # Should contain (bool=True, FTP object)
    assert (connectionResponse[0] == True), "Expected response[0] == True. got: {}".format(connectionResponse[0])
    assert isinstance(connectionResponse[1], FTP), "Expected type(response[1]) == FTP. got: {}".format(connectionResponse[1])


# Test with bad server
def test_connectftp_bad_server():
    # Get a bad server address
    ftpAddr = "bad_address"
    
    # Pass bad address to connectFTP function
    connectionResponse = connectftp.connectFTP(ftpAddr)

    # type(connectionResponse) should be a tuple
    # Should contain (bool=False, str)
    assert (connectionResponse[0] == False), "Expected response[0] == False. got: {}".format(connectionResponse[0])
    assert isinstance(connectionResponse[1], str), "Expected type(response[1]) == str. got: {}".format(connectionResponse[1])

