import logging

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
        print("you chose 1")
    elif opt == "2":
        print("you chose 2")
    elif opt == "3":
        print("you chose 3")
    else:
        errorMsg = "Error! " + opt + " is not a valid option. Exiting..."
        print(errorMsg)
        logging.error(errorMsg)