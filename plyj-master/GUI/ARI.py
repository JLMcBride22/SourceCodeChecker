"""
======================================================================================
*
*
* @name:      ARI.py(Analysis report Interface)
* @author(s): Jonathan Lewis
* @date:      12/01/2021
* @purpose:   The purpose of this file manages the database and inserting the results of the parser
*             into the database.
*             
*
*
=======================================================================================

"""
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
#The main objectives of the ari class is to interface the frontend with the backend of the program. It house the database and the model and it runs it to the parsar
class ARI():
    #In the init of the ARI, we create the database(if one doesn't exist) and a model for the table.
    #
    def __init__(self):
        self.tableView =None
        #This is label that displays if the table is empty or not.
        self.emptyLabel = None
        #The following is the list of uncompilables. 
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
                                        Filesize text,
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
                                        LocalizationOfVar text,
                                        longFileName text

                                    ) '''
        )
        ##Commit the changes
        self.db.commit()
        
        
       



        ##creating the model for the tableview
        self.dbModel = QSqlTableModel()
        
        #these two lines connect the database to the model
        self.dbModel.setTable("AnalysisReports")
        self.dbModel.select()

        #The following code checks if the db is empty on intial open
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

    #inserts a list of data in row into the table model.
    def insertData(self, inList:list):
        i = 1
        for item in inList:
            self.record.setValue(i, item)
            i+=1

          
        ## -1 means inserted at the bottem
        self.dbModel.insertRecord(-1, self.record)
        #This is where we resize the columns and reset the ID column width back to 0
        self.tableView.resizeColumnsToContents()
        self.tableView.setColumnWidth(0,0)
        self.tableView.setEnabled(True)
    #Allows ARI to control the fit the columns
    def setTable(self , tableView:QTableView):
        self.tableView = tableView

            

        return 0

    def setEmptyLabel(self, emptyLabelIn):
        self.emptyLabel = emptyLabelIn
    


    #This method takes the sends the list and sends the filepath through the parser with the all the metrics that were checked.
    def takeFileList(self, filePathList: list, listOfCheckedMetrics : list):
        self.uncompilable = []
        listOfOutputs = []
        for filePath in filePathList:
            pars = myParser2()
            

            
            #This try catch is a crucial component in case of compliation failure.
            # In case of failure it just adds to the list of uncompilable pathways and
            # proceeds with the submission.
            try:
                pars.findMetrics(filePath,listOfCheckedMetrics)
                listOfOutputs.append(pars.output)
            except AttributeError:
                self.uncompilable.append(filePath)
            
        
    
        for output in listOfOutputs:

            self.insertData(output)
            

        #Submits them all from the model to the database
        self.dbModel.submitAll()
        if self.isEmpty:
            self.emptyLabel.setHidden(True)
            self.isEmpty = False

    #Returns true if the filePath is already in the table
    def checkForRedundent(self, pathway, timestamp)-> bool:
        q = QSqlQuery(self.db)
        qStr = "Select * FROM AnalysisReports WHERE longFileName = \'" + str(pathway) +"\' AND timestamp = \'"+ timestamp+ "\';"
        q.exec(qStr)
        if q.next():
            return True
        else:
            return False

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
        
        mHist = MeasurementHistorian
        testConverter = ExcelConverter
        
         
        quer = QSqlQuery('Select filename FROM AnalysisReports')
        listOfFilenames = []
        while quer.next():
            listOfFilenames.append(quer.value(0))

            

        
        dataconn =  mHist.create_connection(dbName)
        
        testConverter.reportToExcel(dataconn, listOfFilenames, fileDirectory)

 





            
