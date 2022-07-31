import logging
from ftplib import FTP
from datetime import datetime

# Returns a tuple of (bool, str)
def loginSecure(ftp, usr):
    # Preconditions 
    # type(ftp) should be: FTP
    # type(usr) should be: str
    # usr should not be an empty string
    assert isinstance(ftp, FTP), "expected type(ftp) == ftplib.FTP. got type: {}".format(type(ftp))
    assert isinstance(usr, str), "expected type(usr) == str. got type: {}".format(type(str))
    assert (len(usr) > 0), "expected non-empty string for usr. got: {}".format(str)

    resp = (True, "")
    # log username from attempted login
    now = datetime.now()
    logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: LOGIN: " + "Attempted login: " + usr)

    # log into ftp server and return the login response from the server
    try:
        ftp.login(user=usr, passwd=input("enter pw: "))
        resp = (True, (ftp.getwelcome()))
        now = datetime.now()
        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: LOGIN: SERVER MESSAGE: " + resp[1])
    # if an error occurs, return the error
    except Exception as err:
        resp = (False, str(err))
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: FTP LOGIN: " + str(err))
        
    print()

    # Postconditions: 
    # resp should be a tuple of length 2
    # resp should be a tuple in the form: (bool, str))
    assert isinstance(resp, tuple), "expected type(resp) == tuple. got type: {}".format(type(resp))
    assert len(resp) == 2, "expected tuple of length 2. got length: {}".format(len(resp))
    assert isinstance(resp[0], bool), "expected type(resp[0]) == bool. got type: {}".format(type(resp[1]))
    assert isinstance(resp[1], str), "expected type(resp[1]) == str. got type: {}".format(type(resp[1]))
    
    return resp