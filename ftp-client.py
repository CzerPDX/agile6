import logging
import sys
from ftplib import FTP

########################################
# Add includes here for your files
import take-input

import login-secure            # 1. Log into remote server


########################################

# References:
# FTPlib documentation: https://docs.python.org/3/library/ftplib.html
# Logging documentation: https://docs.python.org/3/library/logging.html
#                        https://docs.python.org/3/howto/logging.html
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python


# Login menu that appears after you've logged into the ftp client
def postLoginMenu(welcomeMessage, ftp):
    # display menu
    logout = False

    while (logout != True):
        prompt = welcomeMessage + """
\n=========================

1.  Log off

2.  List directories & files on remote server
3.  Get file from remote server
4.  Log off from remote server
5.  Get multiple
6.  List directories & files on  local machine
7.  Put file onto remote server
8.  Put multiple
9.  Create directory on remote server
10. Delete file from remote server
11. Change permissions on remote server
12. Copy directories on remote server
13. Delete directories on remote server
14. Save connection information
15. Use saved connection information to connect
16. Rename file on remote server
17. Timeout after idle time
18. Log history

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
        # Put calls to your functions in here
        # Note: we log all input
        if opt == "1":
            print("Logging out...")
            logout = True
        elif opt == "2":
            # 2.  List directories & files on remote server
            print("you chose 2")
        elif opt == "3":
            # 3.  Get file from remote server
            print("you chose 3")
        elif opt == "4":
            # 4.  Log off from remote server
            print("you chose 4")
        elif opt == "5":
            # 5.  Get multiple
            print("you chose 5")
        elif opt == "6":
            # 6.  List directories & files on  local machine
            print("you chose 6")
        elif opt == "7":
            # 7.  Put file onto remote server
            print("you chose 7")
        elif opt == "8":
            # 8. Put multiple
            print("you chose 8")
        elif opt == "9":
            # 9. Create directory on remote server
            print("you chose 9")
        elif opt == "10":
            # 10. Delete file from remote server
            print("you chose 10")
        elif opt == "11":
            # 11. Change permissions on remote server
            print("you chose 11")
        elif opt == "12":
            # 12. Copy directories on remote server
            print("you chose 12")
        elif opt == "13":
            # 13. Delete directories on remote server
            print("you chose 13")
        elif opt == "14":
            # 15. Save connection information
            print("you chose 14")
        elif opt == "15":
            # 16. Use saved connection information to connect
            print("you chose 15")
        elif opt == "16":
            # 17. Rename file on remote server
            print("you chose 16")
        elif opt == "17":
            # 18. Rename file on local machine
            print("you chose 17")
        elif opt == "18":
            # 20. Timeout after idle time
            print("you chose 18")
        elif opt == "19":
            # 21. Log history
            print("you chose 19")
        elif (opt == "Q") or (opt == "q"):
            sys.exit(0)
        else:
            errorMsg = "Error! " + opt + " is not a valid option. Please try again..."
            print(errorMsg)
            logging.error(errorMsg)


if __name__ == "__main__":
    # Sets up logging. 
    # Uses filemode 'a' so it appends to the existing log instead of overwriting
    # Logging level: anything below the set logging level will be ignored. So it's a logging threshold
    logging.basicConfig(filename='input-and-errors.log', filemode='a', level=logging.DEBUG)

    opt = ""

    while (opt != "Q") and (opt != "q"):

        # display menu
        prompt = """
FTP Client TUI
==============

1.  Log into remote ftp server

Q.  Quit

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
            # 1.  Connect to FTP server
            
            # Connect to FTP server first so you can feed ftp obj to postLoginMenu
            ftpAddr = 'ftptest.portlandredbird.com'
            badAddr = 'afdsfsfafsa'
            #ftp = FTP(ftpAddr)
            ftp = FTP(badAddr)
            print(ftp)

            # Gather un somehow (through entry or saved connection through GUI)
            usr = 'testacct@ftptest.portlandredbird.com'

            # Login to FTP server you are connected to
            serverResponse = login.loginSecure(ftpAddr, usr, ftp)
            if serverResponse[0] == True:
                postLoginMenu(serverResponse[1], ftp)
            else:
                print(serverResponse[0]) 
        elif (opt == "Q") or (opt == "q"):
            sys.exit(0)
        else:
            errorMsg = "Error! " + opt + " is not a valid option. Please try again..."
            print(errorMsg)
            logging.error(errorMsg)