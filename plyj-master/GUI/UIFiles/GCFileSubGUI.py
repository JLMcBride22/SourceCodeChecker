# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSubmitter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileSubForm(object):
    def setupUi(self, FileSubForm):
        FileSubForm.setObjectName("FileSubForm")
        FileSubForm.setWindowModality(QtCore.Qt.WindowModal)
        FileSubForm.resize(680, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileSubForm.sizePolicy().hasHeightForWidth())
        FileSubForm.setSizePolicy(sizePolicy)
        FileSubForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileSubForm.setWindowFilePath("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FileSubForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(FileSubForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(FileSubForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.maxVarLenBox = QtWidgets.QSpinBox(FileSubForm)
        self.maxVarLenBox.setMinimum(5)
        self.maxVarLenBox.setMaximum(20)
        self.maxVarLenBox.setObjectName("maxVarLenBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maxVarLenBox)
        self.label_4 = QtWidgets.QLabel(FileSubForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.mcAbeBox = QtWidgets.QSpinBox(FileSubForm)
        self.mcAbeBox.setMinimum(1)
        self.mcAbeBox.setMaximum(40)
        self.mcAbeBox.setObjectName("mcAbeBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mcAbeBox)
        self.label_5 = QtWidgets.QLabel(FileSubForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.nestLevBox = QtWidgets.QSpinBox(FileSubForm)
        self.nestLevBox.setMinimum(1)
        self.nestLevBox.setMaximum(25)
        self.nestLevBox.setDisplayIntegerBase(10)
        self.nestLevBox.setObjectName("nestLevBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nestLevBox)
        self.recursionBox = QtWidgets.QCheckBox(FileSubForm)
        self.recursionBox.setObjectName("recursionBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.recursionBox)
        self.noGotoBox = QtWidgets.QCheckBox(FileSubForm)
        self.noGotoBox.setObjectName("noGotoBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.noGotoBox)
        self.minVarLenBox = QtWidgets.QSpinBox(FileSubForm)
        self.minVarLenBox.setMinimum(3)
        self.minVarLenBox.setMaximum(20)
        self.minVarLenBox.setObjectName("minVarLenBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.minVarLenBox)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 2, 1)
        self.filePathList = QtWidgets.QListWidget(FileSubForm)
        self.filePathList.setResizeMode(QtWidgets.QListView.Adjust)
        self.filePathList.setObjectName("filePathList")
        self.gridLayout.addWidget(self.filePathList, 0, 0, 1, 5)
        self.removeButton = QtWidgets.QPushButton(FileSubForm)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 4, 1, 1)
        self.cancel = QtWidgets.QCommandLinkButton(FileSubForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icons/red_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 3, 3, 1, 2)
        self.addBtn = QtWidgets.QPushButton(FileSubForm)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 1, 3, 1, 1)
        self.SubmitFileLink = QtWidgets.QCommandLinkButton(FileSubForm)
        self.SubmitFileLink.setObjectName("SubmitFileLink")
        self.gridLayout.addWidget(self.SubmitFileLink, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(FileSubForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 100))
        self.lineEdit.setInputMethodHints(
            QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhPreferLatin)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 2, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(FileSubForm)
        QtCore.QMetaObject.connectSlotsByName(FileSubForm)

    def retranslateUi(self, FileSubForm):
        _translate = QtCore.QCoreApplication.translate
        FileSubForm.setWindowTitle(_translate("FileSubForm", "Submit your .java file(s)"))
        FileSubForm.setToolTip(_translate("FileSubForm", "Please enter open your files"))
        self.label_3.setText(_translate("FileSubForm", "Mininum Variable Length "))
        self.label.setText(_translate("FileSubForm", "MaximumVariable Length "))
        self.label_4.setText(_translate("FileSubForm", "McCabe Complexity"))
        self.label_5.setText(_translate("FileSubForm", "Nesting Level"))
        self.recursionBox.setText(_translate("FileSubForm", "Allow Recursion"))
        self.noGotoBox.setText(_translate("FileSubForm", "No Goto\'s"))
        self.removeButton.setText(_translate("FileSubForm", "REMOVE"))
        self.cancel.setText(_translate("FileSubForm", "Cancel"))
        self.addBtn.setText(_translate("FileSubForm", "ADD"))
        self.SubmitFileLink.setText(_translate("FileSubForm", "Submit Files"))
        self.lineEdit.setPlaceholderText(_translate("FileSubForm", "@Filename,@Author, @Description"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FileSubForm = QtWidgets.QWidget()
    ui = Ui_FileSubForm()
    ui.setupUi(FileSubForm)
    FileSubForm.show()
    sys.exit(app.exec_())
