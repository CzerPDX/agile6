import logging
from ftplib import FTP


def renameFile(ftp):
	
	fromName = input('Which file do you want to rename?\n')
	toName = input('What would you like to rename it to?\n')
	try:
		capture = ftp.rename(fromName, toName)
		ret = (True, (capture))
		logging.info("Files Renamed")

	except Exception as err:
		ret = (False, err)
		logging.error(err)

	return ret



