import logging

# References:
# https://www.w3schools.com/python/python_file_write.asp
# https://docs.python.org/3/library/functions.html#open



# Saves label, ftpAddr, and username to savedconnections.txt
# Currently does not care 
def saveConnection(label, ftpAddr, username):
    # Preconditions
    # Types for label, ftpAddr, and username must all be str
    # Those strings must not be empty.
    assert isinstance(label, str), "expected type(label) == str. got type: {}".format(type(label))
    assert isinstance(ftpAddr, str), "expected type(ftpAddr) == str. got type: {}".format(type(ftpAddr))
    assert isinstance(username, str), "expected type(username) == str. got type: {}".format(type(username))
    assert len(label) > 0, "expected non-empty label. got: {}".format(label)
    assert len(ftpAddr) > 0, "expected non-empty ftpAddr. got: {}".format(ftpAddr)
    assert len(username) > 0, "expected non-empty username. got: {}".format(username)

    ret = (True, "")                    # Return tuple
    filename = "savedconnections.txt"   # Filename to save connections to

    # Append the new entry: add label, ftp, and username to file (comma delimited)
    try:
        f = open(filename, "a")
    except Exception as err:
        # pass error back out to the UI
        ret = (False, err)

    if (ret[0] == True):
        try:
            f.write(label + "," + ftpAddr + "," + username)
        except Exception as err:
            # pass error back out to the UI
            ret = (False, err)

    if (ret[0] == True):
        try: 
            f.close()
            successMsg = "Successfully added new connection information"
            logging.info(successMsg)
            ret = (True, successMsg)
        except Exception as err:
            # pass error back out to the UI
            ret = (False, err)

    
    # Postconditions
    # ret must be a tuple of size 2
    # ret[0] must be a bool
    # ret[1] must be a str
    assert isinstance(ret, tuple), "expected type(ret) == tuple. got type: {}".format(type(ret))
    assert len(ret) == 2, "expected len(ret) == 2. got len(ret) == : {}".format(len(ret))
    assert isinstance(ret[0], bool), "expected type(ret[0]) == bool. got type: {}".format(type(ret[0]))
    assert isinstance(ret[1], str), "expected type(ret[1]) == str. got type: {}".format(type(ret[1]))

    return ret