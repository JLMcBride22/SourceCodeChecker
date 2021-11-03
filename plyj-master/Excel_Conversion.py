import xlsxwriter
import sqlite3

from Measurement_Histories_Draft.MeasurementHistorian import MeasurementHistorian

# This class will handle converting an analysis report to an Excel file.
# Will grab from sql database.

class ExcelConverter:

    # Will convert analysis report for files to an Excel workbook.
    # Has 3 parameters.
    # conn is the dataconnection object, which we can create through Measurement Historian.
    # conn connects to the sqlite database, and is needed to pull in info from reports.
    # filelist is a string list of filenames, as they are stored in sqlite database.
    # ExcelName is the name of the excel file, in .xlsx format
    def reportToExcel(conn, filelist, ExcelName):

        # Create a cursor object
        cur=conn.cursor()

        # Create a workbook and add a worksheet, format column size.
        workbook = xlsxwriter.Workbook(ExcelName)
        worksheet = workbook.add_worksheet()
        worksheet.set_column(1,50,20)
        # Define format object so we can add boldface.
        cell_format = workbook.add_format()
        cell_format.set_bold()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0
        # Column header names. Need to change to grab from sql in the future.
        columnnames = ["id","filename", "timestamp", "ESLOC", "SLOCnoComm", "SLOCComm", "BlankLines", "FullCommLines","Semicolons", "FunctionCalls","NumPassedParam",
                        "McCabeCyclComp","Halstead","MaxNest","ESLOCMaxNest","SwitchComp","NumForLoop","NumWhileLoop","NumRepeatLoop","NumInts","NumFloat",
                        "NumChar","NumString","NumUserDef","NumStruct","NumArray","Num3Char","Num3thru9Char","Num10thru19Char","Num20Char",
                        "PreambleFilename","PreambleAuthor","PreamblePurpose","PreambleInterface","PreambleAssumptions","PreambleChangeLog",
                        "NoGoTo","OneEntry","OneExit","RecursionStatus","VariableNamesAtLeastXChar","VariableNamesNoLongXChar",
                        "DefineParamAllCAPS","VarNamesNotAllCAPS","McCabeLessThanX","NestingLessThanX","ESLOCLessThanXinFunc","LocalizationOfVar"]

        # Set column names in document.
        for header in columnnames:
            worksheet.write(row, col, header, cell_format)
            col+=1
        col = 0
        row = 1

        # For every file we need to send to excel, grab the data from its report and save it to the workbook.
        # Each row in workbook is one analysis report.
        for file in filelist:
            
            cur.execute("SELECT * FROM AnalysisReports WHERE filename=?", (file,))
            data = cur.fetchall()
            # Saving all reports.
            for entry in data:
                i = 0

                # Saving one report.
                while i < 48:
                    worksheet.write(row, col, entry[i])
                    col +=1
                    i+=1
                row += 1
                col = 0

        # Close the workbook when finished.
        workbook.close()



    

#*****************************************************
# Test main for this code
test1 = ExcelConverter

mhist = MeasurementHistorian

# Create connection to our test database.
dataconn = mhist.create_connection("test.db")
# Here we have a hardcoded list, corresponding to our test db.
# Last entry is not present in the db, used to test handling bad filenames.
# If nothing is generated, make sure data is present in the db using sqlite and MeasurementHistorian

templist = ["Test", "Hello", "Java", "garbage"]
# Using 
with dataconn:
    test1.reportToExcel(dataconn, templist, "Test.xlsx")

