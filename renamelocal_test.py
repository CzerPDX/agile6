import pytest
from operator import contains
import os
import renamelocal
from os.path import exists

def test_rename_local_file():    

    #create a new file to be renamed then deleted
    ogFileName = "testname.txt"
    newFileName = "newTest.txt"

    # Check if the OG file exists already. Delete it if it does
    if exists("./" + ogFileName) == True:
        os.remove("./" + ogFileName)
    assert (exists("./" + ogFileName) == False)

    # Check if the new file exists already. Delete it if it does
    if exists("./" + newFileName) == True:
        os.remove("./" + newFileName)
    assert (exists("./" + newFileName) == False)

    # Create a new version of the file and make sure it exists
    fp = open("./" + ogFileName, 'x')
    fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
    fp.close
    assert (exists("./" + ogFileName) == True)

    #rename and delete if successful
    server_response = renamelocal.renameLocal(("./" + ogFileName),("./" + newFileName))
    assert (server_response[0] == True)
    assert (exists("./" + ogFileName) == False)
    assert (exists("./" + newFileName) == True)

    # Cleanup
    if exists("./" + ogFileName) == True:
        os.remove("./" + ogFileName)
    if exists("./" + newFileName) == True:
        os.remove("./" + newFileName)