import logging
from ftplib import FTP
from datetime import datetime

def renameFile(ftp):
	
	fromName = input('Which file do you want to rename?\n')
	toName = input('What would you like to rename it to?\n')
	try:
		capture = ftp.rename(fromName, toName)
		ret = (True, (capture))
		now = datetime.now()
		logging.info(now.strftime("%m/%d/%Y %H:%M:%S") + " COMMAND: RENAME FILE ON FTP SERVER: Files Renamed.")

	except Exception as err:
		ret = (False, err)
		now = datetime.now()
		logging.error(now.strftime("%m/%d/%Y %H:%M:%S") + " ERROR: RENAME FILE ON FTP SERVER: " + str(err))

	return ret



