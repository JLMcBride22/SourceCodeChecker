
import PyQt5.QtGui as testing
from PyQt5 import QtWidgets as qtw


from UIFiles.GCHistory import Ui_HistoryForm

from UIFiles.GCFileSubGUI import Ui_FileSubForm

from Measurement_Histories_Draft.MeasurementHistorian import MeasurementHistorian

class historyForm(qtw.QWidget):
    
    uiForm = Ui_HistoryForm()
    def __init__(self, *args, **kwargs):
        
        super(historyForm, self).__init__(*args, **kwargs)
        
        self.uiForm.setupUi(self)
        self.uiForm.pushButton.clicked.connect(self.close)
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
        historyList = [1,2,3]
        #historyList =  mhist.pullHistory(mhist, tempconn, "Test")
        i = 0
        
        for rowid in historyList:

            self.uiForm.tableWidget.insertRow(i)
            col = 0
            while col < 48:
                self.uiForm.tableWidget.setItem(i, col, qtw.QTableWidgetItem("hello"))
                col += 1
            i +=1
        
        

        
        
        