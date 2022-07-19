import pytest
import os
import listlocaldir



# test that list local is not null
def test_list_local_dir():
    path = os.getcwd()
    dir_list = os.listdir(path)

    assert dir_list != None;

