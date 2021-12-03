# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUItake2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(858, 608)
        MainWindow.setMaximumSize(QtCore.QSize(99999, 9999))
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhTime)
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SearchBar = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy)
        self.SearchBar.setObjectName("SearchBar")
        self.horizontalLayout.addWidget(self.SearchBar)
        self.addFilesButton = QtWidgets.QPushButton(self.groupBox)
        self.addFilesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFilesButton.sizePolicy().hasHeightForWidth())
        self.addFilesButton.setSizePolicy(sizePolicy)
        self.addFilesButton.setObjectName("addFilesButton")
        self.horizontalLayout.addWidget(self.addFilesButton)
        self.refreshAllButton = QtWidgets.QPushButton(self.groupBox)
        self.refreshAllButton.setObjectName("refreshAllButton")
        self.horizontalLayout.addWidget(self.refreshAllButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.JavaTableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JavaTableView.setFont(font)
        self.JavaTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.JavaTableView.setAlternatingRowColors(True)
        self.JavaTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.JavaTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.JavaTableView.setObjectName("JavaTableView")
        self.gridLayout.addWidget(self.JavaTableView, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setAccessibleDescription("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew_File = QtWidgets.QMenu(self.menuFile)
        self.menuNew_File.setObjectName("menuNew_File")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_File = QtWidgets.QAction(MainWindow)
        self.actionExport_File.setObjectName("actionExport_File")
        self.actionSingle_file = QtWidgets.QAction(MainWindow)
        self.actionSingle_file.setObjectName("actionSingle_file")
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        self.actionInstruction.setCheckable(False)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionDirectory = QtWidgets.QAction(MainWindow)
        self.actionDirectory.setObjectName("actionDirectory")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.menuNew_File.addSeparator()
        self.menuNew_File.addAction(self.actionSingle_file)
        self.menuNew_File.addAction(self.actionDirectory)
        self.menuFile.addAction(self.menuNew_File.menuAction())
        self.menuFile.addAction(self.actionExport_File)
        self.menuHelp.addAction(self.actionInstruction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SourceCodeChecker"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.addFilesButton.setText(_translate("MainWindow", "Add Files"))
        self.refreshAllButton.setText(_translate("MainWindow", "Refresh All"))
        self.label.setText(_translate("MainWindow", "The database is empty."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew_File.setTitle(_translate("MainWindow", "New File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport_File.setText(_translate("MainWindow", "Export to Spreadsheet"))
        self.actionSingle_file.setText(_translate("MainWindow", "Single file"))
        self.actionInstruction.setText(_translate("MainWindow", "Instruction"))
        self.actionDirectory.setText(_translate("MainWindow", "Directory"))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
