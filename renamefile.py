import logging
from ftplib import FTP


def renameFile(ftp):
	
	fromName = input('Which file do you want to rename?\n')
	# Check if the file exists on the remote server.
	fileExist = findName(fromName, ftp)
	toName = input('What would you like to rename it to?\n')
	# Check if the name is duplicate
	isDuplicate = findName(toName, ftp)

	if(fileExist and not isDuplicate):
		ftp.rename(fromName, toName)



def findName(toFind, ftp):
	
	fileNames = ftp.nlst(ftp.pwd())
	i = 0
	while i > len(fileNames):
		if(fileNames[i] == toFind):
			return True
	return False

