# Purpose:
#   Logs all user input by default
#   Check for empty input

import logging

# Returns tuple: (bool, message)
# If user input is not empty message will be blank: (True, "")
# If user input is empty, message will contain error info: (False, "Entry cannot be blank")
#   Error is also logged
# Does not check for anything besides empty input
def takeInput():
    user = input()
    logging.info(resp)