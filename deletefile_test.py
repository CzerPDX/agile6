# import pytest
# import os
# import deletefile
# import connectftp
# import loginsecure



### Just waiting to get add new file implemented so I can add and delete a file for this test
                        ### -Nick



# ## connected and in a valid directory ## 
# def test_delete_file(monkeypatch):
#     # Establish FTP connection
#     ftpAddr = os.environ['FTPADDR']
#     connectionObj = connectftp.connectFTP(ftpAddr)
#     ftp = connectionObj[1]

#     # Get valid credentials
#     usr = os.environ['FTPUSR']
#     password = os.environ['FTPPASS']

#     ##need this to catch password stream before loginsecure
#     monkeypatch.setattr('builtins.input', lambda _: password)
#     loginsecure.loginSecure(ftp, usr)

        #delete file call
#     server_response = deletefile.deleteFile(ftp,"default.txt")
#     assert server_response == True

# # Close FTP connection
#     ftp.quit()
