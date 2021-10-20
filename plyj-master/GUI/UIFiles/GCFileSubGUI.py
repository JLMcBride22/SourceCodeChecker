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
        FileSubForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileSubForm.setWindowFilePath("")
        self.lineEdit = QtWidgets.QLineEdit(FileSubForm)
        self.lineEdit.setGeometry(QtCore.QRect(440, 210, 211, 131))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferLatin)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(FileSubForm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 200, 381, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.maxVarLenBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.maxVarLenBox.setMinimum(5)
        self.maxVarLenBox.setMaximum(20)
        self.maxVarLenBox.setObjectName("maxVarLenBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maxVarLenBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.mcAbeBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.mcAbeBox.setMinimum(1)
        self.mcAbeBox.setMaximum(40)
        self.mcAbeBox.setObjectName("mcAbeBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mcAbeBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.nestLevBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.nestLevBox.setMinimum(1)
        self.nestLevBox.setMaximum(25)
        self.nestLevBox.setDisplayIntegerBase(10)
        self.nestLevBox.setObjectName("nestLevBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nestLevBox)
        self.recursionBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.recursionBox.setObjectName("recursionBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.recursionBox)
        self.noGotoBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.noGotoBox.setObjectName("noGotoBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.noGotoBox)
        self.minVarLenBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.minVarLenBox.setMinimum(3)
        self.minVarLenBox.setMaximum(20)
        self.minVarLenBox.setObjectName("minVarLenBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.minVarLenBox)
        self.SubmitFileLink = QtWidgets.QCommandLinkButton(FileSubForm)
        self.SubmitFileLink.setGeometry(QtCore.QRect(420, 360, 131, 41))
        self.SubmitFileLink.setObjectName("SubmitFileLink")
        self.filePathList = QtWidgets.QListWidget(FileSubForm)
        self.filePathList.setGeometry(QtCore.QRect(20, 20, 651, 161))
        self.filePathList.setResizeMode(QtWidgets.QListView.Adjust)
        self.filePathList.setObjectName("filePathList")
        self.addBtn = QtWidgets.QPushButton(FileSubForm)
        self.addBtn.setGeometry(QtCore.QRect(510, 180, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.removeButton = QtWidgets.QPushButton(FileSubForm)
        self.removeButton.setGeometry(QtCore.QRect(590, 180, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.SubmitFileLink_2 = QtWidgets.QCommandLinkButton(FileSubForm)
        self.SubmitFileLink_2.setGeometry(QtCore.QRect(560, 360, 131, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icons/red_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SubmitFileLink_2.setIcon(icon)
        self.SubmitFileLink_2.setObjectName("SubmitFileLink_2")

        self.retranslateUi(FileSubForm)
        QtCore.QMetaObject.connectSlotsByName(FileSubForm)

    def retranslateUi(self, FileSubForm):
        _translate = QtCore.QCoreApplication.translate
        FileSubForm.setWindowTitle(_translate("FileSubForm", "Submit your .java file(s)"))
        FileSubForm.setToolTip(_translate("FileSubForm", "Please enter open your files"))
        self.lineEdit.setPlaceholderText(_translate("FileSubForm", "@Filename,@Author, @Description"))
        self.label_3.setText(_translate("FileSubForm", "Mininum Variable Length "))
        self.label.setText(_translate("FileSubForm", "MaximumVariable Length "))
        self.label_4.setText(_translate("FileSubForm", "McCabe Complexity"))
        self.label_5.setText(_translate("FileSubForm", "Nesting Level"))
        self.recursionBox.setText(_translate("FileSubForm", "Allow Recursion"))
        self.noGotoBox.setText(_translate("FileSubForm", "No Goto\'s"))
        self.SubmitFileLink.setText(_translate("FileSubForm", "Submit Files"))
        self.addBtn.setText(_translate("FileSubForm", "ADD"))
        self.removeButton.setText(_translate("FileSubForm", "REMOVE"))
        self.SubmitFileLink_2.setText(_translate("FileSubForm", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileSubForm = QtWidgets.QWidget()
    ui = Ui_FileSubForm()
    ui.setupUi(FileSubForm)
    FileSubForm.show()
    sys.exit(app.exec_())
