# Jonas Persson
# CS410 Agile Summer 2022 Portland State

def get_single(ftp, files_to_get):
    try:
        ftp.retrbinary("RETR a.png", open('a.png', 'wb').write)       # author/source: https://pythontic.com/ftplib/ftp/retrbinary
    except:                                                           # wb - indicates binary write mode
        pass
