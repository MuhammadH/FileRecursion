import os, sys
from os import stat
from stat import *

# upDir is the current directery being passed in
# stringComp is the string we're searching for in file names
# topRecursion tells us if this is the first iteration of the recursion
def RecFiles (upDir, stringComp, topRecursion):

    # set fileSize to zero
    fileSize = 0

    # check every directory/ file in the current directory
    for internal in os.listdir(upDir):

        # get the potential next directory name
        nextDir = os.path.join(upDir, internal)

        # get the mode for the next file
        nextMode = os.stat(nextDir).st_mode

        # if directory
        if S_ISDIR(nextMode):
            
            # check for stringComp
            if stringComp in internal:
                print ("Found: " + nextDir)
            
            # recursively check next directory
            fileSize += RecFiles(nextDir, stringComp, 0)
            
        # else if normal file
        elif S_ISREG(nextMode):

            # check for stringComp, if so, add file size and print file
            if stringComp in internal:
                fileStat = stat(nextDir)
                print ("Found: " + nextDir + " " + str(fileStat.st_size))
                fileSize += fileStat.st_size

    # print the file size of all normal files found
    # if this is the top recursion
    if topRecursion:
        print ("total file sizes: " + str(fileSize))
    
    return fileSize



topDir = input("Enter directory to start search in")
searchFor = input("Enter string to search for")
RecFiles (topDir, searchFor, 1)
