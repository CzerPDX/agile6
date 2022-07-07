import os
 
def listLocal():
    # Get the list of all files and directories
    path = os.getcwd()
    dir_list = os.listdir(path)
    
    print("Files and directories in '", path, "' :")
    
    # prints all files
    print(dir_list)