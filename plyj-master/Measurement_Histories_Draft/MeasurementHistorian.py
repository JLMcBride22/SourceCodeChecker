import os
import sqlite3
from sqlite3 import Error

# IF this  has module issues let know immediately.


#This class will handle all the methods for storing/searching reports.
class MeasurementHistorian:

    #Standard sqlite function for  creating a connection to a database file.
    #Takes the file path.
    #If does not exist, will create one.
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn
    #***********************************

    # This creates a table in SQLite, taking the connection to the database file and the table format.
    def create_table(conn, create_table_sql):
    
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    # This creates a table for analysis reports, using the data connection and a hardcoded table format.
    # Has to call create_table.
    # Any changes to our database structure will be done here.
    def create_analysis_table(self, conn):
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS AnalysisReports (
                                        id integer PRIMARY KEY,
                                        filename text NOT NULL,
                                        timestamp text, datasize text,
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

                                    ); """
        if conn is not None:
            self.create_table(conn, sql_create_projects_table )
        else:
            print("Error! cannot create the database connection.")
    #************************************************************

    def create_function_table(self, conn):
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS FunctionReports (
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

                                    ); """
        if conn is not None:
            self.create_table(conn, sql_create_projects_table )
        else:
            print("Error! cannot create the database connection.")
    #*************************************************************************
    # Take an analysis report and add it to our report table. 
    def create_analysis_report(conn, report):
        sql = ''' INSERT INTO AnalysisReports(filename, timestamp, datasize, DateAnalyzed, ESLOC,
                                        SLOCnoComm,
                                        SLOCComm,
                                        BlankLines,
                                        FullCommLines,
                                        Semicolons,
                                        FunctionCalls,
                                        NumPassedParam,
                                        McCabeCyclComp,
                                        Halstead,
                                        MaxNest,
                                        ESLOCMaxNest,
                                        SwitchComp,
                                        NumForLoop,
                                        NumWhileLoop,
                                        NumRepeatLoop,
                                        NumInts,
                                        NumFloat,
                                        NumChar,
                                        NumString,
                                        NumUserDef,
                                        NumStruct,
                                        NumArray,
                                        Num3Char,
                                        Num3thru9Char,
                                        Num10thru19Char,
                                        Num20Char,
                                        PreambleFilename,
                                        PreambleAuthor,
                                        PreamblePurpose,
                                        PreambleInterface,
                                        PreambleAssumptions,
                                        PreambleChangeLog,
                                        NoGoTo,
                                        OneEntry,
                                        OneExit,
                                        RecursionStatus,
                                        VariableNamesAtLeastXChar,
                                        VariableNamesNoLongXChar,
                                        DefineParamAllCAPS,
                                        VarNamesNotAllCAPS,
                                        McCabeLessThanX,
                                        NestingLessThanX,
                                        ESLOCLessThanXinFunc,
                                        LocalizationOfVar)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, report)
        conn.commit()
        return cur.lastrowid


    def create_function_report(conn, report):
        sql = ''' INSERT INTO FunctionReports(filename, timestamp, datasize, DateAnalyzed, ESLOC,
                                        SLOCnoComm,
                                        SLOCComm,
                                        BlankLines,
                                        FullCommLines,
                                        Semicolons,
                                        FunctionCalls,
                                        NumPassedParam,
                                        McCabeCyclComp,
                                        Halstead,
                                        MaxNest,
                                        ESLOCMaxNest,
                                        SwitchComp,
                                        NumForLoop,
                                        NumWhileLoop,
                                        NumRepeatLoop,
                                        NumInts,
                                        NumFloat,
                                        NumChar,
                                        NumString,
                                        NumUserDef,
                                        NumStruct,
                                        NumArray,
                                        Num3Char,
                                        Num3thru9Char,
                                        Num10thru19Char,
                                        Num20Char,
                                        PreambleFilename,
                                        PreambleAuthor,
                                        PreamblePurpose,
                                        PreambleInterface,
                                        PreambleAssumptions,
                                        PreambleChangeLog,
                                        NoGoTo,
                                        OneEntry,
                                        OneExit,
                                        RecursionStatus,
                                        VariableNamesAtLeastXChar,
                                        VariableNamesNoLongXChar,
                                        DefineParamAllCAPS,
                                        VarNamesNotAllCAPS,
                                        McCabeLessThanX,
                                        NestingLessThanX,
                                        ESLOCLessThanXinFunc,
                                        LocalizationOfVar)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, report)
        conn.commit()
        return cur.lastrowid          


    # Debugging function. Will print the entire contents of the database to the console.
    def print_all_reports(conn):
    
        cur = conn.cursor()
        cur.execute("SELECT * FROM AnalysisReports")

        rows = cur.fetchall()

        for row in rows:
            print(row)




#******************************************************************************************

    # Given a MeasurementHistorian instance, connection to a database, and the name of the file...
    # will search the AnalysisReport database for all instances of that filename. 
    def search_archive_filename(self, conn, filename):
        IdList = []
        cur = conn.cursor()
        if (self.entry_exists(conn, filename)):
            rows = cur.execute("SELECT * FROM AnalysisReports WHERE filename = ?", (filename,))
            for row in rows:
                IdList.append(row[0])
            return IdList

    #***********************************


    # Will check if an entry exists based on the stored filename. Takes a filename as input.
    # Returns true if an entry exists, false if not.
    def entry_exists(conn, filename):
        cur = conn.cursor()
        #cur.execute("SELECT * FROM AnalysisReports WHERE EXISTS(SELECT * FROM AnalysisReports WHERE filename=?)",(filename,))
        #cur.execute("SELECT EXISTS(SELECT 1 FROM AnalysisReports WHERE filename=?)",(filename,))
        cur.execute("SELECT rowid FROM AnalysisReports WHERE filename = ?", (filename,))
        data = cur.fetchall()
        
        if len(data) == 0:
            print(filename + " not found in report archive.")
            return False

        else:
            return True

if __name__ == '__main__':
    mhist = MeasurementHistorian
    dataconn = mhist.create_connection("test3.db")
    with dataconn:

        report1 = ("Test", "Hello", "filler", 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
        report2 = ("Hello", "Hello", "filler", 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
        report3 = ("Java", "Hello", "filler", 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
        report4 = ("Goodbye", "Hello", "filler", 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
        mhist.create_analysis_table(mhist, dataconn)
        mhist.create_function_table(mhist, dataconn)
        #mhist.create_analysis_report(dataconn, report1)
        #mhist.create_analysis_report(dataconn, report2)
        #mhist.create_analysis_report(dataconn, report3)
        #mhist.create_analysis_report(dataconn, report4)
        #tempcheck = mhist.entry_exists(dataconn, "pizza")
        #mhist.print_all_reports(dataconn)
        #tempList = mhist.search_archive_filename(mhist, dataconn, "Java")
        #for Id in tempList:
            #   print(Id)



        # NEED TO UPDATE FOR BYTE SIZE AND UPDATE THE EXCEL CONVERTER.
