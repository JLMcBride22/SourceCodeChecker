"""
======================================================================================
*
*
* @name:      FileSubmitForm.py
* @author(s): Jonathan Lewis, Isaiah Brooks, James T. Kirkland, Justin McBride
* @date:      12/01/2021
* @purpose:   This file is the window for the file analysis submitter. It creates a
*             dictionary of metrics that the user selects that sends to the ARI.
*             
*             
*
*
=======================================================================================

"""
#from typing import IO
from xml.etree.ElementTree import parse
from PyQt5 import QtWidgets as qtw
# Imported the following to connect a button to a function?
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
import os
from pathlib import Path
from datetime import datetime
from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QCheckBox, QDialogButtonBox, QFileDialog, QListWidgetItem, QMessageBox, QTabWidget, QTableView, QWidget

##Backend interface 
from ARI import ARI
from UIFiles.GCFileSubGUI import Ui_FileSubForm


class FileSubmitForm(qtw.QDialog):
    uiForm = Ui_FileSubForm()

    def __init__(self, *args, **kwargs):
        super(FileSubmitForm, self).__init__(*args, **kwargs)

        self.uiForm.setupUi(self)
        self.dictOfMetrics = {}


        self.connectActions()
        #self.setEnabled(True)
        

    def setARI(self, ariParam: ARI):
        self.ari = ariParam
       
    
    ##Connects the actions to all the buttons in the dialog
    def connectActions(self):
        
        self.uiForm.addBtn.clicked.connect(self.fileExplorer)
        self.uiForm.removeButton.clicked.connect(self.removeItem)
        self.uiForm.pushButton.clicked.connect(self.findDirectory)
        self.uiForm.SubmitFileLink.clicked.connect(self.submit)
        self.uiForm.cancel.clicked.connect(self.close)

        self.uiForm.minVarLenBox.valueChanged.connect(self.compareSpinMinVarLen)
        self.uiForm.maxVarLenBox.valueChanged.connect(self.compareSpinMaxVarLen)
        return 0


    def compareSpinMinVarLen(self):
        min = self.uiForm.minVarLenBox.value()
        max = self.uiForm.maxVarLenBox.value()
        if(min > max):
            self.uiForm.maxVarLenBox.setValue(min)

    def compareSpinMaxVarLen(self):
        min = self.uiForm.minVarLenBox.value()
        max = self.uiForm.maxVarLenBox.value()
        if(min > max):
            self.uiForm.minVarLenBox.setValue(max)
    

    ## Opens file explorer.
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
            dlg.setInformativeText("Please select your file by clicking the \"Add File(s)\" button or add a directory")
            dlg.setIcon(3)
            dlg.exec_()
            return
        else:

            for i in range(0, countPaths):
                
                pathwayItem = self.uiForm.filePathList.item(i)
                pathway = pathwayItem.text()
                



                
                try:
                    
                    open(pathway, 'r')

                    p = Path(pathway)
                    stats = p.stat()
                    time = stats.st_mtime
                    timeStamp = datetime.fromtimestamp(time).strftime('%c')

                    if(self.ari.checkForRedundent(pathway, timeStamp)):
                        qm = QMessageBox()

                        ret  = qm.question(self,'', str(pathway) +"\nThis file has not been changed since last analysis. Are you sure you want to analyze the file again?", qm.Yes | qm.No)


                        if ret == qm.Yes:
                            listPaths.append(pathway)
                        elif ret == qm.No:
                            self.uiForm.filePathList.removeItemWidget(pathwayItem)
                            pathwayItem.setHidden(True)
                             
                    else:
                        listPaths.append(pathway)


                except IOError:
                    dlg = QMessageBox()
                    dlg.setText("Pathway, "+ pathway + " was not found")
                    dlg.setInformativeText("Please remove forementioned path and try again.")
                    dlg.setIcon(3)
                    dlg.exec_()
                    #return
                    

        self.ari.takeFileList(listPaths,self.getMetricsFromBoxes())
            
        uncompiled=self.ari.getUncompiled()
        
        numSuccessAnal = len(listPaths) - len(uncompiled)



        if len(uncompiled) > 0:
            dlg = QMessageBox()
            

            self.uiForm.filePathList.clear()
            self.uiForm.filePathList.addItems(uncompiled)
            ii = 0
            while(ii < len(uncompiled)):
                self.uiForm.filePathList.item(ii).setBackground(QColor('#f0027f'))
                ii += 1

            dlg.setText("Compilation failure:")
            dlg.setInformativeText("The " +str(len(uncompiled))+ " file(s), highlighted in red, failed to compile. The other "+ str(numSuccessAnal) + " file(s) were able to be compiled.")
            dlg.setIcon(2)
            dlg.exec_()
            return

        #All files  were successfully compiled
        else: 
            dlg = QMessageBox()
                
            dlg.setText("Compilation Success:")
            dlg.setInformativeText("ALL "+ str(numSuccessAnal) + " file(s) were able to compile.")
            dlg.setIcon(1)
            dlg.exec_()
            

        self.close()
    
    #This functions returns of a dictionary of strings of the name of the checked boxes.
    def getMetricsFromBoxes(self):
        mts = 0
        while mts < self.uiForm.MeasurementTabs.count():
            w1 = self.uiForm.MeasurementTabs.widget(mts)
            
            for tab in w1.children():
                
                noTab = tab.count()
                tI = 0
                while tI < noTab:
                    w2 = tab.widget(tI)
                
                    listOfObjects =  []
                    for obj in w2.children():
                        
                        if type(obj) is QCheckBox:
                            if(obj.isChecked()):
                                listOfObjects.append(obj.text())
                    self.dictOfMetrics [w2.objectName()] = listOfObjects
                    tI += 1
                



            
            mts+=1
                
        
        return self.dictOfMetrics
        

    

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


        

    
        

        
