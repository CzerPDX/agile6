import pytest
from operator import contains
import os
import rename_local
from os.path import exists



## connected and in a valid directory ## 
def rename_local_file_test(monkeypatch):    

    #create a new file to be renamed then deleted
    fp = open('test.txt', 'x')
    fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
    fp.close

    #rename and delete if successful
    assert(rename_local.renameLocal('.test.txt','.newTest.txt') == True)
    if(exists('.test.txt')):
        os.remove('.test.txt')
    elif(exists('.newTest.txt')):
        os.remove('.newTest.txt')