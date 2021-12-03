# history.py
# Purpose: To display the history of a file's analysis
#          That means displaying every single report corresponding to a particular filepath.
#          Does so with the help of information obtained by MeasurementHistorian.py.
# Authors: James T. Kinkead, Jonathan Lewis.
# Build Date: December 3, 2021.
#********************************************************************************************
import PyQt5.QtGui as testing
from PyQt5 import QtWidgets as qtw

import os

import sqlite3

from UIFiles.GCHistory import Ui_HistoryForm

from UIFiles.GCFileSubGUI import Ui_FileSubForm

from Measurement_Histories_Draft.MeasurementHistorian import MeasurementHistorian

# Class that handles the formatting of the history window.
class historyForm(qtw.QWidget):
    
    uiForm = Ui_HistoryForm()
    def __init__(self, *args, **kwargs):
        
        super(historyForm, self).__init__(*args, **kwargs)
        
        self.uiForm.setupUi(self)
        j = 0
        # This loop controls how many columns you wish to display. Currently corresponds with the list below.
        # Currently does not directly utilize the list of column headers, due to earlier bugs.
        while j < 45:
            self.uiForm.tableWidget.insertColumn(j)
            j += 1
        self.uiForm.tableWidget.setHorizontalHeaderLabels(["timestamp", "datasize", "DateAnalyzed", "ESLOC",
                                        "SLOCnoComm",
                                        "SLOCComm",
                                        "BlankLines",
                                        "FullCommLines",
                                        "Semicolons",
                                        "FunctionCalls",
                                        "NumPassedParam",
                                        "McCabeCyclComp",
                                        "Halstead",
                                        "MaxNest",
                                        "ESLOCMaxNest",
                                        "SwitchComp",
                                        "NumForLoop",
                                        "NumWhileLoop",
                                        "NumRepeatLoop",
                                        "NumInts",
                                        "NumFloat",
                                        "NumChar",
                                       "NumString",
                                        "NumUserDef",
                                        "NumStruct",
                                        "NumArray",
                                        "Num3Char",
                                        "Num3thru9Char",
                                        "Num10thru19Char",
                                        "Num20Char",
                                        "PreambleFilename",
                                        "PreambleAuthor",
                                        "PreamblePurpose",
                                        "PreambleInterface",
                                        "PreambleAssumptions",
                                        "PreambleChangeLog",
                                        "NoGoTo",
                                        "OneEntry",
                                        "OneExit",
                                        "RecursionStatus",
                                        "VariableNamesAtLeastXChar",
                                        "VariableNamesNoLongXChar",
                                        "DefineParamAllCAPS",
                                        "VarNamesNotAllCAPS",
                                        "McCabeLessThanX",
                                        "NestingLessThanX",
                                        "ESLOCLessThanXinFunc",
                                        "LocalizationOfVar"])
        
#*******************************************************************      
        
        
            
    # This loads the rows of the table, corresponding with the headers in the previous version.
    def loadHistTable(self, contentList):
        i = 0
        # For each report, load the information into the row.
        for row in contentList:
            
            # Have to first insert the row for the data
            self.uiForm.tableWidget.insertRow(i)
            
            col = 0
            k = 1
            while col < (len(row)-1):
                # For each item in the report, insert it.
                self.uiForm.tableWidget.setItem(i, col, qtw.QTableWidgetItem(str(row[k])))
                
                col += 1
                k+=1
            i+=1


        
        
        