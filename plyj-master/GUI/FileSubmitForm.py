from PyQt5 import QtWidgets as qtw
# Imported the following to connect a button to a function?
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
import os

from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem

##Backend interface import
from ARI import ARI
from UIFiles.GCFileSubGUI import Ui_FileSubForm


class FileSubmitForm(qtw.QDialog):
    uiForm = Ui_FileSubForm()

    def __init__(self, *args, **kwargs):
        super(FileSubmitForm, self).__init__(*args, **kwargs)

        self.uiForm.setupUi(self)
        self.uiForm.removeButton.clicked.connect
        self.connectActions()
        self.setEnabled(True)

    def setARI(self, ariParam: ARI):
        self.ari = ariParam

    ##Connects the actions to all the buttons in the dialog
    def connectActions(self):
        ## Add remove.
        self.uiForm.addBtn.clicked.connect(self.fileExplorer)
        self.uiForm.removeButton.clicked.connect(self.removeItem)

        self.uiForm.SubmitFileLink.clicked.connect(self.submit)
        self.uiForm.cancel.clicked.connect(self.close)
        return 0

    ## Opens file explorer.
    def fileExplorer(self):
        file_filter = 'Java File(*.java)'
        filePaths = QFileDialog.getOpenFileNames(
            parent=self, caption='Select a Java File(s)',
            directory=os.getcwd(), filter=file_filter,
            initialFilter='Java File(*.java)'
        )

        ##print(filePaths)

        self.uiForm.filePathList.addItems(filePaths.__getitem__(0))

        return 0

    # This function removes only one item.
    def removeItem(self):
        self.uiForm.filePathList.takeItem(self.uiForm.filePathList.currentRow())

    # The following
    def submit(self):
        countPaths = self.uiForm.filePathList.count()
        listPaths = []
        item: QListWidgetItem
        for i in range(0, countPaths):
            item = self.uiForm.filePathList.item(i)
            listPaths.append(item.text())

        
        self.ari.takeFileList(listPaths)
        self.close()

        return


# Testing purposes
if __name__ == '__main__':
    import sys

    a = ARI()
    app = qtw.QApplication(sys.argv)
    widget = FileSubmitForm()
    widget.setARI(a)
    w = qtw.QWidget()

    widget.show()

    sys, exit(app.exec_())
