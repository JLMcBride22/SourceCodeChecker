# The goal of this module is to exchange critical data between the frontend and backend
# It needs to take in the list of filepath and the metric. I would also want to see that
# it gives the model to the table for displaying ideally with SQLite..

from parseFile import myParser2
import os


class ARI():

    def __init__(self):
        x = 1

    def takeFileList(self, filePathList: list):
        pars = myParser2()
        for filePath in filePathList:
           # f = open(filePath, "r")
           # sourceLine = f.readlines
           # print(sourceLine)
            pars.parseThisFile(filePath)
            print('\n')
            open(filePath, 'r') in file
            fileTxt = file.read()
            print(fileTxt)

        return
