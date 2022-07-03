import logging
from ftplib import FTP

# References:
# FTPlib documentation: https://docs.python.org/3/library/ftplib.html
# Logging documentation: https://docs.python.org/3/library/logging.html
#                        https://docs.python.org/3/howto/logging.html
# how to make strings span multiple lines: https://www.tutorialspoint.com/triple-quotes-in-python

def loginSecure(ftpAddr, usr):
    # Connect to ftp server
    ftp = FTP(ftpAddr)

    # log ftpAddr and username to log
    logging.info("Attempted login: " + ftpAddr + ", " + usr)

    # log into ftp server and return the login response from the server
    try:
        resp = ftp.login(user=usr, passwd=input("enter pw: "))
        logging.info(resp)
    # if an error occurs, return the error
    except Exception as err:
        resp = err
        logging.error(err)

    return resp


if __name__ == "__main__":
    # Sets up logging. 
    # Uses filemode 'a' so it appends to the existing log instead of overwriting
    # Logging level: anything below the set logging level will be ignored. So it's a logging threshold
    logging.basicConfig(filename='input-and-errors.log', filemode='a', level=logging.DEBUG)

    # display menu
    prompt = """
    FTP Client TUI
    ==============
    
    1. Log into remote server
    2. List directories & files on remote server
    3. Get file from remote server

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
        # log into ftp and print 
        ftpAddr = 'ftptest.portlandredbird.com'
        usr = 'testacct@ftptest.portlandredbird.com'
        print(loginSecure(ftpAddr, usr))
    elif opt == "2":
        print("you chose 2")
    elif opt == "3":
        print("you chose 3")
    else:
        errorMsg = "Error! " + opt + " is not a valid option. Exiting..."
        print(errorMsg)
        logging.error(errorMsg)