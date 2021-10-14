import xlsxwriter


# This class will handle converting an analysis report to an Excel file.
# Currently relies on report being a text file in a two column format.

class ExcelConverter:

    # Converts a text file to an Excel workbook with one spreadsheet.
    # Takes a filepath string as input.
    def textToExcel(filepath):

        # Declaring a temporary list to hold file data.
        stringlist = []


        # Opening input file in read mode.
        f = open(filepath, "r")

        # We read the file into the list, where each line is a string list nested inside ExcelConverter's list. 
        # Each element of a nested list is a word from the file, so stringlist is a list of lists that holds the words for each line for the file.
        for line in f:
            stripped_line = line.strip()
            templist = stripped_line.split()
            stringlist.append(templist)
        f.close()


        # Debug statement to ensure your list is correct.
        #print(stringlist)



        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Test.xlsx')
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        for item, value in (stringlist):
         worksheet.write(row, col,     item)
         worksheet.write(row, col + 1, value)
         row += 1

        # Close the workbook when finished.
        workbook.close()


# Test main for this code
test1 = ExcelConverter
print('Enter your filepath')
filepath = input()
test1.textToExcel(filepath)
