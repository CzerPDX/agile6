import logging
import sys
from ftplib import FTP

########################################
# Add includes here for your files
import takeinput                # Take input from user (log and check for blank input)
import connectftp               # Connect to remote server

import loginsecure              # 1. Log into remote server


########################################

# References:
# FTPlib documentation: https://docs.python.org/3/library/ftplib.html
# Logging documentation: https://docs.python.org/3/library/logging.html
#                        https://docs.python.org/3/howto/logging.html
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python

# Handle print messages for invalid input
def invalidMenuInput(opt):
    # opt[0] will be false if user entry was blank
    if opt[0] == False:
        # Print error message
        print(opt[1])
    # otherwise, user input was not one of the given options
    else:
        errorMsg = "Error! " + opt[1] + " is not a valid entry. Please try again..."
        print(errorMsg)
        logging.error(errorMsg)


# Login menu that appears after you've logged into the ftp client
#   welcomeMessage: welcomeMessage from ftp server
#   ftp: object for ftp connection
def postLoginMenu(ftp, welcomeMessage):
    logout = False          # 
    opt = (True, "")        # User input tuple

    # Create a menu prompt string
    prompt = welcomeMessage + """
=========================

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

    # Repeat menu options until logout = True
    while (logout != True):
        # Note:
        # takeInput will automatically log input
        # takeInput will automatically log blank user input errors
        # opt is a tuple: (bool, string)
        # If user input was not empty it will contain: (True, userInputString)
        # If user input was empty it will contain: (False, errorMsg)
        opt = takeinput.takeInput(prompt)
        
        ####### Note: log all input using takeinput.takeInput(prompt) function
        #1.  Log off
        if opt[1] == "1":
            print("Logging out...")
            print()
            # Call logout function here
            logout = True
        # 2.  List directories & files on remote server
        elif opt[1] == "2":
            print("You chose " + opt[1])
        # 3.  Get file from remote server
        elif opt[1] == "3":
            pint("You chose " + opt[1])
        # 4.  Log off from remote server
        elif opt[1] == "4":
            print("You chose " + opt[1])
        # 5.  Get multiple
        elif opt[1] == "5":
            print("You chose " + opt[1])
        # 6.  List directories & files on  local machine
        elif opt[1] == "6":
            print("You chose " + opt[1])
        # 7.  Put file onto remote server
        elif opt[1] == "7":
            print("You chose " + opt[1])
        # 8.  Put multiple
        elif opt[1] == "8":
            print("You chose " + opt[1])
        # 9.  Create directory on remote server
        elif opt[1] == "9":
            print("You chose " + opt[1])
        # 10. Delete file from remote server
        elif opt[1] == "10":
            print("You chose " + opt[1])
        # 11. Change permissions on remote server
        elif opt[1] == "11":
            print("You chose " + opt[1])
        # 12. Copy directories on remote server
        elif opt[1] == "12":
            print("You chose " + opt[1])
        # 13. Delete directories on remote server
        elif opt[1] == "13":
            print("You chose " + opt[1])
        # 14. Save connection information
        elif opt[1] == "14":
            print("You chose " + opt[1])
        # 15. Use saved connection information to connect
        elif opt[1] == "15":
            print("You chose " + opt[1])
        # 16. Rename file on remote server
        elif opt[1] == "16":
            print("You chose " + opt[1])
        # 17. Timeout after idle time
        elif opt[1] == "17":
            print("You chose " + opt[1])
        # 18. Log history
        elif opt[1] == "18":
            print("You chose " + opt[1])
        # Otherwise input will be in error
        else:
            invalidMenuInput(opt[1])


# Menu for connected but not logged in
def connectedAnonMenu(ftp, ftpAddr):
    # Option input tuple
    opt = (True, "")

    while (opt[1].lower() != "q"):
        # display menu
        prompt = "Annonymously connected to: " + ftpAddr + """
==========================

1.  Login
Q.  Disconnect

Enter your choice: 
        """
        # Menu formatting (removes newline from the end, then adds a space)
        prompt = prompt.rstrip()
        prompt += " "

        # Take input from user and log it
        opt = takeinput.takeInput(prompt)
        print()

        # 1.  Login to server
        if opt[1] == "1":
            # Gather username somehow (through entry or saved connection, etc)
            usr = 'testacct@ftptest.portlandredbird.com'

            # Login to FTP server you are connected to
            serverResponse = loginsecure.loginSecure(ftp, usr)
            # If login was successful, proceed to logged in commands
            if serverResponse[0] == True:
                postLoginMenu(ftp, serverResponse[1])
            else:
                print(serverResponse[0]) 
        elif (opt[1].lower() == "q"):
            print("Going back...")
            print()
        else:
            invalidMenuInput(opt)




if __name__ == "__main__":
    # Sets up logging. 
    # Uses filemode 'a' so it appends to the existing log instead of overwriting
    # Logging level: anything below the set logging level will be ignored. So it's a logging threshold
    logging.basicConfig(filename='input-and-errors.log', filemode='a', level=logging.DEBUG)

    # Option input tuple
    opt = (True, "")

    while (opt[1].lower() != "q"):
        # display menu
        prompt = """
FTP Client TUI
==============

1.  Connect to server
Q.  Quit

Enter your choice: 
        """

        # Some menu formatting (removes newline from the end, then adds a space)
        prompt = prompt.rstrip()
        prompt += " "

        # Take input from user and log it
        opt = takeinput.takeInput(prompt)
        print()
        
        
        # Proccess user input
        # 1.  Connect to FTP server
        if opt[1] == "1":
            ftpAddr = 'ftptest.portlandredbird.com'
            badAddr = 'afdsfsfafsa'
            
            # Attempt to connect to the server
            serverResponse = connectftp.connectFTP(ftpAddr)

            # If conneciton succeeded allow user to login
            if serverResponse[0] == True:
                connectedAnonMenu(serverResponse[1], ftpAddr)
            # If connection failed display error
            else:
                print("Error! Could not connect to '" + ftpAddr + "'")
                print("Response: " + str(serverResponse[1]))
        # Q.  Quit
        elif (opt[1].lower() == "q"):
            print("Quitting...")
            print()
        else:
            invalidMenuInput(opt)
        
    sys.exit(0)