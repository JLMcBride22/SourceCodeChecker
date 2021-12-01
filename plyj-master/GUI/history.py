
import PyQt5.QtGui as testing
from PyQt5 import QtWidgets as qtw

import os

import sqlite3

from UIFiles.GCHistory import Ui_HistoryForm

from UIFiles.GCFileSubGUI import Ui_FileSubForm

from Measurement_Histories_Draft.MeasurementHistorian import MeasurementHistorian

class historyForm(qtw.QWidget):
    
    uiForm = Ui_HistoryForm()
    def __init__(self, *args, **kwargs):
        
        super(historyForm, self).__init__(*args, **kwargs)
        
        self.uiForm.setupUi(self)
        j = 0
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
        #mhist = MeasurementHistorian()
        #tempconn = mhist.create_connection(mhist, "test3.db")
        historyList = []
        #historyList =  mhist.pullHistory(mhist, tempconn, "Test")
        

        
        #historyList =  mhist.pullHistory(mhist, tempconn, "Test")
        
        
            

    def loadHistTable(self, contentList):
        i = 0
        for row in contentList:
            
            self.uiForm.tableWidget.insertRow(i)
            
            col = 0
            k = 1
            while col < (len(row)-1):
                
                self.uiForm.tableWidget.setItem(i, col, qtw.QTableWidgetItem(str(row[k])))
                
                col += 1
                k+=1
            i+=1


        
        
        