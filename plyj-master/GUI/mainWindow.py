import sys


sys.path.append("./GUI")

from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog, QMenu, QTableView

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import QEvent, QItemSelection, QItemSelectionModel, Qt, QModelIndex

from FileSubmitForm import FileSubmitForm
from history import historyForm
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
        
        self.popUpMenu =QMenu()
        
        



        

        ##buttons
        self.ui.addFilesButton.clicked.connect(self.uploadFile_s)
    
        self.ui.refreshAllButton.clicked.connect(self.viewHistory)
        self.ui.JavaTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.JavaTableView.installEventFilter(self)
        self.ui.JavaTableView.resizeColumnsToContents()
        #self.ui.JavaTableView.hideColumn(0)

        self.actionMetric = self.popUpMenu.addAction("View Metrics")
        self.actionHistory=self.popUpMenu.addAction("View History")
        self.actionHistory.triggered.connect(self.viewHistory)
        
        

    

    def setARI(self, ariPARAM: ARI):
        self.ari = ariPARAM
        
        self.populate_table()
        

    # Opens the dialog for help
    def openHelp(self):
        dlg = QDialog()
        dlg.setWindowTitle("Help")
        label = QLabel(dlg)
        label.setText("Help\n instructions: \nThis program does stuff. Figure it out for yourself")
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()
    
    def excelOpen(self):
        dlg = QFileDialog.getSaveFileName(self, 'Save File',filter='xlsx(*.xlsx)',directory='ExcelTest')
        self.ari.generateExcelsAll(dlg[0])
        



    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.ui.JavaTableView:
            
            
            
            if self.popUpMenu.exec_(event.globalPos()):
                
                selectionIndexes = self.ui.JavaTableView.selectedIndexes()
                if len(selectionIndexes) == 0 :

                    dlg = QDialog()
                    dlg.setWindowTitle("No item selected")
                    label = QLabel(dlg)
                    label.setText("Please Select an item")
                    label.adjustSize()
                    label.move(100, 60)
                    
                    
                
            ## connect action
            
            return True
        return super().eventFilter(source, event)
   
    #Opens the upload file screen. TODO need to change
    def uploadFile_s(self):
        fileSubmit = FileSubmitForm(self)
        
        fileSubmit.setARI(self.ari)
        ##fileSubmit.setAutoFillBackground(True)
        
        
        
        

        fileSubmit.show()

    def viewHistory(self):
        selectionIndexes = self.ui.JavaTableView.selectedIndexes()
        if(len(selectionIndexes) > 0):
            index = selectionIndexes[0]
            id =self.ui.JavaTableView.model().data(index)
            hist = historyForm(self)
            hist.setWindowTitle(id + " \'s History")
            print(id)
            hist.setWindowFlag(True)
            hist.show()
        else:
            print("catch bug")
        

    ## Places the buttons in the table
    def populate_table(self):
        self.dbModel = QSqlTableModel(self)

        
        

        inModel = self.ari.getModel()
        


        
        self.ui.JavaTableView.setModel(inModel)
        self.ui.JavaTableView.resizeColumnsToContents()
        self.ui.JavaTableView.hideColumn(0)
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
