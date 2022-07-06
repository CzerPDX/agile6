import logging
from ftplib import FTP

########################################
# Add includes here for your files
import login            # 1. Log into remote server

########################################

# References:
# FTPlib documentation: https://docs.python.org/3/library/ftplib.html
# Logging documentation: https://docs.python.org/3/library/logging.html
#                        https://docs.python.org/3/howto/logging.html
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python


if __name__ == "__main__":
    # Sets up logging. 
    # Uses filemode 'a' so it appends to the existing log instead of overwriting
    # Logging level: anything below the set logging level will be ignored. So it's a logging threshold
    logging.basicConfig(filename='input-and-errors.log', filemode='a', level=logging.DEBUG)

    # display menu
    prompt = """
    FTP Client TUI
    ==============
    
    1.  Log into remote server
    2.  List directories & files on remote server
    3.  Log into remote ftp server
    4.  List directories & files on remote server
    5.  Get file from remote server
    6.  Log off from remote server
    7.  Get multiple
    8.  List directories & files on  local machine
    9.  Put file onto remote server
    10. Put multiple
    11. Create directory on remote server
    12. Delete file from remote server
    13. Change permissions on remote server
    14. Copy directories on remote server
    15. Delete directories on remote server
    16. Save connection information
    17. Use saved connection information to connect
    18. Rename file on remote server
    19. Rename file on local machine
    20. Timeout after idle time
    21. Log history

    Enter your choice: 
    """

    # Some menu formatting (removes newline from the end, then adds a space)
    prompt = prompt.rstrip()
    prompt += " "

    # Take input from user and log it
    opt = input(prompt)
    logging.info(opt)

    print()
    
    
    # Process user output
    # Note: we log all input
    if opt == "1":
        # 1.  Log into remote server
        ftpAddr = 'ftptest.portlandredbird.com'
        usr = 'testacct@ftptest.portlandredbird.com'
        serverResponse = login.loginSecure(ftpAddr, usr)
        print(serverResponse)
    elif opt == "2":
        # 2.  List directories & files on remote server
        print("you chose 2")
    elif opt == "3":
        # 3.  Log into remote ftp server
        print("you chose 3")
    elif opt == "4":
        # 4.  List directories & files on remote server
        print("you chose 4")
    elif opt == "5":
        # 5.  Get file from remote server
        print("you chose 5")
    elif opt == "6":
        # 6.  Log off from remote server
        print("you chose 5")
    elif opt == "7":
        # 7.  Get multiple
        print("you chose 7")
    elif opt == "8":
        # 8.  List directories & files on  local machine
        print("you chose 8")
    elif opt == "9":
        # 9.  Put file onto remote server
        print("you chose 9")
    elif opt == "10":
        # 10. Put multiple
        print("you chose 10")
    elif opt == "11":
        # 11. Create directory on remote server
        print("you chose 11")
    elif opt == "12":
        # 12. Delete file from remote server
        print("you chose 12")
    elif opt == "13":
        # 13. Change permissions on remote server
        print("you chose 13")
    elif opt == "14":
        # 14. Copy directories on remote server
        print("you chose 14")
    elif opt == "15":
        # 15. Delete directories on remote server
        print("you chose 15")
    elif opt == "16":
        # 16. Save connection information
        print("you chose 16")
    elif opt == "17":
        # 17. Use saved connection information to connect
        print("you chose 17")
    elif opt == "18":
        # 18. Rename file on remote server
        print("you chose 18")
    elif opt == "19":
        # 19. Rename file on local machine
        print("you chose 19")
    elif opt == "20":
        # 20. Timeout after idle time
        print("you chose 20")
    elif opt == "21":
        # 21. Log history
        print("you chose 21")
    else:
        errorMsg = "Error! " + opt + " is not a valid option. Exiting..."
        print(errorMsg)
        logging.error(errorMsg)