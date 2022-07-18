import logging

SAVED_CONNECTIONS_FILE = "savedconnections.txt"   # Filename to save connections to


# References:
# https://www.w3schools.com/python/python_file_write.asp
# https://docs.python.org/3/library/functions.html#open
# https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
# https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
# https://stackoverflow.com/questions/39112645/save-line-in-file-to-list
# https://www.codegrepper.com/code-examples/python/store+each+line+of+text+file+in+list+python


# Escape all commas
def checkCommas(label, ftpAddr, username):
    # Preconditions
    assert isinstance(label, str), "expectd type(label) == str. got type: {}".format(type(label))
    assert isinstance(ftpAddr, str), "expectd type(ftpAddr) == str. got type: {}".format(type(ftpAddr))
    assert isinstance(username, str), "expectd type(username) == str. got type: {}".format(type(username))

    comma = ","
    ret = (True, "")            # Return tuple

    # If there are commas 
    if (comma in label):
        err = "Error. Commas are not allowed in saved connection entries. \"" + label + "\" contains a comma."
        ret = (False, err)
        logging.error(err)
    elif (comma in ftpAddr):
        err = "Error. Commas are not allowed in saved connection entries. \"" + ftpAddr + "\" contains a comma."
        ret = (False, err)
        logging.error(err)
    elif (comma in username):
        err = "Error. Commas are not allowed in saved connection entries. \"" + username + "\" contains a comma."
        ret = (False, err)
        logging.error(err)

    # Postconditions
    # ret must be a tuple of size 2
    # ret[0] must be a bool
    # ret[1] must be a str
    assert isinstance(ret, tuple), "expected type(ret) == tuple. got type: {}".format(type(ret))
    assert len(ret) == 2, "expected len(ret) == 2. got len(ret) == : {}".format(len(ret))
    assert isinstance(ret[0], bool), "expected type(ret[0]) == bool. got type: {}".format(type(ret[0]))
    assert isinstance(ret[1], str), "expected type(ret[1]) == str. got type: {}".format(type(ret[1]))

    return ret


# Saves label, ftpAddr, and username to savedconnections.txt
def saveConnection(label, ftpAddr, username, filename=SAVED_CONNECTIONS_FILE):
    # Preconditions
    # Types for label, ftpAddr, and username must all be str
    # Those strings must not be empty.
    assert isinstance(label, str), "expected type(label) == str. got type: {}".format(type(label))
    assert isinstance(ftpAddr, str), "expected type(ftpAddr) == str. got type: {}".format(type(ftpAddr))
    assert isinstance(username, str), "expected type(username) == str. got type: {}".format(type(username))
    assert len(label) > 0, "expected non-empty label. got: {}".format(label)
    assert len(ftpAddr) > 0, "expected non-empty ftpAddr. got: {}".format(ftpAddr)
    assert len(username) > 0, "expected non-empty username. got: {}".format(username)

    ret = (True, "")            # Return tuple

    # Check for commas first (commas are not allowed)
    try:
        ret = checkCommas(label, ftpAddr, username)
    except Exception as err:
        ret = (False, str(err))
        logging.error(err)

    # Append the new entry to the file: add label, ftp, and username to file (comma delimited)
    if (ret[0] == True):
        try:
            f = open(filename, "a")
        except Exception as err:
            # pass error back out to the UI
            ret = (False, str(err))
            logging.error(err)

    # Write to the file
    if (ret[0] == True):
        try:
            writeToFile = label + "," + ftpAddr + "," + username + '\n'
            f.write(writeToFile)
            successMsg = "Successfully added new connection information: " + writeToFile.rstrip('\n')
            logging.info(successMsg)
        except Exception as err:
            # pass error back out to the UI
            ret = (False, str(err))
            logging.error(err)

    # Close the file
    if (ret[0] == True):
        try: 
            f.close()
            ret = (True, successMsg)
        except Exception as err:
            # pass error back out to the UI
            ret = (False, str(err))
            logging.error(err)

    
    # Postconditions
    # ret must be a tuple of size 2
    # ret[0] must be a bool
    # ret[1] must be a str
    assert isinstance(ret, tuple), "expected type(ret) == tuple. got type: {}".format(type(ret))
    assert len(ret) == 2, "expected len(ret) == 2. got len(ret) == : {}".format(len(ret))
    assert isinstance(ret[0], bool), "expected type(ret[0]) == bool. got type: {}".format(type(ret[0]))
    assert isinstance(ret[1], str), "expected type(ret[1]) == str. got type: {}".format(type(ret[1]))

    return ret

    


# Read saved connections from file and return as a list
def loadSavedConnections(filename=SAVED_CONNECTIONS_FILE):
    buf = []
    ret = []

    # Save each line as a string in a list
    with open(filename) as infile:
        for line in infile:
            lineBuffer = line.strip()
            lineBuffer = lineBuffer.split('\n')
            buf.append(lineBuffer[0])

    # Save each line in ret as a list of 3 strings
    for line in buf:
        listBuffer = line.split(',')
        ret.append(listBuffer)


    return ret

        
