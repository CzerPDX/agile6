import logging
from ftplib import FTP

def listDir(ftpAddr, usr):
    ftp = FTP(ftpAddr)
    ftp.dir()
    