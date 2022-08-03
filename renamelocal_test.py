import pytest
from operator import contains
import os
import renamelocal
from os.path import exists

def test_rename_local_file():    

    #create a new file to be renamed then deleted
    fp = open('test.txt', 'x')
    fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
    fp.close

    #rename and delete if successful
    assert(renamelocal.renameLocal('./test.txt','./newTest.txt') == True)
    if(exists('./newTest.txt')):
        os.remove('./newTest.txt')
    else:
        os.remove('./test.txt')