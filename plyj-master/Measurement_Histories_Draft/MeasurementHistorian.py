# MeasurementHistorian.py
# Purpose: To handle the primary management of the SQL database for our program reports.
#          This includes creating tables, storing data, retrieving data, and certain data management checks.
# Author: James T. Kinkead
# Build Date: December 3, 2021.
#********************************




import os
import sqlite3
import datetime
from sqlite3 import Error


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

#****************************************************************************************************
   

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

    # Experimental function to search a database for all filenames that contain a given substring.
    # Based on the fact that we shouldn't expect a user to always give the exact filepath.
    # Likely to be used in searching the archive for past reports, where file might not be on disk.
    # Needs to be improved so that we aren't just
    def search_archive_filename_substring(self, conn, filename):
        IdList = []
        cur = conn.cursor()
        rows = cur .execute("SELECT * FROM AnalysisReports")
        for row in rows:
            if filename in row[1]:
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

    # This function takes a filepath, database connection, and a MeasurementHistorian object.
    # It returns a list of row Ids from the database, sorted in descending order of DateAnalyzed.
    # DateAnalyzed is assumed to be in the format given by datetime.datetime.now().
    # MORE TESTING OVER THE COURSE OF THE WEEK IS NEEDED TO MAKE SURE SORTING WORKS!
    def pullHistory(self, conn, filepath):
        if(self.entry_exists(conn, filepath)):
            IdList = []
            cur = conn.cursor()
            rows = cur.execute("SELECT * FROM AnalysisReports WHERE filename = ?", (filepath,))
            # Need a formal sorting function for agreed upon date format.
            
            for row in rows:
                
                # For each report, grab the rowid and the DateAnalyzed field
                IdList.append((row[0], row[4]))
                
            
            # Sort the Ids based on their respective DateAnalyzed fields, in descending order.
            IdList.sort(key=lambda tup: tup[1], reverse=True)

            # Debug statement, remove in final.
            print(IdList)

            # Since we want it to only return Ids, transfer Ids to a new list and return.
            SortedIdList = []
            for tuple in IdList:
                SortedIdList.append(tuple[0])
            return SortedIdList
        
        # IF an invalid filepath, return an error value.
        # This should only occur if the user edits the sqlite database mid execution, using sqlite software
        else:
            return False

    # This function will check if a file has been changed at all since analysis.
    # Requires the filepath and timestamp of input file.
    # For use on detecting whether to go forward with analysis or not.
    def checkIfChanged(self, conn, filename, timestamp):
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM AnalysisReports WHERE filename = ? AND timestamp = ? ", (filename, timestamp,))
        if len[rows] == 0:
            return True
        else:
            return False


    # This function pulls most of the data from rows going into the history window.
    # Takes an IDList, which should be sorted by pullHistory.
    # In future updates, would like this and pullHistory to be a single function.
    def pullHistoryContent(self, conn, IDList):
        cur = conn.cursor()
        contentList = []
        i = 0

        # loop through each iteration of the specified file and grab the needed information.
        for ID in IDList:
            rows = cur.execute("SELECT * FROM AnalysisReports WHERE ID = ?", (IDList[i],))
            for row in rows:
                j = 0
                rowList = []

                # Skip the last entry because the xml string is not needed.
                while j < (len(row) - 1):

                    # We do not want the filename.
                    if j != 1:
                        rowList.append(row[j])
                   
                    j+=1
                contentList.append(rowList)
                    
                
            i+=1
        return contentList

            


