# Purpose: Centralize logging for user input
#   Takes user input:
#       Check for blank user entry
#       Logs blank user entry errors
#   Logs all user input

import logging

# Returns tuple: (bool, message)
# If user input is not empty, the message will be the user input: (True, [user input string])
# If user input is empty, the message will contain an error message that was logged: (False, "Error! Entry cannot be blank")
# Does not check for anything besides empty input (No other validity tests)
def takeInput(prompt):
    userInput = input(prompt)
    logging.info(userInput)

    ret = (True, userInput)

    if userInput == "":
        ret = (False, "Error! Entry cannot be blank")
        logging.error(ret)

    return ret