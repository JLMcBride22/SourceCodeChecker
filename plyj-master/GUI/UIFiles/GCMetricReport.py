# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MetricReport.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(717, 491)
        Form.setAutoFillBackground(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "")
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_4.addWidget(self.toolButton, 1, 0, 1, 1, QtCore.Qt.AlignRight)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Metric Reports"))
        self.label.setText(_translate("Form", "Navigation tree"))
        self.toolButton.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
