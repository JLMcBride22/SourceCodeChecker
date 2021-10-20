
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon

from UIFiles.GCMainWindowGUI import Ui_MainWindow
from PyQt5 import QtCore as qtc
import os
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QDialog, QLabel,QPushButton




class MainWindow(qtw.QMainWindow):
    ui = Ui_MainWindow()
    excelBtnDict = {}
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        
        self.ui.setupUi(self)
        self.ui.actionInstruction.associatedGraphicsWidgets

        ## Adds the function to the button.
        self.ui.SubmitFileLink.clicked.connect(self.uploadSingleFile)
        self.ui.actionInstruction.triggered.connect(self.openHelp)
        self.ui.javaFileTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.populate_table()


    #Uploads a single java file to the parser.
    def uploadSingleFile(self):

        file_filter = 'Java File(*.java)'
        filePath = QFileDialog.getOpenFileName(
            parent = self, caption = 'Select a Java File', 
            directory= os.getcwd(), filter=file_filter,
            initialFilter='Java File(*.java)'
        )

        print(filePath[0])
    
    #Opens the dialog for help
    def openHelp(self):
        dlg = QDialog()
        dlg.setWindowTitle("Help")
        label = QLabel(dlg)
        label.setText("Help\n instructions: \nThis program does shit. Figure it out for yourself")
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def populate_table(self):
        
        for index in range (0, 2):
            btnExcel = QPushButton(self)
            btnExcel.setIcon(QIcon("GUI\icons\excel.jfif"))
            
            self.ui.javaFileTable.setIndexWidget(self.ui.javaFileTable.model().index(index, 7), btnExcel)
        


if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)
    widget = MainWindow()
    w = qtw.QMainWindow()
    
    widget.show()

    sys,exit(app.exec_())
    




        

