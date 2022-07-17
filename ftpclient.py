import logging
import sys
import os
from ftplib import FTP

########################################
# Add includes here for your files
import takeinput                # Take input from user (log and check for blank input)
import connectftp               # Connect to remote server
import loginsecure              # Log into remote server
import listremotedir            # 
import listlocaldir             #
import getfiles                 # Module for downloading a single and multiple files

# References:
# FTPlib documentation: https://docs.python.org/3/library/ftplib.html
# Logging documentation: https://docs.python.org/3/library/logging.html
#                        https://docs.python.org/3/howto/logging.html
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python
# checking types within a tuples

# Handle print messages for invalid input
def invalidMenuInput(opt):

    # opt[0] will be false if user entry was blank
    # opt[1] will contain an error message about blank entry in this case
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

1.  List directories & files on remote server
2.  Get file from remote server
3.  Log off from remote server
4.  Get multiple
5.  List directories & files on local machine
6.  Put file onto remote server
7.  Put multiple
8.  Create directory on remote server
9. Delete file from remote server
10. Change permissions on remote server
11. Copy directories on remote server
12. Delete directories on remote server
13. Save connection information
14. Use saved connection information to connect
15. Rename file on remote server
16. Timeout after idle time
17. Log history

Q.  Log off

Enter your choice: 
    """
    # Some menu formatting (removes newline from the end, then adds a space)
    prompt = prompt.rstrip()
    prompt += " "
    files_to_get = []

    # Repeat menu options until logout = True
    while (logout != True):
        # Note:
        # takeInput will automatically log input
        # takeInput will automatically log blank user input errors
        # opt is a tuple: (bool, string)
        # If user input was not empty it will contain: (True, userInputString)
        # If user input was empty it will contain: (False, errorMsg)
        opt = takeinput.takeInput(prompt)
        

        ####################################################
        # Add your function calls below
        
        # 1.  List directories & files on remote server
        if opt[1] == "1":
            print("You chose " + opt[1])
            list = listremotedir.listRemote(ftp)
            print(list[0])
            print(list[1])
            listremotedir.listRemote(ftp)
        # 2.  Get file from remote server
        elif opt[1] == "2":
            print("You chose " + opt[1])
            try:
                getfiles.get_single(ftp, files_to_get)
            except:
                pass
            files_to_get = []
        # 3.  Log off from remote server
        elif opt[1] == "3":
            print("You chose " + opt[1])
        # 4.  Get multiple
        elif opt[1] == "4":
            print("You chose " + opt[1])
        # 5.  List directories & files on  local machine
        elif opt[1] == "5":
            print("You chose " + opt[1])
            listlocaldir.listLocal()
        # 6.  Put file onto remote server
        elif opt[1] == "6":
            print("You chose " + opt[1])
        # 7.  Put multiple
        elif opt[1] == "7":
            print("You chose " + opt[1])
        # 8.  Create directory on remote server
        elif opt[1] == "8":
            print("You chose " + opt[1])
        # 9. Delete file from remote server
        elif opt[1] == "9":
            print("You chose " + opt[1])
        # 10. Change permissions on remote server
        elif opt[1] == "10":
            print("You chose " + opt[1])
        # 11. Copy directories on remote server
        elif opt[1] == "11":
            print("You chose " + opt[1])
        # 12. Delete directories on remote server
        elif opt[1] == "12":
            print("You chose " + opt[1])
        # 13. Save connection information
        elif opt[1] == "13":
            print("You chose " + opt[1])
        # 14. Use saved connection information to connect
        elif opt[1] == "14":
            print("You chose " + opt[1])
        # 15. Rename file on remote server
        elif opt[1] == "15":
            print("You chose " + opt[1])
        # 16. Timeout after idle time
        elif opt[1] == "16":
            print("You chose " + opt[1])
        # 17. Log history
        elif opt[1] == "17":
            print("You chose " + opt[1])
        #Q.  Log off
        elif opt[1].lower() == "q":
            print("Logging out...")
            print()
            # Call logout function here
            logout = True
        # Otherwise input will be in error
        else:
            invalidMenuInput(opt)



# Menu for anonymous connection (connected but not logged in)
def connectedAnonMenu(ftp, ftpAddr):
    # Option input tuple
    opt = (True, "")

    while (opt[1].lower() != "q"):
        # display menu
        prompt = ("Annonymously connected to: " + ftpAddr)
        print (prompt)
        for character in prompt:
            print ("=", end ="")

        prompt = """
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

        # Attempt to login to server
        if opt[1] == "1":
            # Gather username somehow (through entry or saved connection, etc)
            usr = 'testacct@ftptest.portlandredbird.com'

            # Login to FTP server you are connected to
            serverResponse = loginsecure.loginSecure(ftp, usr)
            # If login was successful, proceed to logged in commands
            if serverResponse[0] == True:
                postLoginMenu(ftp, serverResponse[1])
            # If login was unsuccessful, display error message
            else:
                print("Error! Failed to log into server")
                print("Response: " + str(serverResponse[1])) 
                print()
        elif (opt[1].lower() == "q"):
            print("Disconnecting...")
            print()
        else:
            invalidMenuInput(opt)


# Main
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
FTP Client (not connected)
==========================

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
            ftpAddr = os.environ['FTPADDR']
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