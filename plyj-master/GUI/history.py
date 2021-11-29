
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
        if os.path.exists("tempList.txt"):
            with open('tempList.txt', 'r') as f:
                for line in f:
                    historyList.append(line)
                f.close()

        
        #historyList =  mhist.pullHistory(mhist, tempconn, "Test")
        i = 0
        conn = sqlite3.connect("test3.db")
        for rowid in historyList:
            cur = conn.cursor()
            entry = cur.execute("SELECT * FROM AnalysisReports WHERE ID = ?", (rowid,))
            
            rowList = []
            k = 2
            for row in entry:
                while k < 48:
                    
                    rowList.append(row[k])
                    k += 1
            self.uiForm.tableWidget.insertRow(i)
            col = 0
            
            k = 0
            while col < 48:
                tempstring = "hello"
                
                print(k)
                print(len(rowList))
                tempstring = str(rowList[k])
                self.uiForm.tableWidget.setItem(i, col, qtw.QTableWidgetItem(tempstring))
                if(k  < 45):
                    k += 1
                col += 1
            i +=1
        
        

        
        
        