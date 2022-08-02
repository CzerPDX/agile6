# Jonas Persson
# CS410 Agile Summer 2022 Portland State
import logging
from datetime import datetime

def open_file(filename):
    try:
        f = open(filename, "r")                 
    except Exception as err:
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: LOG HISTORY OPEN FILE: " + str(err))
        return None
    return f

def close_file(f):
    try: 
        f.close()
    except Exception as err:
        now = datetime.now()
        logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: LOG HISTORY CLOSE FILE: " + str(err))
        return False
    return True

def process_log_file(filename):
    log_string = ""
    f = open_file(filename)
    if f is None:
        return None
    if f is not None:
        try:
            with f:
                for line in f:
                    if line[0] == 'E':
                        log_string += line[11:]
                    if line[0] == 'I':
                        log_string += line[10:]
        except Exception as err:
            now = datetime.now()
            logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: GENERATE LOG HISTORY STRING: " + str(err))
    else:
        return None
    close_file(f)
    return log_string
