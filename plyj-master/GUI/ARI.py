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
        self.tableView =None
        self.emptyLabel = None
        self.uncompilable = []
        ##This sets up the database for the QSQlDatabase
        self.db =  QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('test3.db')
        self.db.open()
        self.db.transaction()
        self.db.exec_(
           ''' CREATE TABLE IF NOT EXISTS AnalysisReports (
                                        id integer PRIMARY KEY,
                                        filename text NOT NULL,
                                        timestamp text,
                                        datasize text,
                                        DateAnalyzed text,
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
        ##Commit the changes
        self.db.commit()
        
        
       



        ##creating the model for the tableview
        self.dbModel = QSqlTableModel()
        
        #these two lines connect the database to the model
        self.dbModel.setTable("AnalysisReports")
        self.dbModel.select()
        self.isEmpty = False
        if self.dbModel.rowCount() == 0:
            self.isEmpty = True
            

        #you have to manually submit your changes. by you using model.submitAll()
        self.dbModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        self.record = self.dbModel.record()
        self.record.setGenerated('tableid', False)
        #self.dbModel.submitAll()
    
    #returns the SQL model
    def getModel(self)->QSqlTableModel:
        return self.dbModel

    #inserts a list of data intoa row of the table model.
    def insertData(self, inList:list):
        i = 1
        for item in inList:
            self.record.setValue(i, item)
            i+=1

          
        ## -1 means inserted at the bottem
        self.dbModel.insertRecord(-1, self.record)
        self.tableView.resizeColumnsToContents()
    #Allows ARI to control the fit the columns
    def setTable(self , tableView:QTableView):
        self.tableView = tableView

            

        return 0

    def setEmptyLabel(self, emptyLabelIn):
        self.emptyLabel = emptyLabelIn
    #This takes the filepath to the compiler
    def takeFileList(self, filePathList: list, listOfCheckedMetrics : list):
        self.uncompilable = []
        listOfOutputs = []
        for filePath in filePathList:
            pars = myParser2()

            #This try catch is a crucial component in case of compliation failure.
            # In case of failure it just adds to the list of uncompilable pathways and
            # proceeds with the submission.
            #try:
            pars.findMetrics(filePath,listOfCheckedMetrics)
                #This is a list of a list lol!
            listOfOutputs.append(pars.output)
            #except AttributeError:
                #self.uncompilable.append(filePath)
            

            
            
            #record = pars.getRecord()
            #print(record.isGenerated(1))
            ##self.dbModel.insertRowIntoTable(record)
            #self.dbModel.insertRecord(-1,record)
        
    
        for output in listOfOutputs:

            self.insertData(output)
            

        #Submits them all from the model to the database
        self.dbModel.submitAll()
        if self.isEmpty:
            self.emptyLabel.setHidden(True)
            self.isEmpty = False

    #This sends back a list of uncompilable file path ways.  
    def getUncompiled(self):
        return self.uncompilable

    #This fuction uses a SQL command to search for a cell given the columnName and the row number.
    # This is implemented when the user selects a row and right clicks to view metric/history of report 
    #TODO This may causes us a bug if we add a remove feature.
    def getCellContentFromDataBase(self, rowNo, columnName:str):
        q = QSqlQuery(self.db)
        qStr = "Select [" + columnName + "] FROM AnalysisReports WHERE id = " + str(rowNo)+";"
        q.exec(qStr)
        while q.next():
           return q.value(0)


        
        

    ##This is where the Excel_Conversion.py
    def generateExcelsAll(self, fileDirectory):
        
        dbName = self.db.databaseName()
        print(dbName)
        mHist = MeasurementHistorian
        testConverter = ExcelConverter
        
         
        quer = QSqlQuery('Select filename FROM AnalysisReports')
        listOfFilenames = []
        while quer.next():
            listOfFilenames.append(quer.value(0))

            

        
        dataconn =  mHist.create_connection(dbName)
        
        testConverter.reportToExcel(dataconn, listOfFilenames, fileDirectory)







            
