# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoryForm(object):
    def setupUi(self, HistoryForm):
        HistoryForm.setObjectName("HistoryForm")
        HistoryForm.setWindowModality(QtCore.Qt.WindowModal)
        HistoryForm.resize(740, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HistoryForm.sizePolicy().hasHeightForWidth())
        HistoryForm.setSizePolicy(sizePolicy)
        HistoryForm.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        HistoryForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        HistoryForm.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(HistoryForm)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(HistoryForm)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(HistoryForm)
        QtCore.QMetaObject.connectSlotsByName(HistoryForm)

    def retranslateUi(self, HistoryForm):
        _translate = QtCore.QCoreApplication.translate
        HistoryForm.setWindowTitle(_translate("HistoryForm", "Submit your .java file(s)"))
        HistoryForm.setToolTip(_translate("HistoryForm", "Please enter open your files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoryForm = QtWidgets.QWidget()
    ui = Ui_HistoryForm()
    ui.setupUi(HistoryForm)
    HistoryForm.show()
    sys.exit(app.exec_())
