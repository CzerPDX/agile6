from ftplib import FTP
import os  
import logging


def copyDir(ftp, toCopy):
    localPath = os.getcwd()
    remotePath = ftp.pwd()

    ftp.cwd(remotePath + toCopy)

    newlocalPath = os.path.join(localPath, toCopy)
    os.mkdir(newlocalPath)
    os.chdir(newlocalPath)

    files = ftp.nlst()

    files = files[1:-1]
    for file in files:
        ftp.retrbinary("RETR "+file, open(file[0:], 'wb').write)
