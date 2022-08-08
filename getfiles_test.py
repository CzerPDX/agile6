from operator import contains
import pytest
import putfile
import deletefile
import os
import connectftp
import loginsecure
import getfiles

## connected and in a valid directory ## 
def test_getfiles_get_single(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    ##need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

# getfiles get_single test:
    assert True == getfiles.get_single(ftp, "a.png", False)
    assert True == os.path.exists("a.png")
    
# Cleanup. Close connection and delete test files.
    ftp.quit()
    os.remove("a.png")

## connected and in a valid directory ## 
def test_getfiles_get_single(monkeypatch):
    # Establish FTP connection
    ftpAddr = os.environ['FTPADDR']
    connectionObj = connectftp.connectFTP(ftpAddr)
    ftp = connectionObj[1]

    # Get valid credentials
    usr = os.environ['FTPUSR']
    password = os.environ['FTPPASS']

    ##need this to catch password stream before loginsecure
    monkeypatch.setattr('builtins.input', lambda _: password)
    loginsecure.loginSecure(ftp, usr)

    #create 2 new files to test with
    file1 = "tab.txt"
    file2 = "tux.txt"

    # Make local versions to test with
    # Check if file1 exists. Create it if not
    if os.path.exists(file1) != True:
        fp = open(file1, 'w')
        fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
        fp.close
    assert os.path.exists(file1) == True

    # Check if file2 exists. Create it if not
    if os.path.exists(file2) != True:
        fp = open(file2, 'w')
        fp.write("This is a test file, you should not be seeing this if the test does what it's suppose to")
        fp.close
    assert os.path.exists(file2) == True

    # Put them on the server
    #def put_file(ftp, path, filename, upload_path):
    resp = putfile.put_file(ftp, "./", file1, "/")
    assert resp[0] == True
    resp = putfile.put_file(ftp, "./", file2, "/")
    assert resp[0] == True

# getfiles get_multiple test:
    test_list = [file1, file2]
    
    resp = getfiles.get_multiple(ftp, test_list)
    assert resp[0] == True
    assert True == os.path.exists(file1)
    assert True == os.path.exists(file2)

# Cleanup. Close connection and delete test files.
    # Remove files from server
    resp = deletefile.deleteFile(ftp, file1)
    assert resp[0] == True
    resp = deletefile.deleteFile(ftp, file2)
    assert resp[0] == True

    # Quit server connection
    ftp.quit()

    # Remove local copies of files
    os.remove("./" + file1)
    assert os.path.exists(file1) == False
    os.remove("./" + file2)
    assert os.path.exists(file2) == False
    