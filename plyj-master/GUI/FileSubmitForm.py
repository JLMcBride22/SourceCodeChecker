import sys
from typing import List
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from UIFiles.GCFileSubGUI import Ui_FileSubForm
#Imported this to connect a button to a function?
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore as qtc
import os
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QDialog, QLabel, QListWidgetItem,QPushButton, QApplication


class FileSubmitForm(qtw.QDialog):
    uiForm = Ui_FileSubForm()
    
    def __init__(self, *args, **kwargs):
        super(FileSubmitForm,self).__init__(*args, **kwargs)
        
        self.uiForm.setupUi(self)
        self.uiForm.removeButton.clicked.connect
        self.connectActions()
        self.setEnabled(True)

    ##Connects the actions to all the buttons in the dialog
    def connectActions(self):
        self.uiForm.addBtn.clicked.connect(self.fileExplorer)
        self.uiForm.removeButton.clicked.connect(self.removeItem)
        return 0
    
    ## Opens file explorer.
    def fileExplorer(self):
        file_filter = 'Java File(*.java)'
        filePaths = QFileDialog.getOpenFileNames(
            parent = self, caption = 'Select a Java File(s)', 
            directory= os.getcwd(), filter=file_filter,
            initialFilter='Java File(*.java)'
        )

        print(filePaths)

        self.uiForm.filePathList.addItems(filePaths.__getitem__(0))

        return 0
        
    def removeItem(self):
        listItems = self.uiForm.filePathList.selectedItems
        if not listItems: return
        for item in listItems:
            self.uiForm.filePathList.takeItem(self.uiForm.filePathList.row(item))



if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)
    widget = FileSubmitForm()
    w = qtw.QWidget()
    
    widget.show()

    sys,exit(app.exec_())
        





