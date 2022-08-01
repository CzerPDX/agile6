from ftplib import FTP
import logging


def copyDir(ftp):
    toCopy = input("Enter Name of Copy")
    files = ftp.nlst()
    for file in files:
        ftp.retrbinary("RETR "+file, open(file[1:], 'wb').write)
    ftp.close
    



