from fileinput import filename
import logging
import sys
import os
from ftplib import FTP
from datetime import datetime

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
import getfiles                 # Functionality for downloading a single and multiple files
import saveconnection           # Save a new connection information
import renamelocal

import renamefile
import createremotedir

import removeremotedir

import copyremotedir


import logoff
import saveconnection           # Save a new connection information
import logtostring              # Functions for reading the input-and-errors log to a string

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
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: MENU SELECTION: " + errorMsg)


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
9.  Delete file from remote server
10. Change permissions on remote server
11. Copy directories on remote server
12. Delete directories on remote server
13. -------- REMOVED FROM THIS LEVEL -------
14. -------- REMOVED FROM THIS LEVEL -------
15. Rename file on remote server
16. Timeout after idle time
17. Log history
18. Rename local file

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
            print("Files available to download:")
            list = getfiles.list_files(ftp, False)
            for l in list:
                print(str(list.index((l[0], l[1])) + 1) + " " + l[0])
            user_input = ""
            while user_input != "/":
                print("Please enter the number of the file to download or the slash character / to abort:", end =" ")
                user_input = input()
                if user_input == "/":
                    break
                try:
                    val = int(user_input)
                    if val < 1 or len(list) < val:
                        print("Number given is out of range.")
                        continue
                    print("File selected: " + list[val - 1][0] + "\n")
                    if getfiles.get_single(ftp, list[val - 1][0] , list[val - 1][1]):
                        now = datetime.now()
                        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: RETRIEVE FILE FROM FTP SERVER: File retrieved successfully.")
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
            print("Files available to download:")
            list = getfiles.list_files(ftp, False)
            for l in list:
                print(str(list.index((l[0], l[1])) + 1) + " " + l[0])
            user_input = ""
            files_to_get = []
            bad_input_flag = False
            while user_input != "/":
                print("Please enter the number of each file to download separated by a space, or enter the slash character / to abort:")
                user_input = input()
                if user_input == "/":
                    break
                try:
                    # Validate that each file chosen exists in the list
                    for num in user_input.split(" "):
                        val = int(num)
                        if val < 1 or len(list) < val:
                            bad_input_flag = True
                            print("At least one number given is out of range.")
                            break
                        files_to_get.append(list[val - 1])
                    if bad_input_flag:
                        bad_input_flag = False
                        continue
                    print("Files selected for download: ", end='')
                    for file in files_to_get:
                        print(file[0] + " ", end='')
                    print("\n")
                    if getfiles.get_multiple(ftp, files_to_get):
                        now = datetime.now()
                        logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: RETRIEVE MULTIPLE FILES FROM FTP SERVER: Files retrieved successfully.")
                    break
                except ValueError:
                    print("Input was not a valid number.")
        # 5.  List directories & files on  local machine
        elif opt[1] == "5":
            print("You chose " + opt[1])
            listlocaldir.listLocal()
        # 6.  Put file onto remote server
        elif opt[1] == "6":
            print("Put a file onto the remote server")
            print()
            fileInfo = putFilesUI()
            resp = (False, "")

            if fileInfo[0] == True:
                resp = putfile.put_file(ftp, fileInfo[1], fileInfo[2], fileInfo[3])
            
                
        # 7.  Put multiple
        elif opt[1] == "7":
            print("Put multiple files onto the remote server")
            print()
            add_more = True
            ans = ""
            while add_more == True:
                fileInfo = putFilesUI()
                resp = (False, "")


                if fileInfo[0] == True:
                    resp = putfile.put_file(ftp, fileInfo[1], fileInfo[2], fileInfo[3])

                print(resp[1])

                while (ans != "no") and (ans != "yes"):
                    prompt = "Do you wish to upload another file? yes/no: "
                    inputBuf = takeinput.takeInput(prompt)

                    if inputBuf[0] == True:
                        ans = inputBuf[1]
                        if(ans == 'no'):
                            add_more = False
                        if(ans == 'yes'):
                            add_more = True
                        else:
                            errMsg = ans[1] + " is not a valid entry. Please enter 'yes' or 'no'"
                            logging.error(errMsg)
                    else:
                        print(inputBuf[1])

        # 8.  Create directory on remote server
        elif opt[1] == "8":
            prompt = "What is the name of the new directory you'd like to add?"
            # Take input from user and log it
            inputBuf = takeinput.takeInput(prompt)
            
            if inputBuf[0] == True:
                server_response = createremotedir.createDir(ftp, inputBuf[1])
            print(server_response)
            
        # 9. Delete file from remote server
        elif opt[1] == "9":
            print("You chose " + opt[1])
            fileName = takeinput.takeInput("Please enter file or directory to delete: ")
            ftpResponse = deletefile.deleteFile(ftp, fileName[1])
            print(ftpResponse)
        # 10. Change permissions on remote server
        elif opt[1] == "10":
            print("You chose " + opt[1])
            chmodKey = takeinput.takeInput("Please enter 3 digit chmod key: ")
            fileName = takeinput.takeInput("Please enter file or directory name to change permissions: ")
            ftpResponse = changepermissions.changePermissions(ftp, chmodKey[1], fileName[1])
            print(ftpResponse)
        # 11. Copy directories on remote server
        elif opt[1] == "11":
            print("You chose " + opt[1])
            copyremotedir.copyDir(ftp)
        # 12. Delete directories on remote server
        elif opt[1] == "12":
            prompt = "What is the name of the directory you'd like to remove?"
            # Take input from user and log it
            inputBuf = takeinput.takeInput(prompt)
            
            if inputBuf[0] == True:
                removeremotedir.removeDir(ftp, inputBuf[1])
            print(inputBuf)
        # 13. Save connection information
        elif opt[1] == "13":
            print("MOVED TO UPPER LEVEL OF UI")
        # 14. Use saved connection information to connect
        elif opt[1] == "14":
            print("MOVED TO UPPER LEVEL OF UI")
        # 15. Rename file on remote server
        elif opt[1] == "15":
            print("You chose " + opt[1])
            fileToRename = takeinput.takeInput('Which file do you want to rename?\n')
            newName = takeinput.takeInput('What would you like to rename it to?\n')
            response = renamefile.renameFile(ftp, fileToRename[1], newName[1])
        # 16. Timeout after idle time
        elif opt[1] == "16":
            print("You chose " + opt[1])

        # 17. Log history
        elif opt[1] == "17":
            print("You chose " + opt[1])
            log_string = logtostring.process_log_file("input-and-errors.log")
            if log_string is not None:
                print("\n======== LOG HISTORY ========\n" + log_string + "=======================\n")
                now = datetime.now()
                logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: PRINT LOG HISTORY: Successfully printed.")
            else:
                now = datetime.now()
                logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: PRINT LOG HISTORY: Log history string could not be generated.")

        # 18. Rename local file
        elif opt[1] == "18":
            print("You chose " + opt[1])
            old = takeinput.takeInput("Please enter relative path to local file you want to rename: ")
            new = takeinput.takeInput("Please enter the relative path of the new name of the file: ")
            ftpResponse = renamelocal.renameLocal(old[1], new[1])
            if(ftpResponse == True):
                print("\nLocal file successfully renamed")
            else:
                print("\nError renaming file")


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

