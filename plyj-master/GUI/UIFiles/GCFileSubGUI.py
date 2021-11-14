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
        FileSubForm.setWindowModality(QtCore.Qt.NonModal)
        FileSubForm.resize(660, 624)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileSubForm.sizePolicy().hasHeightForWidth())
        FileSubForm.setSizePolicy(sizePolicy)
        FileSubForm.setMaximumSize(QtCore.QSize(1000, 850))
        FileSubForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileSubForm.setWindowFilePath("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FileSubForm)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(FileSubForm)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.filePathList = QtWidgets.QListWidget(FileSubForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathList.sizePolicy().hasHeightForWidth())
        self.filePathList.setSizePolicy(sizePolicy)
        self.filePathList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filePathList.setAlternatingRowColors(True)
        self.filePathList.setResizeMode(QtWidgets.QListView.Adjust)
        self.filePathList.setObjectName("filePathList")
        self.verticalLayout.addWidget(self.filePathList)
        self.addBtn = QtWidgets.QPushButton(FileSubForm)
        self.addBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy)
        self.addBtn.setMinimumSize(QtCore.QSize(84, 0))
        self.addBtn.setAutoFillBackground(False)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.pushButton = QtWidgets.QPushButton(FileSubForm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.removeButton = QtWidgets.QPushButton(FileSubForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.MeasurementTabs = QtWidgets.QTabWidget(FileSubForm)
        self.MeasurementTabs.setObjectName("MeasurementTabs")
        self.MeasurementTab = QtWidgets.QWidget()
        self.MeasurementTab.setObjectName("MeasurementTab")
        self.InnerTab = QtWidgets.QTabWidget(self.MeasurementTab)
        self.InnerTab.setGeometry(QtCore.QRect(-10, 0, 641, 177))
        self.InnerTab.setToolTip("")
        self.InnerTab.setObjectName("InnerTab")
        self.SizeTab = QtWidgets.QWidget()
        self.SizeTab.setObjectName("SizeTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.SizeTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SLOCwCBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SLOCwCBox.setAcceptDrops(False)
        self.SLOCwCBox.setAutoFillBackground(False)
        self.SLOCwCBox.setChecked(True)
        self.SLOCwCBox.setObjectName("SLOCwCBox")
        self.buttonGroup = QtWidgets.QButtonGroup(FileSubForm)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.SLOCwCBox)
        self.gridLayout_5.addWidget(self.SLOCwCBox, 0, 0, 1, 1)
        self.SemicolonBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SemicolonBox.setChecked(True)
        self.SemicolonBox.setObjectName("SemicolonBox")
        self.buttonGroup.addButton(self.SemicolonBox)
        self.gridLayout_5.addWidget(self.SemicolonBox, 0, 1, 1, 1)
        self.SLOCwoCBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SLOCwoCBox.setChecked(True)
        self.SLOCwoCBox.setObjectName("SLOCwoCBox")
        self.buttonGroup.addButton(self.SLOCwoCBox)
        self.gridLayout_5.addWidget(self.SLOCwoCBox, 1, 0, 1, 1)
        self.FunctionCallBox = QtWidgets.QCheckBox(self.SizeTab)
        self.FunctionCallBox.setChecked(True)
        self.FunctionCallBox.setObjectName("FunctionCallBox")
        self.buttonGroup.addButton(self.FunctionCallBox)
        self.gridLayout_5.addWidget(self.FunctionCallBox, 1, 1, 1, 1)
        self.BlankLineBox = QtWidgets.QCheckBox(self.SizeTab)
        self.BlankLineBox.setChecked(True)
        self.BlankLineBox.setObjectName("BlankLineBox")
        self.buttonGroup.addButton(self.BlankLineBox)
        self.gridLayout_5.addWidget(self.BlankLineBox, 2, 0, 1, 1)
        self.CommentLinesBox = QtWidgets.QCheckBox(self.SizeTab)
        self.CommentLinesBox.setChecked(True)
        self.CommentLinesBox.setObjectName("CommentLinesBox")
        self.buttonGroup.addButton(self.CommentLinesBox)
        self.gridLayout_5.addWidget(self.CommentLinesBox, 3, 0, 1, 1)
        self.InnerTab.addTab(self.SizeTab, "")
        self.ComplexityTab = QtWidgets.QWidget()
        self.ComplexityTab.setObjectName("ComplexityTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ComplexityTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PassedParamBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.PassedParamBox.setChecked(True)
        self.PassedParamBox.setObjectName("PassedParamBox")
        self.buttonGroup.addButton(self.PassedParamBox)
        self.gridLayout_4.addWidget(self.PassedParamBox, 0, 0, 1, 1)
        self.SwitchComplexityBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.SwitchComplexityBox.setEnabled(True)
        self.SwitchComplexityBox.setChecked(True)
        self.SwitchComplexityBox.setTristate(False)
        self.SwitchComplexityBox.setObjectName("SwitchComplexityBox")
        self.buttonGroup.addButton(self.SwitchComplexityBox)
        self.gridLayout_4.addWidget(self.SwitchComplexityBox, 0, 1, 1, 1)
        self.McCabeCompBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.McCabeCompBox.setChecked(True)
        self.McCabeCompBox.setObjectName("McCabeCompBox")
        self.buttonGroup.addButton(self.McCabeCompBox)
        self.gridLayout_4.addWidget(self.McCabeCompBox, 1, 0, 1, 1)
        self.MaxNestingBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.MaxNestingBox.setChecked(True)
        self.MaxNestingBox.setObjectName("MaxNestingBox")
        self.buttonGroup.addButton(self.MaxNestingBox)
        self.gridLayout_4.addWidget(self.MaxNestingBox, 3, 0, 1, 2)
        self.ESLOCatMaxNestBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.ESLOCatMaxNestBox.setChecked(True)
        self.ESLOCatMaxNestBox.setObjectName("ESLOCatMaxNestBox")
        self.buttonGroup.addButton(self.ESLOCatMaxNestBox)
        self.gridLayout_4.addWidget(self.ESLOCatMaxNestBox, 1, 1, 1, 1)
        self.HalsteadCompBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.HalsteadCompBox.setChecked(True)
        self.HalsteadCompBox.setObjectName("HalsteadCompBox")
        self.buttonGroup.addButton(self.HalsteadCompBox)
        self.gridLayout_4.addWidget(self.HalsteadCompBox, 2, 0, 1, 1)
        self.InnerTab.addTab(self.ComplexityTab, "")
        self.LoopTab = QtWidgets.QWidget()
        self.LoopTab.setObjectName("LoopTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LoopTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ForLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.ForLoopBox.setChecked(True)
        self.ForLoopBox.setObjectName("ForLoopBox")
        self.buttonGroup.addButton(self.ForLoopBox)
        self.gridLayout_3.addWidget(self.ForLoopBox, 0, 0, 1, 1)
        self.WhileLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.WhileLoopBox.setChecked(True)
        self.WhileLoopBox.setObjectName("WhileLoopBox")
        self.buttonGroup.addButton(self.WhileLoopBox)
        self.gridLayout_3.addWidget(self.WhileLoopBox, 1, 0, 1, 1)
        self.DoWhileLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.DoWhileLoopBox.setChecked(True)
        self.DoWhileLoopBox.setObjectName("DoWhileLoopBox")
        self.buttonGroup.addButton(self.DoWhileLoopBox)
        self.gridLayout_3.addWidget(self.DoWhileLoopBox, 2, 0, 1, 1)
        self.InnerTab.addTab(self.LoopTab, "")
        self.VariableTab = QtWidgets.QWidget()
        self.VariableTab.setObjectName("VariableTab")
        self.gridLayout = QtWidgets.QGridLayout(self.VariableTab)
        self.gridLayout.setObjectName("gridLayout")
        self.UserDefBox = QtWidgets.QCheckBox(self.VariableTab)
        self.UserDefBox.setChecked(True)
        self.UserDefBox.setObjectName("UserDefBox")
        self.buttonGroup.addButton(self.UserDefBox)
        self.gridLayout.addWidget(self.UserDefBox, 0, 1, 1, 1)
        self.TotalVarBox = QtWidgets.QCheckBox(self.VariableTab)
        self.TotalVarBox.setChecked(True)
        self.TotalVarBox.setObjectName("TotalVarBox")
        self.buttonGroup.addButton(self.TotalVarBox)
        self.gridLayout.addWidget(self.TotalVarBox, 1, 0, 1, 1)
        self.FloatBox = QtWidgets.QCheckBox(self.VariableTab)
        self.FloatBox.setChecked(True)
        self.FloatBox.setObjectName("FloatBox")
        self.buttonGroup.addButton(self.FloatBox)
        self.gridLayout.addWidget(self.FloatBox, 4, 0, 1, 1)
        self.ArrayBox = QtWidgets.QCheckBox(self.VariableTab)
        self.ArrayBox.setChecked(True)
        self.ArrayBox.setObjectName("ArrayBox")
        self.buttonGroup.addButton(self.ArrayBox)
        self.gridLayout.addWidget(self.ArrayBox, 6, 0, 1, 1)
        self.IntegerBox = QtWidgets.QCheckBox(self.VariableTab)
        self.IntegerBox.setChecked(True)
        self.IntegerBox.setObjectName("IntegerBox")
        self.buttonGroup.addButton(self.IntegerBox)
        self.gridLayout.addWidget(self.IntegerBox, 3, 0, 1, 1)
        self.StringBox = QtWidgets.QCheckBox(self.VariableTab)
        self.StringBox.setChecked(True)
        self.StringBox.setObjectName("StringBox")
        self.buttonGroup.addButton(self.StringBox)
        self.gridLayout.addWidget(self.StringBox, 0, 0, 1, 1)
        self.CharacterBox = QtWidgets.QCheckBox(self.VariableTab)
        self.CharacterBox.setChecked(True)
        self.CharacterBox.setObjectName("CharacterBox")
        self.buttonGroup.addButton(self.CharacterBox)
        self.gridLayout.addWidget(self.CharacterBox, 5, 0, 1, 1)
        self.StructBox = QtWidgets.QCheckBox(self.VariableTab)
        self.StructBox.setChecked(True)
        self.StructBox.setObjectName("StructBox")
        self.buttonGroup.addButton(self.StructBox)
        self.gridLayout.addWidget(self.StructBox, 1, 1, 1, 1)
        self.InnerTab.addTab(self.VariableTab, "")
        self.NameLengthTab = QtWidgets.QWidget()
        self.NameLengthTab.setObjectName("NameLengthTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.NameLengthTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LessThan3Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.LessThan3Box.setChecked(True)
        self.LessThan3Box.setObjectName("LessThan3Box")
        self.buttonGroup.addButton(self.LessThan3Box)
        self.gridLayout_2.addWidget(self.LessThan3Box, 0, 0, 1, 1)
        self.MoreThan20Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan20Box.setChecked(True)
        self.MoreThan20Box.setObjectName("MoreThan20Box")
        self.buttonGroup.addButton(self.MoreThan20Box)
        self.gridLayout_2.addWidget(self.MoreThan20Box, 0, 1, 1, 1)
        self.MoreThan3LessThan10Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan3LessThan10Box.setChecked(True)
        self.MoreThan3LessThan10Box.setObjectName("MoreThan3LessThan10Box")
        self.buttonGroup.addButton(self.MoreThan3LessThan10Box)
        self.gridLayout_2.addWidget(self.MoreThan3LessThan10Box, 1, 0, 1, 1)
        self.MoreThan10LessThan20Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan10LessThan20Box.setChecked(True)
        self.MoreThan10LessThan20Box.setObjectName("MoreThan10LessThan20Box")
        self.buttonGroup.addButton(self.MoreThan10LessThan20Box)
        self.gridLayout_2.addWidget(self.MoreThan10LessThan20Box, 2, 0, 1, 1)
        self.InnerTab.addTab(self.NameLengthTab, "")
        self.MeasurementTabs.addTab(self.MeasurementTab, "")
        self.StandardTab = QtWidgets.QWidget()
        self.StandardTab.setObjectName("StandardTab")
        self.tabWidget = QtWidgets.QTabWidget(self.StandardTab)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 631, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.PreambleTab = QtWidgets.QWidget()
        self.PreambleTab.setObjectName("PreambleTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.PreambleTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.AssumptionsBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.AssumptionsBox.setChecked(True)
        self.AssumptionsBox.setObjectName("AssumptionsBox")
        self.buttonGroup.addButton(self.AssumptionsBox)
        self.gridLayout_7.addWidget(self.AssumptionsBox, 0, 1, 1, 1)
        self.PurposeBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.PurposeBox.setChecked(True)
        self.PurposeBox.setObjectName("PurposeBox")
        self.buttonGroup.addButton(self.PurposeBox)
        self.gridLayout_7.addWidget(self.PurposeBox, 2, 0, 1, 2)
        self.FileNameBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.FileNameBox.setChecked(True)
        self.FileNameBox.setObjectName("FileNameBox")
        self.buttonGroup.addButton(self.FileNameBox)
        self.gridLayout_7.addWidget(self.FileNameBox, 0, 0, 1, 1)
        self.ChangeLogBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.ChangeLogBox.setChecked(True)
        self.ChangeLogBox.setObjectName("ChangeLogBox")
        self.buttonGroup.addButton(self.ChangeLogBox)
        self.gridLayout_7.addWidget(self.ChangeLogBox, 1, 1, 1, 1)
        self.InterfaceBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.InterfaceBox.setChecked(True)
        self.InterfaceBox.setObjectName("InterfaceBox")
        self.buttonGroup.addButton(self.InterfaceBox)
        self.gridLayout_7.addWidget(self.InterfaceBox, 3, 0, 1, 2)
        self.AuthorBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.AuthorBox.setChecked(True)
        self.AuthorBox.setObjectName("AuthorBox")
        self.buttonGroup.addButton(self.AuthorBox)
        self.gridLayout_7.addWidget(self.AuthorBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.PreambleTab, "")
        self.FlowControlTab = QtWidgets.QWidget()
        self.FlowControlTab.setObjectName("FlowControlTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.FlowControlTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.GotoBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.GotoBox.setChecked(True)
        self.GotoBox.setObjectName("GotoBox")
        self.buttonGroup.addButton(self.GotoBox)
        self.gridLayout_8.addWidget(self.GotoBox, 0, 0, 1, 1)
        self.SingleEntryBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.SingleEntryBox.setChecked(True)
        self.SingleEntryBox.setObjectName("SingleEntryBox")
        self.buttonGroup.addButton(self.SingleEntryBox)
        self.gridLayout_8.addWidget(self.SingleEntryBox, 1, 0, 1, 1)
        self.SingleExitBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.SingleExitBox.setChecked(True)
        self.SingleExitBox.setObjectName("SingleExitBox")
        self.buttonGroup.addButton(self.SingleExitBox)
        self.gridLayout_8.addWidget(self.SingleExitBox, 2, 0, 1, 1)
        self.RecursionBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.RecursionBox.setChecked(True)
        self.RecursionBox.setObjectName("RecursionBox")
        self.buttonGroup.addButton(self.RecursionBox)
        self.gridLayout_8.addWidget(self.RecursionBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.FlowControlTab, "")
        self.ClarityTab = QtWidgets.QWidget()
        self.ClarityTab.setObjectName("ClarityTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.ClarityTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_38 = QtWidgets.QCheckBox(self.ClarityTab)
        self.checkBox_38.setChecked(True)
        self.checkBox_38.setObjectName("checkBox_38")
        self.buttonGroup.addButton(self.checkBox_38)
        self.gridLayout_9.addWidget(self.checkBox_38, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.ClarityTab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.minVarLenBox = QtWidgets.QSpinBox(self.ClarityTab)
        self.minVarLenBox.setMinimum(3)
        self.minVarLenBox.setMaximum(20)
        self.minVarLenBox.setObjectName("minVarLenBox")
        self.gridLayout_9.addWidget(self.minVarLenBox, 0, 2, 1, 1)
        self.VariableNameLessThanXBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.VariableNameLessThanXBox.setChecked(True)
        self.VariableNameLessThanXBox.setObjectName("VariableNameLessThanXBox")
        self.buttonGroup.addButton(self.VariableNameLessThanXBox)
        self.gridLayout_9.addWidget(self.VariableNameLessThanXBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.ClarityTab)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.maxVarLenBox = QtWidgets.QSpinBox(self.ClarityTab)
        self.maxVarLenBox.setMinimum(5)
        self.maxVarLenBox.setMaximum(20)
        self.maxVarLenBox.setObjectName("maxVarLenBox")
        self.gridLayout_9.addWidget(self.maxVarLenBox, 1, 2, 1, 1)
        self.DefineParamBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.DefineParamBox.setChecked(True)
        self.DefineParamBox.setObjectName("DefineParamBox")
        self.buttonGroup.addButton(self.DefineParamBox)
        self.gridLayout_9.addWidget(self.DefineParamBox, 2, 0, 1, 1)
        self.VariableAllCapsBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.VariableAllCapsBox.setChecked(True)
        self.VariableAllCapsBox.setObjectName("VariableAllCapsBox")
        self.buttonGroup.addButton(self.VariableAllCapsBox)
        self.gridLayout_9.addWidget(self.VariableAllCapsBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.ClarityTab, "")
        self.ComplexityStandardTab = QtWidgets.QWidget()
        self.ComplexityStandardTab.setObjectName("ComplexityStandardTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ComplexityStandardTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.McCabesLessThanXBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.McCabesLessThanXBox.setChecked(True)
        self.McCabesLessThanXBox.setObjectName("McCabesLessThanXBox")
        self.buttonGroup.addButton(self.McCabesLessThanXBox)
        self.gridLayout_6.addWidget(self.McCabesLessThanXBox, 0, 0, 1, 1)
        self.MaxNestingLessThanXBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.MaxNestingLessThanXBox.setChecked(True)
        self.MaxNestingLessThanXBox.setObjectName("MaxNestingLessThanXBox")
        self.buttonGroup.addButton(self.MaxNestingLessThanXBox)
        self.gridLayout_6.addWidget(self.MaxNestingLessThanXBox, 1, 0, 1, 1)
        self.nestLevBox = QtWidgets.QSpinBox(self.ComplexityStandardTab)
        self.nestLevBox.setMinimum(1)
        self.nestLevBox.setMaximum(25)
        self.nestLevBox.setDisplayIntegerBase(10)
        self.nestLevBox.setObjectName("nestLevBox")
        self.gridLayout_6.addWidget(self.nestLevBox, 1, 2, 1, 1)
        self.LocalizationBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.LocalizationBox.setChecked(True)
        self.LocalizationBox.setObjectName("LocalizationBox")
        self.buttonGroup.addButton(self.LocalizationBox)
        self.gridLayout_6.addWidget(self.LocalizationBox, 3, 0, 1, 1)
        self.ESLOCLessThanXInFunctionBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.ESLOCLessThanXInFunctionBox.setChecked(True)
        self.ESLOCLessThanXInFunctionBox.setObjectName("ESLOCLessThanXInFunctionBox")
        self.buttonGroup.addButton(self.ESLOCLessThanXInFunctionBox)
        self.gridLayout_6.addWidget(self.ESLOCLessThanXInFunctionBox, 2, 0, 1, 1)
        self.mcAbeBox = QtWidgets.QSpinBox(self.ComplexityStandardTab)
        self.mcAbeBox.setMinimum(1)
        self.mcAbeBox.setMaximum(40)
        self.mcAbeBox.setObjectName("mcAbeBox")
        self.gridLayout_6.addWidget(self.mcAbeBox, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.ComplexityStandardTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(self.ComplexityStandardTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.tabWidget.addTab(self.ComplexityStandardTab, "")
        self.MeasurementTabs.addTab(self.StandardTab, "")
        self.verticalLayout.addWidget(self.MeasurementTabs)
        self.groupBox = QtWidgets.QGroupBox(FileSubForm)
        self.groupBox.setMinimumSize(QtCore.QSize(640, 40))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SubmitFileLink = QtWidgets.QCommandLinkButton(self.groupBox)
        self.SubmitFileLink.setMaximumSize(QtCore.QSize(640, 16777215))
        self.SubmitFileLink.setAutoFillBackground(True)
        self.SubmitFileLink.setIconSize(QtCore.QSize(25, 25))
        self.SubmitFileLink.setObjectName("SubmitFileLink")
        self.horizontalLayout.addWidget(self.SubmitFileLink)
        self.cancel = QtWidgets.QCommandLinkButton(self.groupBox)
        self.cancel.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icons/red_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FileSubForm)
        self.MeasurementTabs.setCurrentIndex(0)
        self.InnerTab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FileSubForm)

    def retranslateUi(self, FileSubForm):
        _translate = QtCore.QCoreApplication.translate
        FileSubForm.setWindowTitle(_translate("FileSubForm", "Submit your .java file(s)"))
        FileSubForm.setToolTip(_translate("FileSubForm", "Please enter open your files"))
        self.label_6.setText(_translate("FileSubForm", "File Name(s)"))
        self.addBtn.setText(_translate("FileSubForm", "Add Files"))
        self.pushButton.setText(_translate("FileSubForm", "Add a Directory"))
        self.removeButton.setText(_translate("FileSubForm", "Remove Files"))
        self.SLOCwCBox.setToolTip(_translate("FileSubForm", "Count the number of lines of code including comments."))
        self.SLOCwCBox.setText(_translate("FileSubForm", "Source Lines of Code with Comments"))
        self.SemicolonBox.setToolTip(_translate("FileSubForm", "Count the number of semicolons."))
        self.SemicolonBox.setText(_translate("FileSubForm", "Number of Semicolons"))
        self.SLOCwoCBox.setToolTip(_translate("FileSubForm", "Count the number of lines of code not including comments"))
        self.SLOCwoCBox.setText(_translate("FileSubForm", "Source Lines of Code without Comments"))
        self.FunctionCallBox.setToolTip(_translate("FileSubForm", "Count the number of function calls."))
        self.FunctionCallBox.setText(_translate("FileSubForm", "Number of Function Calls"))
        self.BlankLineBox.setToolTip(_translate("FileSubForm", "Count the number of blank lines."))
        self.BlankLineBox.setText(_translate("FileSubForm", "Blank Lines"))
        self.CommentLinesBox.setToolTip(_translate("FileSubForm", "Count the number of lines in the code that are only comments."))
        self.CommentLinesBox.setText(_translate("FileSubForm", "Full Comment Lines"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.SizeTab), _translate("FileSubForm", "Code Size"))
        self.PassedParamBox.setToolTip(_translate("FileSubForm", "Count the number of parameters that are passed."))
        self.PassedParamBox.setText(_translate("FileSubForm", "Number of Passed Parameters"))
        self.SwitchComplexityBox.setToolTip(_translate("FileSubForm", "Determine switch complexity"))
        self.SwitchComplexityBox.setText(_translate("FileSubForm", "Switch Complexity"))
        self.McCabeCompBox.setToolTip(_translate("FileSubForm", "Calculate McCab\'s Cyclomatic Complexity"))
        self.McCabeCompBox.setText(_translate("FileSubForm", "McCabe\'s Cyclomatic Complexity"))
        self.MaxNestingBox.setToolTip(_translate("FileSubForm", "Determine the maximum nesting level within the source code"))
        self.MaxNestingBox.setText(_translate("FileSubForm", "Maximum Nesting Level"))
        self.ESLOCatMaxNestBox.setToolTip(_translate("FileSubForm", "Count the executable source lines of code at the maximum nesting level"))
        self.ESLOCatMaxNestBox.setText(_translate("FileSubForm", "ESLOC at Max Nesting Level"))
        self.HalsteadCompBox.setToolTip(_translate("FileSubForm", "Calculate Halstead\'s Software Science Primitives"))
        self.HalsteadCompBox.setText(_translate("FileSubForm", "Halstead\'s Software Science Primitives"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.ComplexityTab), _translate("FileSubForm", "Code Complexity"))
        self.ForLoopBox.setToolTip(_translate("FileSubForm", "Count the number of for loops"))
        self.ForLoopBox.setText(_translate("FileSubForm", "Number of For Loops"))
        self.WhileLoopBox.setToolTip(_translate("FileSubForm", "count the number of while loops"))
        self.WhileLoopBox.setText(_translate("FileSubForm", "Number of While Loops"))
        self.DoWhileLoopBox.setToolTip(_translate("FileSubForm", "count the number of repeat loops"))
        self.DoWhileLoopBox.setText(_translate("FileSubForm", "Number of Do-While Loops"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.LoopTab), _translate("FileSubForm", "Loop Types"))
        self.UserDefBox.setToolTip(_translate("FileSubForm", "Count the total number of user defined variables in the code"))
        self.UserDefBox.setText(_translate("FileSubForm", "User Defined Variable"))
        self.TotalVarBox.setToolTip(_translate("FileSubForm", "Count the total number of variables in the code"))
        self.TotalVarBox.setText(_translate("FileSubForm", "Total Number of Variables"))
        self.FloatBox.setToolTip(_translate("FileSubForm", "Count the total number of float variables in the code"))
        self.FloatBox.setText(_translate("FileSubForm", "Float"))
        self.ArrayBox.setToolTip(_translate("FileSubForm", "Count the number of arrays in the code"))
        self.ArrayBox.setText(_translate("FileSubForm", "Array"))
        self.IntegerBox.setToolTip(_translate("FileSubForm", "Count the total number of integer variables in the code"))
        self.IntegerBox.setText(_translate("FileSubForm", "Integer"))
        self.StringBox.setToolTip(_translate("FileSubForm", "Count the total number of string variables in the code"))
        self.StringBox.setText(_translate("FileSubForm", "String"))
        self.CharacterBox.setToolTip(_translate("FileSubForm", "Count the total number of character variables in the code"))
        self.CharacterBox.setText(_translate("FileSubForm", "Character"))
        self.StructBox.setToolTip(_translate("FileSubForm", "Count the number of structures in the code"))
        self.StructBox.setText(_translate("FileSubForm", "Structure"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.VariableTab), _translate("FileSubForm", "Variables"))
        self.LessThan3Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names that are less than 3 characters"))
        self.LessThan3Box.setText(_translate("FileSubForm", "Names Less Than 3 Characters"))
        self.MoreThan20Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names mor than 20 characters"))
        self.MoreThan20Box.setText(_translate("FileSubForm", "Names 20 or More Characters"))
        self.MoreThan3LessThan10Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names more than 3 characters but less than 10 characters"))
        self.MoreThan3LessThan10Box.setText(_translate("FileSubForm", "Names More Than 3 but Less Than 10 Characters"))
        self.MoreThan10LessThan20Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names more than 10 characters but less than 20 characters"))
        self.MoreThan10LessThan20Box.setText(_translate("FileSubForm", "Names 10 or More but Less than 20 Characters"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.NameLengthTab), _translate("FileSubForm", "Name Length"))
        self.MeasurementTabs.setTabText(self.MeasurementTabs.indexOf(self.MeasurementTab), _translate("FileSubForm", "Measurements"))
        self.AssumptionsBox.setToolTip(_translate("FileSubForm", "Check for the presence of assumptions in the user preamble"))
        self.AssumptionsBox.setText(_translate("FileSubForm", "Assumptions"))
        self.PurposeBox.setToolTip(_translate("FileSubForm", "Check for the presence of purpose in the user preamble"))
        self.PurposeBox.setText(_translate("FileSubForm", "Purpose"))
        self.FileNameBox.setToolTip(_translate("FileSubForm", "Check for the presence of filename in the user preamble"))
        self.FileNameBox.setText(_translate("FileSubForm", "Filename"))
        self.ChangeLogBox.setToolTip(_translate("FileSubForm", "Check for the presence of a change log in the user preamble"))
        self.ChangeLogBox.setText(_translate("FileSubForm", "Change Log"))
        self.InterfaceBox.setToolTip(_translate("FileSubForm", "Check for the presence of interface in the user preamble"))
        self.InterfaceBox.setText(_translate("FileSubForm", "Interface"))
        self.AuthorBox.setToolTip(_translate("FileSubForm", "Check for the presence of author in the user preamble"))
        self.AuthorBox.setText(_translate("FileSubForm", "Author"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PreambleTab), _translate("FileSubForm", "User Preamble"))
        self.GotoBox.setToolTip(_translate("FileSubForm", "Check for the presence of GoTo statements"))
        self.GotoBox.setText(_translate("FileSubForm", "Presence of GoTo\'s"))
        self.SingleEntryBox.setToolTip(_translate("FileSubForm", "Check that the code has only one entry point"))
        self.SingleEntryBox.setText(_translate("FileSubForm", "Singular Entry Point"))
        self.SingleExitBox.setToolTip(_translate("FileSubForm", "Check that the code has only one exit point"))
        self.SingleExitBox.setText(_translate("FileSubForm", "Singular Exit Point"))
        self.RecursionBox.setToolTip(_translate("FileSubForm", "Check for the presence of recursion"))
        self.RecursionBox.setText(_translate("FileSubForm", "Presence of Recursion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FlowControlTab), _translate("FileSubForm", "Flow Control"))
        self.checkBox_38.setToolTip(_translate("FileSubForm", "Check that all variables are longer than the number \"X\" entered"))
        self.checkBox_38.setText(_translate("FileSubForm", "All Variable Names at Least X Characters Long"))
        self.label_3.setText(_translate("FileSubForm", "Mininum Variable Length"))
        self.VariableNameLessThanXBox.setToolTip(_translate("FileSubForm", "Check that all variables are not longer than the number \"X\" entered"))
        self.VariableNameLessThanXBox.setText(_translate("FileSubForm", "All Variable Names Not Longer than X Characters"))
        self.label.setText(_translate("FileSubForm", "Maximum Variable Length"))
        self.DefineParamBox.setToolTip(_translate("FileSubForm", "Check that all #define parameters are in all capital letters"))
        self.DefineParamBox.setText(_translate("FileSubForm", "All #define Parameters in All Capitals"))
        self.VariableAllCapsBox.setToolTip(_translate("FileSubForm", "Check that no standard variables are in all capital letters"))
        self.VariableAllCapsBox.setText(_translate("FileSubForm", "No Variable Names in All Capitals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ClarityTab), _translate("FileSubForm", "Program Clarity"))
        self.McCabesLessThanXBox.setToolTip(_translate("FileSubForm", "Determine if the given source code\'s cyclomatic coplexity is less than the number \"X\" entered"))
        self.McCabesLessThanXBox.setText(_translate("FileSubForm", "McCabe\'s Cyclomatic Complexity Less Than X"))
        self.MaxNestingLessThanXBox.setToolTip(_translate("FileSubForm", "Determine if the source code\'s maximum nesting level is less than the number \"X\" entered"))
        self.MaxNestingLessThanXBox.setText(_translate("FileSubForm", "Maximum Nesting Level Less Than X"))
        self.LocalizationBox.setToolTip(_translate("FileSubForm", "Check for localization of variables"))
        self.LocalizationBox.setText(_translate("FileSubForm", "Localization of Variables"))
        self.ESLOCLessThanXInFunctionBox.setToolTip(_translate("FileSubForm", "Determine if the number of executable source lines of code within functions is less than the number \"X\" entered"))
        self.ESLOCLessThanXInFunctionBox.setText(_translate("FileSubForm", "ESLOC Less Than X Within Functions"))
        self.label_5.setText(_translate("FileSubForm", "Nesting Level"))
        self.label_4.setText(_translate("FileSubForm", "McCabe\'s Complexity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ComplexityStandardTab), _translate("FileSubForm", "Complexity"))
        self.MeasurementTabs.setTabText(self.MeasurementTabs.indexOf(self.StandardTab), _translate("FileSubForm", "Coding Standards"))
        self.SubmitFileLink.setText(_translate("FileSubForm", "Submit Files"))
        self.cancel.setText(_translate("FileSubForm", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileSubForm = QtWidgets.QWidget()
    ui = Ui_FileSubForm()
    ui.setupUi(FileSubForm)
    FileSubForm.show()
    sys.exit(app.exec_())
