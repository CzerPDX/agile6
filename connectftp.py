import logging
from ftplib import FTP
from datetime import datetime

def connectFTP(ftpAddr):
    # Preconditions
    # type(ftpAddr) should be: str
    assert isinstance(ftpAddr, str), "expected type(ftpAddr) == str. got type: {}".format(type(ftpAddr))

    # log FTP address from attempted connection
    now = datetime.now()
    logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: CONNECT TO FTP SERVER: Connected to: " + ftpAddr)
    
    try: 
        resp = (True, FTP(ftpAddr, timeout=1))
    except Exception as err:
        resp = (False, str(err))
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: CONNECT TO FTP SERVER: Failed FTP connection to: " + str(err))

    # Postconditions
    # Returns type: tuple of size 2
    # If resp[0] == True, then resp[1] == FTP
    # If resp[0] == False, then resp[1] == err
    assert isinstance(resp, tuple), "expected type(resp) == tuple. got type: {}".format(type(resp))
    assert (len(resp) == 2), "expected tuple of length 2. got length: {}".format(len(resp))
    assert (
        ((resp[0] == True) and isinstance(resp[1], FTP))
        or
        ((resp[0] == False) and isinstance(resp[1], str))
    ), "expected resp to contain (bool=True, FTP) or (bool=False, str). got: (bool={}, {})".format(resp[0], type(resp[1]))

    return resp 