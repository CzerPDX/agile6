# Purpose: Centralize logging for user input
#   Takes user input:
#       Check for blank user entry
#       Logs blank user entry errors
#   Logs all user input

import logging

# Returns tuple: (bool, str)
# If user input is not empty, the str will be the user input: (True, [user input string])
# If user input is empty, the str will contain an error message that was logged: (False, "Error! Entry cannot be blank")
# Does not check for anything besides empty input (No other validity tests)
def takeInput(prompt):
    # Preconditions
    # prompt must be a str
    # prompt must not be empty
    assert isinstance(prompt, str), "expected type(prompt) == str. got type: {}".format(type(prompt))
    assert len(prompt) > 0, "expected non-empty prompt. got: {}".format(prompt)

    userInput = input(prompt)
    print()
    logging.info(userInput)

    ret = (True, userInput)

    if userInput == "":
        ret = (False, "Error! Entry cannot be blank")
        logging.error(ret[1])

    # Postconditions
    # ret must be a tuple of size 2
    # ret[0] must be a bool
    # ret[1] must be a str
    assert isinstance(ret, tuple), "expected type(ret) == tuple. got type: {}".format(ret)
    assert len(ret) == 2, "expected tuple of size 2. got tuple of size: {}".format(len(ret))
    assert isinstance(ret[0], bool), "expected type(ret[0] == bool. got type: {}".format(ret[0])
    assert isinstance(ret[1], str), "expected type(ret[1] == str. got type: {}".format(type(ret[1]))
    
    return ret