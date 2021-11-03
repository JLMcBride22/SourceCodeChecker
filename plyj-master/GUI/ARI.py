# The goal of this module is to exchange critical data between the frontend and backend
# It needs to take in the list of filepath and the metric. I would also want to see that
# it gives the model to the table for displaying ideally with SQLite..

from parseFile import myParser2

import sys
from PyQt5.QtSql import*
from PyQt5.QtCore import Qt

import os

class ARI():

    def __init__(self):
        
        self.db =  QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('MainTable.db')
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

    #inserts data into table model.
    def insertData(self, inList:list):
        i = 1
        for item in inList:
            self.record.setValue(i, item)
            i += 1
            
        
        self.dbModel.insertRecord(-1, self.record)
        
            

        return 0
        
    def takeFileList(self, filePathList: list):
        
        
        for filePath in filePathList:
            pars = myParser2()
            pars.findMetrics(filePath)
            self.insertData(pars.output)
            
            #record = pars.getRecord()
            #print(record.isGenerated(1))
            ##self.dbModel.insertRowIntoTable(record)
            #self.dbModel.insertRecord(-1,record)
            
        self.dbModel.submitAll()
        

            
            



if __name__ == '__main__':

    a = ARI()
    filepaths =["JavaTest\\AccessControl.java",
        "JavaTest\\AddDialog.java",
        "JavaTest\\AreYouSureDialog.java",
        "JavaTest\\Controller.java",
        "JavaTest\\defaultPage.java",
        "JavaTest\\dev.java",
        "JavaTest\\ingrePanel.java",
        "JavaTest\\loginGUI.java",
        "JavaTest\\Main.java",
        "JavaTest\\Personal_Income_Tax.java",
        "JavaTest\\AccessControl.java"]
    

    a.takeFileList(filepaths)
            
