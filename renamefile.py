import logging
from ftplib import FTP
from datetime import datetime

def renameFile(ftp, fromName, toName):
	
	try:
		capture = ftp.rename(fromName, toName)
		ret = (True, (capture))

		logging.info("Files Renamed")

	except Exception as err:
		ret = (False, err)
		logging.error(err)

		now = datetime.now()
		logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: RENAME FILE ON FTP SERVER: Files Renamed.")

	except Exception as err:
		ret = (False, err)
		now = datetime.now()
		logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RENAME FILE ON FTP SERVER: " + str(err))

	return ret

