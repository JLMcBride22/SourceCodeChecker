#######################################################################################
#
#
#
#######################################################################################
import sys
sys.path.append(".")
from PyQt5.QtWidgets import QTableView
#from Excel_Conversion import ExcelConverter

from MetricCalc.PostCompileCalc import myParser2


from PyQt5.QtSql import*
from PyQt5.QtCore import Qt
from Excel_Conversion import ExcelConverter

import Utilities.xlsxwriter
from Measurement_Histories_Draft.MeasurementHistorian import MeasurementHistorian
import os

class ARI():
    
    def __init__(self):
        self.uncompilable = ""
        self.db =  QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('test3.db')
        self.db.open()
        self.db.transaction()
        self.db.exec_(
           ''' CREATE TABLE IF NOT EXISTS AnalysisReports (
                                        id integer PRIMARY KEY,
                                        filename text NOT NULL,
                                        timestamp text,
                                        ESLOC integer,
                                        SLOCnoComm integer,
                                        SLOCComm integer,
                                        BlankLines integer,
                                        FullCommLines integer,
                                        Semicolons integer,
                                        FunctionCalls integer,
                                        NumPassedParam integer,
                                        McCabeCyclComp integer,
                                        Halstead integer,
                                        MaxNest integer,
                                        ESLOCMaxNest integer,
                                        SwitchComp text,
                                        NumForLoop integer,
                                        NumWhileLoop integer,
                                        NumRepeatLoop integer,
                                        NumInts integer,
                                        NumFloat integer,
                                        NumChar integer,
                                        NumString integer,
                                        NumUserDef integer,
                                        NumStruct integer,
                                        NumArray integer,
                                        Num3Char integer,
                                        Num3thru9Char integer,
                                        Num10thru19Char integer,
                                        Num20Char integer,
                                        PreambleFilename text,
                                        PreambleAuthor text,
                                        PreamblePurpose text,
                                        PreambleInterface text,
                                        PreambleAssumptions text,
                                        PreambleChangeLog text,
                                        NoGoTo text,
                                        OneEntry text,
                                        OneExit text,
                                        RecursionStatus text,
                                        VariableNamesAtLeastXChar text,
                                        VariableNamesNoLongXChar text,
                                        DefineParamAllCAPS text,
                                        VarNamesNotAllCAPS text,
                                        McCabeLessThanX text,
                                        NestingLessThanX text,
                                        ESLOCLessThanXinFunc text,
                                        LocalizationOfVar text

                                    ) '''
        )
        self.db.commit()
        
        
       



        ##creating the model for the tableview
        self.dbModel = QSqlTableModel()
        #these two lines connect the database to the model
        self.dbModel.setTable("AnalysisReports")
        self.dbModel.select()
        
        #you have to manually submit your changes. by you using model.submitAll()
        self.dbModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.record = self.dbModel.record()
        self.record.setGenerated('tableid', False)
        #self.dbModel.submitAll()
    
    #returns the SQL model
    def getModel(self)->QSqlTableModel:
        return self.dbModel

    #inserts a list of data into table model.
    def insertData(self, inList:list):
        i = 1
        for item in inList:
            self.record.setValue(i, item)
            i += 1
          
        ## -1 mean inserted at the bottem
        self.dbModel.insertRecord(-1, self.record)
        
            

        return 0
    #This takes the filepath to the compiler
    def takeFileList(self, filePathList: list):
        self.uncompilable = ""
        listOfOutputs = []
        for filePath in filePathList:
            pars = myParser2()

            try:
                pars.findMetrics(filePath)
            except AttributeError:
                self.uncompilable = filePath
                return
            

            listOfOutputs.append(pars.output)
            
            #record = pars.getRecord()
            #print(record.isGenerated(1))
            ##self.dbModel.insertRowIntoTable(record)
            #self.dbModel.insertRecord(-1,record)
        
        for output in listOfOutputs:
            self.insertData(output)


        self.dbModel.submitAll()
        
    def getUncompiled(self):
        return self.uncompilable

    ##This is where the Excel_Conversion.py
    def generateExcelsAll(self, fileDirectory):
        print(fileDirectory)
        conn = self.db.databaseName()
        print(conn)
        mHist = MeasurementHistorian
        testConverter = ExcelConverter
        
         
        quer = QSqlQuery('Select filename FROM AnalysisReports')
        listOfFilenames = []
        while quer.next():
            listOfFilenames.append(quer.value(0))

            

        
        dataconn =  mHist.create_connection(conn)
        
        testConverter.reportToExcel(dataconn, listOfFilenames, fileDirectory)







            
