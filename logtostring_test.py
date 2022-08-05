import logtostring
import os

def test_process_log_file(monkeypatch):

    test_file_data = "INFO:root:08/02/2022 20:48:15 COMMAND: MENU OPTION: 3\nINFO:root:08/02/2022 20:48:31 COMMAND: ADD NEW SAVED FTP SERVER: Saving new FTP connection\nINFO:root:08/02/2022 20:48:39 COMMAND: NEW CONNECTION INFORMATION: Successfully added new connection information: ftpuser,127.0.0.1,ftpuser"
    test_1_boolean = False
    test_2_boolean = False

    # Create a test log file for the process_log_file function to read:
    f = open("test_log.txt", "a")
    f.write(test_file_data)
    f.close()

    # Call the process_log_file function to check if it reads the test file format correctly
    test_string = logtostring.process_log_file("test_log.txt")

    if "08/02/2022 20:48:31 COMMAND: ADD NEW SAVED FTP SERVER: Saving new FTP connection" in test_string:
        test_1_boolean = True

    if "08/02/2022 20:48:39 COMMAND: NEW CONNECTION INFORMATION: Successfully added new connection information: ftpuser,127.0.0.1,ftpuser" in test_string:
        test_2_boolean = True

    assert test_1_boolean is True
    assert test_2_boolean is True

    os.remove("test_log.txt")
