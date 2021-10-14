
from PyQt5 import QtWidgets as qtw

from UIFiles.GCMainWindowGUI import Ui_MainWindow
from PyQt5 import QtCore as qtc
import os
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QDialog, QLabel




class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.actionInstruction.associatedGraphicsWidgets

        ## Adds the function to the button.
        ui.SubmitFileLink.clicked.connect(self.uploadSingleFile)
        ui.actionInstruction.triggered.connect(self.openHelp)
        ui.javaFileTable.setSelectionBehavior(QAbstractItemView.SelectRows)


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
        label.setText("Help\n instructions: \nThis program does shit. Figure it out for you self")
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()


if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)
    widget = MainWindow()
    w = qtw.QMainWindow()
    
    widget.show()

    sys,exit(app.exec_())
    




        

