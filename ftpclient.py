from fileinput import filename
import logging
import sys
import os
from ftplib import FTP
from datetime import datetime
from colorama import Fore, Back, Style

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
# Printing colored text: https://stackabuse.com/how-to-print-colored-text-in-python/ 
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python
# checking types within a tuples

def printSuccess(resp):
    print()
    print(Fore.BLACK + Back.GREEN + str(resp) + Style.RESET_ALL)
    print()

def printFailure(resp):
    print()
    print(Fore.BLACK + Back.RED + str(resp) + Style.RESET_ALL)
    print()

def printTitle(title):
    print()
    print(title)
    for c in title:
        print("=", end="")
    print()
    print()

def printNumberedList(list):
    # Print the contents of the remote folder
    bullet = 1
    for item in list:
        print(str(bullet) + ". " + item)
        bullet = bullet + 1
    print()

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
        printFailure(errorMsg)
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
2.  Download file from remote server
3.  Download multiple files from remote server
4.  List directories & files on local machine
5.  Put file onto remote server
6.  Put multiple
7.  Create directory on remote server
8.  Delete file from remote server
9.  Change permissions on remote server
10. Copy directories on remote server
11. Delete directories on remote server
12. Rename file on remote server
13. Log history
14. Rename local file

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
            # Print the title
            title = "List directories & files on remote server"
            printTitle(title)

            # Get the files at the location
            server_response = listremotedir.listRemote(ftp)

            if server_response[0]:
                list = server_response[1]
                # Print a numbered list of files
                printNumberedList(list)
            else:
                print(server_response[1])

        # 2.  Download file from remote server
        elif opt[1] == "2":
            # Print the title
            title = "Download file from remote server"
            printTitle(title)

            # Get the list of files available for the user to download
            server_response = getfiles.list_files(ftp, False)
            if (server_response[0]):
                list = server_response[1]
            else:
                print(server_response[1])

            if (server_response[0]):
                # Print out a numbered list of files
                print("Files available to download:")
                printNumberedList(list)
                print()

                # Get the user's entry for file number
                prompt = "Please enter the number of the file to download or the slash character / to abort: "
                inputBuf = takeinput.takeInput(prompt)

                # Check input assuming a valid (non-empty) response was given
                if inputBuf[0] == True:
                    user_input = inputBuf[1]
                    if user_input != "/":
                        try:
                            val = int(user_input)
                            if val < 1 or len(list) < val:
                                printFailure("Number given is out of range.")
                            else:
                                print("File selected: " + list[val - 1] + "\n")
                                server_response = getfiles.get_single(ftp, list[val - 1])
                                
                                # Print out the response from the server
                                if server_response[0]:
                                    printSuccess(server_response[1])
                                else:
                                    printFailure(server_response[1])

                        except ValueError:
                            printFailure("Input was not a valid number.\n")
                else:
                    printFailure(inputBuf[1])

        # 3.  Get multiple
        elif opt[1] == "3":
            # Print the title
            title = "Download multiple files from the remote server"
            printTitle(title)
            
            # Get the list of files available for the user to download
            server_response = getfiles.list_files(ftp, False)
            if (server_response[0]):
                list = server_response[1]
            else:
                printFailure(server_response[1])

            if (server_response[0]):
                # Print out a numbered list of files
                print("Files available to download:")
                printNumberedList(list)
                print()


                user_input = ""
                files_to_get = []
                bad_input_flag = False

                while user_input != "/":
                    prompt = "Please enter the number of each file to download separated by a space, or enter the slash character / to abort: "
                    inputBuf = takeinput.takeInput(prompt)

                    if inputBuf[0]:
                        user_input = inputBuf[1]
                    else:
                        printFailure(inputBuf[1])
                    
                    if inputBuf[0]:
                        if user_input != "/":
                            # Verify that all user input is valid
                            try:
                                for num in user_input.split(" "):
                                    # Check that it can successfully be turned into an int
                                    val = int(num)
                                    # Validate that each file chosen exists in the list (valid index)
                                    if val < 1 or len(list) < val:
                                        raise Exception("Error! Value " + str(val) + " is out of range.")
                                        bad_input_flag == True
                                    # Add to the list of files_to_get, if it's in range.
                                    else:
                                        files_to_get.append(list[val - 1])
                            except Exception as err:
                                now = datetime.now()
                                errMsg = now.strftime("%m/%d/%Y %H:%M:%S ERROR: ") + str(err)
                                logging.error(errMsg)
                                bad_input_flag = True

                                printFailure(errMsg)

                            # Validate that each file chosen exists in the list
                            if (bad_input_flag == False):
                                print("Files selected for download: ", end='')
                                for file in files_to_get:
                                    print(file + " ", end='')
                                print("\n")
                                server_response = getfiles.get_multiple(ftp, files_to_get)
                                    
                                # Print out the response from the server
                                if server_response[0]:
                                    printSuccess(server_response[1])
                                else:
                                    printFailure(server_response[1])
                                    now = datetime.now()
                                    logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: RETRIEVE MULTIPLE FILES FROM FTP SERVER: FAILED.\nResponse: " + server_response[1])

        # 4.  List directories & files on local machine
        elif opt[1] == "4":
            # Print the titles
            title = "List directories & files on local machine"
            printTitle(title)

            # Get local path
            pathGood = False
            try:
                path = os.getcwd()
                pathGood = True
            except Exception as err:
                printFailure(str(err))

            if pathGood:
                server_response = listlocaldir.listLocal(path)

                if server_response[0] == True:
                    printNumberedList(server_response[1])
                else:
                    printFailure(server_response[1])
        
        # 5.  Put file onto remote server
        elif opt[1] == "5":
            # Print the title
            title = "Put a file onto the remote server"
            printTitle(title)
            
            # Gather info for what files to put where
            fileInfo = putFilesUI()
            server_response = (False, "")

            # Put the files in the places
            if fileInfo[0] == True:
                server_response = putfile.put_file(ftp, fileInfo[1], fileInfo[2], fileInfo[3])
            
            # Display outcome
            if server_response[0]:
                printSuccess(server_response[1])
            else:
                printFailure(server_response[1])
            
        # 6. Put multiple files onto the remote server
        elif opt[1] == "6":
            # Print the title
            title = "Put multiple files onto the remote server"
            printTitle(title)

            # Put more files on sever until the user enters "no"
            add_more = True
            ans = ""
            while add_more == True:
                fileInfo = putFilesUI()
                server_response = (False, "")

                # Call putfile
                if fileInfo[0] == True:
                    server_response = putfile.put_file(ftp, fileInfo[1], fileInfo[2], fileInfo[3])

                if server_response[0]:
                    printSuccess(server_response[1])
                else:
                    printFailure(server_response[1])

                # Ask for "yes" or "no" input until valid response is given
                ans = ""
                while (ans != "no") and (ans != "yes"):
                    prompt = "Do you wish to upload another file? yes/no: "
                    inputBuf = takeinput.takeInput(prompt)

                    if inputBuf[0] == True:
                        ans = inputBuf[1]
                        if(ans.lower() == "no"):
                            add_more = False
                        elif(ans.lower() == "yes"):
                            add_more = True
                        else:
                            errMsg = ans + " is not a valid entry. Please enter 'yes' or 'no'"
                            logging.error(errMsg)
                            printFailure(errMsg)

        # 7.  Create directory on remote server
        elif opt[1] == "7":
            server_response = (False, "")
            # Print the title
            title = "Create directory on remote server"
            printTitle(title)

            # Get the directory name to add
            prompt = "What is the name of the new directory you'd like to add? "
            inputBuf = takeinput.takeInput(prompt)
            
            # If input is valid
            if inputBuf[0] == True:
                server_response = createremotedir.createDir(ftp, inputBuf[1])
                print()
                
                if server_response[0] == True:
                    printSuccess("directory " + server_response[1] + " successfully added.")
                else:
                    printFailures(server_response[1])
            else:
                printFailure(inputBuf[1])
            
        # 8. Delete file from remote server
        elif opt[1] == "8":
            server_response = (False, "")
            # Print the title
            title = "Delete file from remote server"
            printTitle(title)

            # Get local path
            pathGood = False
            try:
                path = os.getcwd()
                pathGood = True
            except Exception as err:
                printFailure(str(err))

            if pathGood:
                # Print the list of files on the server
                server_response = listremotedir.listRemote(ftp)

                if (server_response[0] == True):
                    for item in server_response[1]:
                        print(item)
                    print()
                else:
                    printFailure(server_response[1])

                fileName = takeinput.takeInput("Please enter file or directory to delete: ")
                server_response = deletefile.deleteFile(ftp, fileName[1])
                
                if server_response[0]:
                    printSuccess(server_response[1])
                else:
                    printFailure(server_response[1])

        # 9. Change permissions on remote server
        elif opt[1] == "9":
            # Print the title
            title = "Change permissions on remote server"
            printTitle(title)

            # Print the list of files on the server
            server_response = listremotedir.listRemote(ftp)

            if (server_response[0] == True):
                for item in server_response[1]:
                    print(item)
                print()
            else:
                printFailure(server_response[1])
            
            fileName = takeinput.takeInput("Please enter file or directory name to change permissions: ")
            chmodKey = takeinput.takeInput("Please enter 3 digit chmod key: ")
            server_response = changepermissions.changePermissions(ftp, chmodKey[1], fileName[1])
            
            if server_response[0]:
                printSuccess(server_response[1])
            else:
                printFailure(server_response[1])


        # 10. Copy directories on remote server
        elif opt[1] == "10":
            # Print the title
            title = "Copy directories on remote server"
            printTitle(title)
            pathGood = False

            try:
                path = ftp.pwd()
                pathGood = True
            except Exception as err:
                printFailure(str(err))

            if pathGood:
                toCopy = input("Enter the directory name to copy: ")
                server_response = copyremotedir.copyDir(ftp, toCopy)

                if server_response[0]:
                    printSuccess(server_response[1])
                else:
                    printFailure(server_response[1])
                
            try:
                resp = ftp.cwd(path)
            except Exception as err:
                printFailure(str(err))


        # 11. Delete directories on remote server
        elif opt[1] == "11":
            # Print the title
            title = "Delete directories on remote server"
            printTitle(title)

            prompt = "What is the name of the directory you'd like to remove? "
            # Take input from user and log it
            inputBuf = takeinput.takeInput(prompt)
            
            if inputBuf[0] == True:
                server_response = removeremotedir.removeDir(ftp, inputBuf[1])
                
            if server_response[0]:
                printSuccess(server_response[1])
            else:
                printFailure(server_response[1])

        # 12. Rename file on remote server
        elif opt[1] == "12":
            # Print the title
            title = "Rename file on remote server"
            printTitle(title)

            # Print the list of files on the server
            server_response = listremotedir.listRemote(ftp)

            if (server_response[0] == True):
                for item in server_response[1]:
                    print(item)
                print()
            else:
                printFailure(server_response[1])

            fileToRename = takeinput.takeInput('Which file do you want to rename?\n')
            newName = takeinput.takeInput('What would you like to rename it to?\n')
            server_response = renamefile.renameFile(ftp, fileToRename[1], newName[1])

            if server_response[0]:
                printSuccess(server_response[1])
            else:
                printFailure(server_response[1])

        # 13. Log history
        elif opt[1] == "13":
            # Print the title
            title = "Display the log history"
            printTitle(title)
            
            log_string = logtostring.process_log_file("input-and-errors.log")
            if log_string is not None:
                print("\n======== LOG HISTORY ========\n" + log_string + "=======================\n")
                now = datetime.now()
                logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: PRINT LOG HISTORY: Successfully printed.")
            else:
                now = datetime.now()
                logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: PRINT LOG HISTORY: Log history string could not be generated.")

        # 14. Rename local file
        elif opt[1] == "14":
            server_response = (False, "")
            old = ""
            new = ""

            # Print the title
            title = "Rename local file"
            printTitle(title)

            # Get local path
            pathGood = False
            try:
                path = os.getcwd()
                pathGood = True
            except Exception as err:
                printFailure(str(err))

            if pathGood:
                server_response = listlocaldir.listLocal(path)

                if server_response[0] == True:
                    printNumberedList(server_response[1])
                else:
                    printFailure(server_response[1])

                # Get old path/file name
                prompt = "Please enter relative path to local file you want to rename: "
                inputBuf = takeinput.takeInput(prompt)
                if inputBuf[0] == True:
                    old = inputBuf[1]
                else:
                    printFailure(inputBuf[1])

                # Get new path/file name
                if inputBuf[0] == True:
                    prompt = "Please enter the relative path of the new name of the file: "
                    inputBuf = takeinput.takeInput(prompt)
                    if inputBuf[0] == True:
                        new = inputBuf[1]
                    else:
                        printFailure(inputBuf[1])
                
                # Feed old and new file names into renamelocal
                if inputBuf[0] == True:
                    server_response = renamelocal.renameLocal(old, new)

                    # Print out the result
                    if server_response[0]:
                        printSuccess(server_response[1])
                    else:
                        printFailure(server_response[1]) 
            else:
                printFailure(server_response[1])

        #Q.  Log off
        elif opt[1].lower() == "q":
            print("Logging out...")
            print()
            logout = True #NOTE: Logout occurrs one level up
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
                printFailure("Error! Failed to log into server.\nResponse: " + str(serverResponse[1]))
                printFailure()
        elif (opt[1].lower() == "q"):
            printSuccess("Disconnecting...")
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
                printSuccess(resp[1])
            except Exception as err:
                printFailure(err)
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
                        logout_resp = logoff.logoff(ftp)
                        if logout_resp[0] == True:
                            printSuccess(logout_resp[1])
                        else:
                            printFailed("Logout failed. Server response: " + logout_resp[1])

                    # If login was unsuccessful, display error message
                    else:
                        # If connection failed display error
                        printFailure("Error! Failed to log into server\n" + "Response: " + str(serverResponse[1]))
                else:
                    printFailure("Error! Could not connect to '" + ftpAddr + "'\n" + "Response: " + str(serverResponse[1]))
            elif (choice.lower() == "q"):
                printSuccess("Returning to main menu...")
            else:
                invalidMenuInput(inputBuf)

            

        # Q.  Quit
        elif (opt[1].lower() == "q"):
            printSuccess("Quitting...")
        else:
            invalidMenuInput(opt)
        
    sys.exit(0)