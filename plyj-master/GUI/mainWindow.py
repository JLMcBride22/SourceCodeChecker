import sys

sys.path.append("./GUI")

from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QIcon
from FileSubmitForm import FileSubmitForm
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

        ## Adds the function to the button/menu options.
        ##self.ui.SubmitFileLink.clicked.connect(self.uploadSingleFile)
        self.ui.actionInstruction.triggered.connect(self.openHelp)
        self.ui.actionSingle_file.triggered.connect(self.uploadFile_s)
        self.ui.javaFileTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.populate_table()

    def setARI(self, ariPARAM: ARI):
        self.ari = ariPARAM

    # Opens the dialog for help
    def openHelp(self):
        dlg = QDialog()
        dlg.setWindowTitle("Help")
        label = QLabel(dlg)
        label.setText("Help\n instructions: \nThis program does stuff. Figure it out for yourself")
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    #Opens the upload file screen.
    def uploadFile_s(self):
        fileSubmit = FileSubmitForm(self)
        fileSubmit.setARI(self.ari)
        fileSubmit.setAutoFillBackground(True)

        

        fileSubmit.show()

    ## Places the buttons in the table
    def populate_table(self):
        for index in range(0, 2):
            btnExcel = QToolButton(self)
            

            self.ui.javaFileTable.setIndexWidget(self.ui.javaFileTable.model().index(index, 7), btnExcel)


if __name__ == '__main__':
    import sys

    app = qtw.QApplication(sys.argv)
    widget = MainWindow()
    widget.__init__()
    w = qtw.QMainWindow()

    widget.show()

    sys, exit(app.exec_())
