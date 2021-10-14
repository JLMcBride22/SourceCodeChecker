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
        MainWindow.resize(733, 608)
        MainWindow.setMaximumSize(QtCore.QSize(99999, 9999))
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhTime)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.javaFileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.javaFileTable.setGeometry(QtCore.QRect(0, 30, 731, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.javaFileTable.sizePolicy().hasHeightForWidth())
        self.javaFileTable.setSizePolicy(sizePolicy)
        self.javaFileTable.setMouseTracking(True)
        self.javaFileTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.javaFileTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.javaFileTable.setDragDropOverwriteMode(False)
        self.javaFileTable.setAlternatingRowColors(True)
        self.javaFileTable.setGridStyle(QtCore.Qt.SolidLine)
        self.javaFileTable.setRowCount(6)
        self.javaFileTable.setObjectName("javaFileTable")
        self.javaFileTable.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.javaFileTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.javaFileTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.javaFileTable.setItem(1, 6, item)
        self.javaFileTable.horizontalHeader().setCascadingSectionResizes(True)
        self.javaFileTable.verticalHeader().setCascadingSectionResizes(False)
        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchBar.setGeometry(QtCore.QRect(0, 10, 113, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy)
        self.SearchBar.setObjectName("SearchBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 300, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 330, 281, 151))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferLatin)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 510, 81, 16))
        self.label_2.setObjectName("label_2")
        self.SubmitFileLink = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.SubmitFileLink.setGeometry(QtCore.QRect(250, 520, 185, 41))
        self.SubmitFileLink.setObjectName("SubmitFileLink")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 320, 371, 171))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.minVarLenBox = QtWidgets.QSpinBox(self.widget)
        self.minVarLenBox.setObjectName("minVarLenBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minVarLenBox)
        self.recursionBox = QtWidgets.QCheckBox(self.widget)
        self.recursionBox.setObjectName("recursionBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.recursionBox)
        self.noGotoBox = QtWidgets.QCheckBox(self.widget)
        self.noGotoBox.setObjectName("noGotoBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.noGotoBox)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.maxVarLenBox = QtWidgets.QSpinBox(self.widget)
        self.maxVarLenBox.setObjectName("maxVarLenBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.maxVarLenBox)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.mcAbeBox = QtWidgets.QSpinBox(self.widget)
        self.mcAbeBox.setObjectName("mcAbeBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.mcAbeBox)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.nestLevBox = QtWidgets.QSpinBox(self.widget)
        self.nestLevBox.setObjectName("nestLevBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nestLevBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew_File = QtWidgets.QMenu(self.menuFile)
        self.menuNew_File.setObjectName("menuNew_File")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
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
        self.menuNew_File.addSeparator()
        self.menuNew_File.addAction(self.actionSingle_file)
        self.menuFile.addAction(self.menuNew_File.menuAction())
        self.menuFile.addAction(self.actionExport_File)
        self.menuHelp.addAction(self.actionInstruction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SourceCodeChecker"))
        self.javaFileTable.setSortingEnabled(True)
        item = self.javaFileTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.javaFileTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Change"))
        item = self.javaFileTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "No. of Lines"))
        item = self.javaFileTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        item = self.javaFileTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "No.  of Changes"))
        item = self.javaFileTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nesting Level"))
        item = self.javaFileTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "McCabe"))
        __sortingEnabled = self.javaFileTable.isSortingEnabled()
        self.javaFileTable.setSortingEnabled(False)
        item = self.javaFileTable.item(0, 0)
        item.setText(_translate("MainWindow", "HelloWorld.java"))
        item = self.javaFileTable.item(0, 1)
        item.setText(_translate("MainWindow", "9/19/2021 11:16 PM"))
        item = self.javaFileTable.item(0, 2)
        item.setText(_translate("MainWindow", "55"))
        item = self.javaFileTable.item(0, 3)
        item.setText(_translate("MainWindow", "15 MB"))
        item = self.javaFileTable.item(0, 4)
        item.setText(_translate("MainWindow", "5"))
        item = self.javaFileTable.item(0, 5)
        item.setText(_translate("MainWindow", "4"))
        item = self.javaFileTable.item(0, 6)
        item.setText(_translate("MainWindow", "21"))
        item = self.javaFileTable.item(1, 0)
        item.setText(_translate("MainWindow", "Main.java"))
        item = self.javaFileTable.item(1, 1)
        item.setText(_translate("MainWindow", "9/20/2021 01:35 AM"))
        item = self.javaFileTable.item(1, 2)
        item.setText(_translate("MainWindow", "500"))
        item = self.javaFileTable.item(1, 3)
        item.setText(_translate("MainWindow", "65 MB"))
        item = self.javaFileTable.item(1, 4)
        item.setText(_translate("MainWindow", "12"))
        item = self.javaFileTable.item(1, 5)
        item.setText(_translate("MainWindow", "3"))
        item = self.javaFileTable.item(1, 6)
        item.setText(_translate("MainWindow", "14"))
        self.javaFileTable.setSortingEnabled(__sortingEnabled)
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "@Filename,@Author, @Description"))
        self.label_2.setText(_translate("MainWindow", "Preamble"))
        self.SubmitFileLink.setText(_translate("MainWindow", "Submit File/Directory"))
        self.label.setText(_translate("MainWindow", "MaximumVariable Length "))
        self.recursionBox.setText(_translate("MainWindow", "Allow Recursion"))
        self.noGotoBox.setText(_translate("MainWindow", "No Goto\'s"))
        self.label_3.setText(_translate("MainWindow", "Mininum Variable Length "))
        self.label_4.setText(_translate("MainWindow", "McCabe Complexity"))
        self.label_5.setText(_translate("MainWindow", "Nesting Level"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew_File.setTitle(_translate("MainWindow", "New File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport_File.setText(_translate("MainWindow", "Export to Excel"))
        self.actionSingle_file.setText(_translate("MainWindow", "Single file"))
        self.actionInstruction.setText(_translate("MainWindow", "Instruction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())