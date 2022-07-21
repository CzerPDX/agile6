from ftplib import FTP


def createDir(ftp):

    #Ask for a the name of the new directory
    newDir = input("What is the name of the new directory?")
    #Create a new directory
    ftp.mkd(newDir)

