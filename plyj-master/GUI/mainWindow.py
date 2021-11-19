import sys



from PyQt5.QtGui import QCloseEvent



sys.path.append("./GUI")


from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog, QMenu, QTableView, QMessageBox

from PyQt5.QtSql import QSqlQuery, QSqlTableModel

from PyQt5.QtCore import QEvent, QItemSelection, QItemSelectionModel, Qt, QModelIndex

from FileSubmitForm import FileSubmitForm
from history import historyForm
from metricReport import metricFormC
from UserHelp import userHelpC


from UIFiles.GCMainWindowGUI import Ui_MainWindow

import os
from PyQt5.QtWidgets import QAbstractItemView, QDialog, QLabel, QToolButton

##SQL

##backend imports
from ARI import ARI


class MainWindow(qtw.QMainWindow):
    ui = Ui_MainWindow()

    excelBtnDict = {}
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui.setupUi(self)
        self.ui.actionInstruction.associatedGraphicsWidgets
        self.ari = None
        ## Adds the function to the button/menu options.
        self.ui.actionInstruction.triggered.connect(self.openHelp)
        self.ui.actionSingle_file.triggered.connect(self.uploadFile_s)
        self.ui.actionExport_File.triggered.connect(self.excelOpen)
        self.fileSubmit = None
        self.popUpMenu =QMenu()
        
        



        

        ##buttons
        self.ui.addFilesButton.clicked.connect(self.uploadFile_s)
        
    
        self.ui.refreshAllButton.clicked.connect(self.refresh)
        self.ui.JavaTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.JavaTableView.installEventFilter(self)
        self.ui.JavaTableView.resizeColumnsToContents()
        #self.ui.JavaTableView.hideColumn(0)

        self.actionMetric = self.popUpMenu.addAction("View Function/Classes Reports")
        self.actionHistory=self.popUpMenu.addAction("View History")
        self.actionHistory.triggered.connect(self.viewHistory)
        self.actionMetric.triggered.connect(self.viewMetrics)
        

    

    def setARI(self, ariPARAM: ARI):
        self.ari = ariPARAM
        self.ari.setTable(self.ui.JavaTableView)
        self.ari.setEmptyLabel(self.ui.label)
        if(not self.ari.isEmpty):
            self.ui.label.setHidden(True)
        
        self.populate_table()
        
        

    # Opens the dialog for help
    def openHelp(self):
        help = userHelpC(self)
        help.setWindowTitle("Help")
                
        help.setWindowFlag(True)
        help.show()
    
    def excelOpen(self):
        dlg = QFileDialog.getSaveFileName(self, 'Save File',filter='xlsx(*.xlsx)',directory='ExcelTest')
        
        if(dlg[0] != ""):
            self.ari.generateExcelsAll(dlg[0])
            

    def refresh(self):
        self.ui.JavaTableView.resizeColumnsToContents()



    def eventFilter(self, source, event):
            if event.type() == QEvent.ContextMenu and source is self.ui.JavaTableView:
                
                
                
                if self.popUpMenu.exec_(event.globalPos()):
                    
                    return True

            return super().eventFilter(source, event)
    
    def uploadFile_s(self):
        

        self.fileSubmit = FileSubmitForm(self)
        
        self.fileSubmit.setARI(self.ari)
        self.fileSubmit.show()
        
            
        ##fileSubmit.setAutoFillBackground(True)
        
    #this gets the value of the selected row from SQL DB
    def getSelectedRowFromDB(self):
        selectionIndexes = self.ui.JavaTableView.selectedIndexes()
        
        if(len(selectionIndexes) > 0):
            index = selectionIndexes[0]
            
        else:
            dlg = QMessageBox()
            dlg.setText("You haven't selected a file")
            dlg.setInformativeText("Please select a file to view details.")
            dlg.setIcon(3)
            dlg.exec_()
            return None
        
        id= index.row() +1
    
        return id

        

    def viewHistory(self):
            #TODO dialog boxes
            id = self.getSelectedRowFromDB()
            if(id == ""):
                print("Must select at least 1")
            elif id == None:
                print("Can't select more than")
            else:
                fileName = self.ari.getCellContentFromDataBase(id,"filename")

                
                hist = historyForm(self)
                hist.setWindowTitle(fileName + " \'s History")
                
                hist.setWindowFlag(True)
                hist.show()

    def viewMetrics(self):
        
        met = metricFormC(self)

        row = self.getSelectedRowFromDB()
        if(row != None):
            xmlStr =self.ari.getCellContentFromDataBase(row, "LocalizationOfVar")
            met.strToXml(xmlStr)
            met.findItemRemoves()
            met.setVisible(True)
            met.setWindowFlag(True)
            met.show()
            met.showNormal()
        return
        

    



    ## Places the buttons in the table
    def populate_table(self):
        self.dbModel = QSqlTableModel(self)

        
        

        inModel = self.ari.getModel()
        


        
        self.ui.JavaTableView.setModel(inModel)
        self.ui.JavaTableView.resizeColumnsToContents()
        #hide columns
        self.ui.JavaTableView.hideColumn(0)
        self.ui.JavaTableView.hideColumn(48)
        self.ui.JavaTableView.setVisible(True)
        self.ui.JavaTableView.show()

        



if __name__ == '__main__':
    import sys
    a = ARI()

    app = qtw.QApplication(sys.argv)
    widget = MainWindow()
    widget.setARI(a)
    widget.__init__()
    w = qtw.QMainWindow()

    widget.show()

    sys, exit(app.exec_())
