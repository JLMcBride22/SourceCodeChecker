from typing import IO
from xml.etree.ElementTree import parse
from PyQt5 import QtWidgets as qtw
# Imported the following to connect a button to a function?
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
import os
from pathlib import Path

from PyQt5.QtWidgets import QDialogButtonBox, QFileDialog, QListWidgetItem, QMessageBox, QTableView

##Backend interface 
from ARI import ARI
from UIFiles.GCFileSubGUI import Ui_FileSubForm


class FileSubmitForm(qtw.QDialog):
    uiForm = Ui_FileSubForm()

    def __init__(self, *args, **kwargs):
        super(FileSubmitForm, self).__init__(*args, **kwargs)

        self.uiForm.setupUi(self)
        self.listOfCheckedMetrics =[]
        
        self.connectActions()
        #self.setEnabled(True)
        

    def setARI(self, ariParam: ARI):
        self.ari = ariParam
       
    
    ##Connects the actions to all the buttons in the dialog
    def connectActions(self):
        ## Add remove.
        self.uiForm.addBtn.clicked.connect(self.fileExplorer)
        self.uiForm.removeButton.clicked.connect(self.removeItem)
        self.uiForm.pushButton.clicked.connect(self.findDirectory)
        self.uiForm.SubmitFileLink.clicked.connect(self.submit)
        self.uiForm.cancel.clicked.connect(self.close)
        return 0

    ## Opens file explorer.
    #TODO We need to add an settings function that gives the user selects its on default directory!
    def fileExplorer(self):
        file_filter = 'Java File(*.java)'
        filePaths = QFileDialog.getOpenFileNames(
            parent=self, caption='Select a Java File(s)',
            directory="JavaTest", filter=file_filter,
            initialFilter='Java File(*.java)'
        )

        

        self.uiForm.filePathList.addItems(filePaths.__getitem__(0))

        return 0
    
    # This function removes only one item.
    def removeItem(self):
        self.uiForm.filePathList.takeItem(self.uiForm.filePathList.currentRow())

    # The following submits the list.
    def submit(self):
        countPaths = self.uiForm.filePathList.count()
        listPaths = []
        if countPaths == 0:
            dlg = QMessageBox()
            dlg.setText("You haven't selected any files")
            dlg.setInformativeText("Please select your file by clicking the \"Add File(s)\" button")
            dlg.setIcon(3)
            dlg.exec_()
            return
        else:
            for i in range(0, countPaths):
                
                pathway = self.uiForm.filePathList.item(i).text()
                
                try:
                    open(pathway, 'r')
                    listPaths.append(pathway)

                except IOError:
                    dlg = QMessageBox()
                    dlg.setText("Pathway, "+ pathway + " was not found")
                    dlg.setInformativeText("Please remove forementioned path and try again.")
                    dlg.setIcon(3)
                    dlg.exec_()
                    return
                    

        self.ari.takeFileList(listPaths,self.getMetricsFromBoxes())
            
        uncompiled=self.ari.getUncompiled()
        
        for uc in uncompiled:
            dlg = QMessageBox()
            
            dlg.setText("Pathway, "+ str(uc) + ", wasn't abled to be compiled")
            dlg.setInformativeText("The others were able to be added unless noted")
            dlg.setIcon(3)
            dlg.exec_()
            
        
        self.close()
    
    #This functions returns of a list of strings of the name of checked boxes
    def getMetricsFromBoxes(self):
        boxes = self.uiForm.buttonGroup.buttons()
        
        for box in boxes:
            if box.isChecked():
                self.listOfCheckedMetrics.append(box.text())
                print("\t\t\telif metric == "+"\"" +box.text()+"\"" + ":\n\t\t\t\tpass")
        return self.listOfCheckedMetrics

    #This method finds and recurses a directory adding it to the Qwidget list
    def findDirectory(self):
            
            #TODO add
            dir= QFileDialog.getExistingDirectory(self, "Choose your directory",
            'C:/Users/Jonathan Lewis/IdeaProjects'
            )
            listPath = []
            if dir != '':
                for path in Path(dir).rglob("*.java"):
                    resolvePathStr = str(path.resolve)
                    listResolvePath = resolvePathStr.split("\'")
                    
                    listPath.append(str(listResolvePath[1]))

                self.uiForm.filePathList.addItems(listPath)



# Testing purposes
if __name__ == '__main__':
    dir = 'C:\\Users\\Jonathan Lewis\\IdeaProjects'
    listPath = []
    for path in Path(dir).rglob("*.java"):
        resolvePathStr = str(path.resolve)
        listResolvePath = resolvePathStr.split("\'")


        

    
        

        
