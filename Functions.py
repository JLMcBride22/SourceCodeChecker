from queue import Queue

def fileQueue (maxSize,file):

# Initializing a queue
q = Queue(maxSize)
c = 0
if(c < q):
# Adding of element to queue
q.put(file)
c = c + 1
else :
    print ("\nFull:", q.full())

############################################################

# retrieve data for filename and date
import os
import platform

 #Function to get the date of file
def creation_date(filePath):
 
    if platform.system() == 'Windows':

        return os.path.getctime(filePath)
    else:
        stat = os.stat(filePath)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

 ############################################################

 #Function to get the name of file

import pathlib

def file_name_created(filePath)

path = filePath

filename = pathlib.Path(path).name

print(filename)











