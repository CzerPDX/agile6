from fileinput import filename
import logging
import sys
import os
from ftplib import FTP

########################################
# Add includes here for your files
import takeinput                # Take input from user (log and check for blank input)
import connectftp               # Connect to remote server
import loginsecure              # Log into remote server
import listremotedir
import listlocaldir
import putfile
import put_multi
import changepermissions
import deletefile
import listlocaldir
import listremotedir 
import getfiles                 #
import saveconnection           # Save a new connection information
import renamefile
import createremotedir

import removeremotedir

import logoff
import saveconnection           # Save a new connection information

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

    # Repeat menu options until logout = True
    while (logout != True):
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
13. -------- REMOVED FROM THIS LEVEL -------
14. -------- REMOVED FROM THIS LEVEL -------
15. Rename file on remote server
16. Timeout after idle time
17. Log history

Q.  Log off

Enter your choice: 
    """

        # Some menu formatting (removes newline from the end, then adds a space)
        prompt = prompt.rstrip()
        prompt += " "

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
            print(list[1])
        # 2.  Get file from remote server
        elif opt[1] == "2":
            print("You chose " + opt[1])
            print("Files available to download:\n")
            list = getfiles.list_files(ftp, False)
            for l in list:
                print(str(list.index((l[0], l[1])) + 1) + " " + l[0])
            user_input = ""
            while user_input != "/":
                print("Please enter the number of the file to download or the slash character / to abort:")
                user_input = input()
                if user_input == "/":
                    break
                try:
                    val = int(user_input)
                    if val < 1 or len(list) < val:
                        print("Number given is out of range.")
                        continue
                    print(list[val - 1][0])
                    getfiles.get_single(ftp, list[val - 1][0] , list[val - 1][1])
                    break
                except ValueError:
                    print("Input was not a valid number.")
        # 3.  Log off from remote server
        elif opt[1] == "3":
            print("You chose " + opt[1])
            logout_resp = logoff.logoff(ftp)
            if(logout_resp[0] == True):
                print("\n" + logout_resp[1])
            else:
                print("Logout Failed")

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
            path = input(r"Please enter the path of the file you wish to upload(eg:C:\Users\jake\Desktop\uploads ): ")
            filename = input("please type in file name you wish to upload with extention: ");
            upload_path = input("Please enter the diretory path you want to upload the file to eg: /uploads : ")
            putfile.put_file(ftp, path, filename, upload_path)
        # 7.  Put multiple
        elif opt[1] == "7":
            print("You chose " + opt[1])
            add_more = True
            while add_more == True:
                path = input(r"Please enter the path of the file you wish to upload(eg:C:\Users\jake\Desktop\uploads ): ")
                filename = input("please type in file name you wish to upload with extention: ");
                upload_path = input("Please enter the diretory path you want to upload the file to eg: /uploads : ")
                put_multi.put_multi_file(ftp, path, filename, upload_path)
                ans = input("Do you wish to upload another file? yes/no : ")

                if(ans == 'no'):
                    add_more = False;

        # 8.  Create directory on remote server
        elif opt[1] == "8":
            print("You chose " + opt[1])
            createremotedir.createDir(ftp)
        # 9. Delete file from remote server
        elif opt[1] == "9":
            print("You chose " + opt[1])
            fileName = input("Please enter file or directory to delete: ")
            ftpResponse = deletefile.deleteFile(ftp, fileName)
            print(ftpResponse)
        # 10. Change permissions on remote server
        elif opt[1] == "10":
            print("You chose " + opt[1])
            chmodKey = input("Please enter 3 digit chmod key: ")
            fileName = input("Please enter file or directory name to change permissions: ")
            ftpResponse = changepermissions.changePermissions(ftp, chmodKey, fileName)
            print(ftpResponse)
        # 11. Copy directories on remote server
        elif opt[1] == "11":
            print("You chose " + opt[1])
        # 12. Delete directories on remote server
        elif opt[1] == "12":
            print("You chose " + opt[1])
            removeremotedir.removeDir(ftp)
        # 13. Save connection information
        elif opt[1] == "13":
            print("MOVED TO UPPER LEVEL OF UI")
        # 14. Use saved connection information to connect
        elif opt[1] == "14":
            print("MOVED TO UPPER LEVEL OF UI")
        # 15. Rename file on remote server
        elif opt[1] == "15":
            print("You chose " + opt[1])
            renamefile.renameFile(ftp)
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
            # usr = os.environ['FTPUSR']
            # Get username
            prompt = "Enter your username: ".rstrip('\n')
            inputBuf = (False, "")
            while (inputBuf[0] == False):
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    usr = inputBuf[1]

            # Login to FTP server you are connected to
            serverResponse = loginsecure.loginSecure(ftp, usr)
            # If login was successful, proceed to logged in commands
            if serverResponse[0] == True:
                postLoginMenu(ftp, serverResponse[1])
                # quit after successful login menu return. There doesn't seem
                # to be a different function call for "logout" vs "disconnect", so
                # once they log in successfully they must then fully disconnect from
                # the server with a ftp.quit()
                ftp.quit()
                break
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

1.  Manually connect to server
2.  Save new connection information
3.  Use saved connection information to connect
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
            # ftpAddr = os.environ['FTPADDR']
            # Get ftp address
            inputBuf = (False, "")
            prompt = "Enter the FTP address: ".rstrip('\n')
            while (inputBuf[0] == False):
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    ftpAddr = inputBuf[1]
            
            # Attempt to connect to the server
            serverResponse = connectftp.connectFTP(ftpAddr)

            # If conneciton succeeded allow user to login
            if serverResponse[0] == True:
                connectedAnonMenu(serverResponse[1], ftpAddr)
            # If connection failed display error
            else:
                print("Error! Could not connect to '" + ftpAddr + "'")
                print("Response: " + str(serverResponse[1]))
        elif opt[1] == "2":
            # Input is being taken in the UI because the function itself
            # will take the connection information as arguments.
            prompt = "Saving new FTP connection"
            logging.info(prompt)

            # Display UI
            print(prompt)
            print("=======================")
            print()
            inputBuf = (False, "")
            label = ""
            ftpAddr = ""
            username = ""

            # Get label for ftp
            prompt = "Enter a label or name for your FTP connection: ".rstrip('\n')
            while (inputBuf[0] == False):
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    label = inputBuf[1]
            # Reset user input
            inputBuf = (False, "")

            # Get ftp address
            prompt = "Enter a ftp server address: ".rstrip('\n')
            while (inputBuf[0] == False):
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    ftpAddr = inputBuf[1]
            # Reset user input
            inputBuf = (False, "")

            # Get username
            prompt = "Enter your username: ".rstrip('\n')
            while (inputBuf[0] == False):
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    username = inputBuf[1]

            # Now call the function to add the new connection info to the list
            try:
                resp = saveconnection.saveConnection(label, ftpAddr, username)
                logging.info(resp[1])
                print(resp[1])
            except Exception as err:
                print(err)
                logging.error(err)
        # Use saved connection information to connect
        elif opt[1] == "3":
            inputBuf = (False, "")
            choice = ""
            menuOptions = saveconnection.loadSavedConnections()
            print("Which saved connection to connect with?")
            print("=======================================")
            print()
            number = 0
            for line in menuOptions:
                number = number + 1
                print("{}. ".format(number), end="")
                print(line[0])
            print("Q. Go back to main menu")
            print()
            prompt = "Enter the number of the connection you want to use: ".rstrip('\n')
            
            while inputBuf[0] == False:
                inputBuf = takeinput.takeInput(prompt)
                if (inputBuf[0] == False):
                    print(inputBuf[1])
                else:
                    choice = inputBuf[1]
            
            print()
            if inputBuf[1].isdigit() and (int(choice) > 0) and (int(choice) <= len(menuOptions)):
                # Attempt to connect to the server
                index = int(inputBuf[1]) - 1
                ftpAddr = menuOptions[index][1]
                usr = menuOptions[index][2]
                serverResponse = connectftp.connectFTP(ftpAddr)
                print()
                print("Attempting to connect with ftp address: " + ftpAddr + " and username: " + usr)
                print()

                # If conneciton succeeded allow user to login
                if serverResponse[0] == True:
                    # Login to FTP server you are connected to
                    ftp = serverResponse[1]
                    serverResponse = loginsecure.loginSecure(ftp, usr)
                    # If login was successful, proceed to logged in commands
                    if serverResponse[0] == True:
                        postLoginMenu(ftp, serverResponse[1])
                        # quit after successful login menu return. There doesn't seem
                        # to be a different function call for "logout" vs "disconnect", so
                        # once they log in successfully they must then fully disconnect from
                        # the server with a ftp.quit()
                        ftp.quit()
                    # If login was unsuccessful, display error message
                    else:
                        print("Error! Failed to log into server")
                        print("Response: " + str(serverResponse[1])) 
                        print()
                        # If connection failed display error
                else:
                    print("Error! Could not connect to '" + ftpAddr + "'")
                    print("Response: " + str(serverResponse[1]))
            elif (choice.lower() == "q"):
                print("Quitting...")
                print()
            else:
                invalidMenuInput(inputBuf)

            

        # Q.  Quit
        elif (opt[1].lower() == "q"):
            print("Quitting...")
            print()
        else:
            invalidMenuInput(opt)
        
    sys.exit(0)