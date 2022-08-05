from ftplib import FTP
import logging
import getfiles
import os

def copyDir(ftp, toCopy):
    localPath = os.getcwd()                     #Get local path
    remotePath = ftp.pwd()


    getfiles.get_directory(ftp, toCopy)          #Download Copy


    newlocalPath = os.path.join(localPath, toCopy)
    os.chdir(newlocalPath)

    newremotePath = remotePath + '/Copy of ' + toCopy
    ftp.mkd(newremotePath)
    ftp.cwd(newremotePath)

    files = os.listdir()

    for file in files:
        ftp.storbinary('STOR ' + file, open(file[0:], 'rb'))

    for file in files:
        toRemove = os.path.join(newlocalPath, file)
        os.remove(toRemove)
    os.rmdir(newlocalPath)