def putFilesUI():
    # Get file path
    prompt = "Enter the filepath of the file to upload: "
    #inputBuf = takeinput.takeInput(prompt)
    ret = (False, "", "", "")
    path = ""
    filename = ""
    uploadPath = ""

    inputBuf = takeinput.takeInput(prompt)

    # Check for errors in input
    if inputBuf[0] == True:
        path = inputBuf[1]

        # Get filename
        prompt = "Please type in file name you wish to upload with extention: "
        inputBuf = takeinput.takeInput(prompt)

        # Check for errors in input
        if inputBuf[0] == True:
            filename = inputBuf[1]

            # Get directory path
            prompt = "Please enter the diretory path you want to upload the file to eg: /uploads : "
            inputBuf = takeinput.takeInput(prompt)

            # Check for errors in input
            if inputBuf[0] == True:
                uploadPath = inputBuf[1]

                # return tuple
                if inputBuf[0] == True:
                    ret = (True, path, filename, uploadPath)
                else:
                    print(resp[1])
            else:
                print(inputBuf[1])
        else:
            print(inputBuf[1])
    else:
        print(inputBuf[1])

    return ret


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
            now = datetime.now()
            logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: ADD NEW SAVED FTP SERVER: " + prompt)

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
                now = datetime.now()
                logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: ADD NEW CONNECTION: " + resp[1])
                print(resp[1])
            except Exception as err:
                print(err)
                now = datetime.now()
                logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: ADD NEW CONNECTION: " + str(err))
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