# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JLMcB\OneDrive\Documents\GitHub\SourceCodeChecker\plyj-master\GUI\UIFiles\FileSubmitter.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileSubForm(object):
    def setupUi(self, FileSubForm):
        FileSubForm.setObjectName("FileSubForm")
        FileSubForm.setWindowModality(QtCore.Qt.NonModal)
        FileSubForm.resize(660, 850)
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
        self.InnerTab.setGeometry(QtCore.QRect(0, 0, 1631, 431))
        self.InnerTab.setToolTip("")
        self.InnerTab.setObjectName("InnerTab")
        self.SizeTab = QtWidgets.QWidget()
        self.SizeTab.setObjectName("SizeTab")
        self.SLOCwCBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SLOCwCBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.SLOCwCBox.setAcceptDrops(False)
        self.SLOCwCBox.setAutoFillBackground(False)
        self.SLOCwCBox.setChecked(True)
        self.SLOCwCBox.setObjectName("SLOCwCBox")
        self.SLOCwoCBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SLOCwoCBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.SLOCwoCBox.setChecked(True)
        self.SLOCwoCBox.setObjectName("SLOCwoCBox")
        self.FunctionCallBox = QtWidgets.QCheckBox(self.SizeTab)
        self.FunctionCallBox.setGeometry(QtCore.QRect(400, 70, 265, 40))
        self.FunctionCallBox.setChecked(True)
        self.FunctionCallBox.setObjectName("FunctionCallBox")
        self.SemicolonBox = QtWidgets.QCheckBox(self.SizeTab)
        self.SemicolonBox.setGeometry(QtCore.QRect(400, 20, 265, 40))
        self.SemicolonBox.setChecked(True)
        self.SemicolonBox.setObjectName("SemicolonBox")
        self.CommentLinesBox = QtWidgets.QCheckBox(self.SizeTab)
        self.CommentLinesBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.CommentLinesBox.setChecked(True)
        self.CommentLinesBox.setObjectName("CommentLinesBox")
        self.BlankLineBox = QtWidgets.QCheckBox(self.SizeTab)
        self.BlankLineBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.BlankLineBox.setChecked(True)
        self.BlankLineBox.setObjectName("BlankLineBox")
        self.InnerTab.addTab(self.SizeTab, "")
        self.ComplexityTab = QtWidgets.QWidget()
        self.ComplexityTab.setObjectName("ComplexityTab")
        self.PassedParamBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.PassedParamBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.PassedParamBox.setChecked(True)
        self.PassedParamBox.setObjectName("PassedParamBox")
        self.SwitchComplexityBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.SwitchComplexityBox.setGeometry(QtCore.QRect(400, 20, 265, 40))
        self.SwitchComplexityBox.setChecked(True)
        self.SwitchComplexityBox.setObjectName("SwitchComplexityBox")
        self.ESLOCatMaxNestBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.ESLOCatMaxNestBox.setGeometry(QtCore.QRect(400, 70, 265, 40))
        self.ESLOCatMaxNestBox.setChecked(True)
        self.ESLOCatMaxNestBox.setObjectName("ESLOCatMaxNestBox")
        self.MaxNestingBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.MaxNestingBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.MaxNestingBox.setChecked(True)
        self.MaxNestingBox.setObjectName("MaxNestingBox")
        self.HalsteadCompBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.HalsteadCompBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.HalsteadCompBox.setChecked(True)
        self.HalsteadCompBox.setObjectName("HalsteadCompBox")
        self.McCabeCompBox = QtWidgets.QCheckBox(self.ComplexityTab)
        self.McCabeCompBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.McCabeCompBox.setChecked(True)
        self.McCabeCompBox.setObjectName("McCabeCompBox")
        self.InnerTab.addTab(self.ComplexityTab, "")
        self.LoopTab = QtWidgets.QWidget()
        self.LoopTab.setObjectName("LoopTab")
        self.ForLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.ForLoopBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.ForLoopBox.setChecked(True)
        self.ForLoopBox.setObjectName("ForLoopBox")
        self.WhileLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.WhileLoopBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.WhileLoopBox.setChecked(True)
        self.WhileLoopBox.setObjectName("WhileLoopBox")
        self.DoWhileLoopBox = QtWidgets.QCheckBox(self.LoopTab)
        self.DoWhileLoopBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.DoWhileLoopBox.setChecked(True)
        self.DoWhileLoopBox.setObjectName("DoWhileLoopBox")
        self.InnerTab.addTab(self.LoopTab, "")
        self.VariableTab = QtWidgets.QWidget()
        self.VariableTab.setObjectName("VariableTab")
        self.TotalVarBox = QtWidgets.QCheckBox(self.VariableTab)
        self.TotalVarBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.TotalVarBox.setChecked(True)
        self.TotalVarBox.setObjectName("TotalVarBox")
        self.IntegerBox = QtWidgets.QCheckBox(self.VariableTab)
        self.IntegerBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.IntegerBox.setChecked(True)
        self.IntegerBox.setObjectName("IntegerBox")
        self.FloatBox = QtWidgets.QCheckBox(self.VariableTab)
        self.FloatBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.FloatBox.setChecked(True)
        self.FloatBox.setObjectName("FloatBox")
        self.CharacterBox = QtWidgets.QCheckBox(self.VariableTab)
        self.CharacterBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.CharacterBox.setChecked(True)
        self.CharacterBox.setObjectName("CharacterBox")
        self.StringBox = QtWidgets.QCheckBox(self.VariableTab)
        self.StringBox.setGeometry(QtCore.QRect(30, 220, 265, 40))
        self.StringBox.setChecked(True)
        self.StringBox.setObjectName("StringBox")
        self.UserDefBox = QtWidgets.QCheckBox(self.VariableTab)
        self.UserDefBox.setGeometry(QtCore.QRect(400, 20, 265, 40))
        self.UserDefBox.setChecked(True)
        self.UserDefBox.setObjectName("UserDefBox")
        self.StructBox = QtWidgets.QCheckBox(self.VariableTab)
        self.StructBox.setGeometry(QtCore.QRect(400, 70, 265, 40))
        self.StructBox.setChecked(True)
        self.StructBox.setObjectName("StructBox")
        self.checkBox_23 = QtWidgets.QCheckBox(self.VariableTab)
        self.checkBox_23.setGeometry(QtCore.QRect(30, 355, 265, 40))
        self.checkBox_23.setObjectName("checkBox_23")
        self.InnerTab.addTab(self.VariableTab, "")
        self.NameLengthTab = QtWidgets.QWidget()
        self.NameLengthTab.setObjectName("NameLengthTab")
        self.LessThan3Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.LessThan3Box.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.LessThan3Box.setChecked(True)
        self.LessThan3Box.setObjectName("LessThan3Box")
        self.MoreThan3LessThan10Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan3LessThan10Box.setGeometry(QtCore.QRect(30, 70, 281, 40))
        self.MoreThan3LessThan10Box.setChecked(True)
        self.MoreThan3LessThan10Box.setObjectName("MoreThan3LessThan10Box")
        self.MoreThan10LessThan20Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan10LessThan20Box.setGeometry(QtCore.QRect(30, 120, 281, 40))
        self.MoreThan10LessThan20Box.setChecked(True)
        self.MoreThan10LessThan20Box.setObjectName("MoreThan10LessThan20Box")
        self.MoreThan20Box = QtWidgets.QCheckBox(self.NameLengthTab)
        self.MoreThan20Box.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.MoreThan20Box.setChecked(True)
        self.MoreThan20Box.setObjectName("MoreThan20Box")
        self.InnerTab.addTab(self.NameLengthTab, "")
        self.MeasurementTabs.addTab(self.MeasurementTab, "")
        self.StandardTab = QtWidgets.QWidget()
        self.StandardTab.setObjectName("StandardTab")
        self.StandardTabs = QtWidgets.QTabWidget(self.StandardTab)
        self.StandardTabs.setGeometry(QtCore.QRect(0, 0, 981, 391))
        self.StandardTabs.setObjectName("StandardTabs")
        self.PreambleTab = QtWidgets.QWidget()
        self.PreambleTab.setObjectName("PreambleTab")
        self.FileNameBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.FileNameBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.FileNameBox.setChecked(True)
        self.FileNameBox.setObjectName("FileNameBox")
        self.AuthorBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.AuthorBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.AuthorBox.setChecked(True)
        self.AuthorBox.setObjectName("AuthorBox")
        self.PurposeBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.PurposeBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.PurposeBox.setChecked(True)
        self.PurposeBox.setObjectName("PurposeBox")
        self.InterfaceBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.InterfaceBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.InterfaceBox.setChecked(True)
        self.InterfaceBox.setObjectName("InterfaceBox")
        self.ChangeLogBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.ChangeLogBox.setGeometry(QtCore.QRect(250, 70, 265, 40))
        self.ChangeLogBox.setChecked(True)
        self.ChangeLogBox.setObjectName("ChangeLogBox")
        self.AssumptionsBox = QtWidgets.QCheckBox(self.PreambleTab)
        self.AssumptionsBox.setGeometry(QtCore.QRect(250, 20, 265, 40))
        self.AssumptionsBox.setChecked(True)
        self.AssumptionsBox.setObjectName("AssumptionsBox")
        self.StandardTabs.addTab(self.PreambleTab, "")
        self.FlowControlTab = QtWidgets.QWidget()
        self.FlowControlTab.setObjectName("FlowControlTab")
        self.GotoBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.GotoBox.setGeometry(QtCore.QRect(30, 20, 265, 40))
        self.GotoBox.setChecked(True)
        self.GotoBox.setObjectName("GotoBox")
        self.SingleEntryBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.SingleEntryBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.SingleEntryBox.setChecked(True)
        self.SingleEntryBox.setObjectName("SingleEntryBox")
        self.SingleExitBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.SingleExitBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.SingleExitBox.setChecked(True)
        self.SingleExitBox.setObjectName("SingleExitBox")
        self.RecursionBox = QtWidgets.QCheckBox(self.FlowControlTab)
        self.RecursionBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.RecursionBox.setChecked(True)
        self.RecursionBox.setObjectName("RecursionBox")
        self.StandardTabs.addTab(self.FlowControlTab, "")
        self.ClarityTab = QtWidgets.QWidget()
        self.ClarityTab.setObjectName("ClarityTab")
        self.checkBox_38 = QtWidgets.QCheckBox(self.ClarityTab)
        self.checkBox_38.setGeometry(QtCore.QRect(30, 20, 281, 40))
        self.checkBox_38.setChecked(True)
        self.checkBox_38.setObjectName("checkBox_38")
        self.VariableNameLessThanXBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.VariableNameLessThanXBox.setGeometry(QtCore.QRect(30, 70, 281, 40))
        self.VariableNameLessThanXBox.setChecked(True)
        self.VariableNameLessThanXBox.setObjectName("VariableNameLessThanXBox")
        self.DefineParamBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.DefineParamBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.DefineParamBox.setChecked(True)
        self.DefineParamBox.setObjectName("DefineParamBox")
        self.VariableAllCapsBox = QtWidgets.QCheckBox(self.ClarityTab)
        self.VariableAllCapsBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.VariableAllCapsBox.setChecked(True)
        self.VariableAllCapsBox.setObjectName("VariableAllCapsBox")
        self.label_3 = QtWidgets.QLabel(self.ClarityTab)
        self.label_3.setGeometry(QtCore.QRect(350, 32, 151, 16))
        self.label_3.setObjectName("label_3")
        self.minVarLenBox = QtWidgets.QSpinBox(self.ClarityTab)
        self.minVarLenBox.setGeometry(QtCore.QRect(500, 32, 37, 20))
        self.minVarLenBox.setMinimum(3)
        self.minVarLenBox.setMaximum(20)
        self.minVarLenBox.setObjectName("minVarLenBox")
        self.label = QtWidgets.QLabel(self.ClarityTab)
        self.label.setGeometry(QtCore.QRect(350, 83, 151, 16))
        self.label.setObjectName("label")
        self.maxVarLenBox = QtWidgets.QSpinBox(self.ClarityTab)
        self.maxVarLenBox.setGeometry(QtCore.QRect(500, 82, 37, 20))
        self.maxVarLenBox.setMinimum(5)
        self.maxVarLenBox.setMaximum(20)
        self.maxVarLenBox.setObjectName("maxVarLenBox")
        self.StandardTabs.addTab(self.ClarityTab, "")
        self.ComplexityStandardTab = QtWidgets.QWidget()
        self.ComplexityStandardTab.setObjectName("ComplexityStandardTab")
        self.McCabesLessThanXBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.McCabesLessThanXBox.setGeometry(QtCore.QRect(30, 20, 300, 40))
        self.McCabesLessThanXBox.setChecked(True)
        self.McCabesLessThanXBox.setObjectName("McCabesLessThanXBox")
        self.MaxNestingLessThanXBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.MaxNestingLessThanXBox.setGeometry(QtCore.QRect(30, 70, 265, 40))
        self.MaxNestingLessThanXBox.setChecked(True)
        self.MaxNestingLessThanXBox.setObjectName("MaxNestingLessThanXBox")
        self.ESLOCLessThanXInFunctionBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.ESLOCLessThanXInFunctionBox.setGeometry(QtCore.QRect(30, 120, 265, 40))
        self.ESLOCLessThanXInFunctionBox.setChecked(True)
        self.ESLOCLessThanXInFunctionBox.setObjectName("ESLOCLessThanXInFunctionBox")
        self.LocalizationBox = QtWidgets.QCheckBox(self.ComplexityStandardTab)
        self.LocalizationBox.setGeometry(QtCore.QRect(30, 170, 265, 40))
        self.LocalizationBox.setChecked(True)
        self.LocalizationBox.setObjectName("LocalizationBox")
        self.label_4 = QtWidgets.QLabel(self.ComplexityStandardTab)
        self.label_4.setGeometry(QtCore.QRect(350, 32, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.ComplexityStandardTab)
        self.label_5.setGeometry(QtCore.QRect(350, 80, 131, 16))
        self.label_5.setObjectName("label_5")
        self.nestLevBox = QtWidgets.QSpinBox(self.ComplexityStandardTab)
        self.nestLevBox.setGeometry(QtCore.QRect(480, 80, 37, 20))
        self.nestLevBox.setMinimum(1)
        self.nestLevBox.setMaximum(25)
        self.nestLevBox.setDisplayIntegerBase(10)
        self.nestLevBox.setObjectName("nestLevBox")
        self.mcAbeBox = QtWidgets.QSpinBox(self.ComplexityStandardTab)
        self.mcAbeBox.setGeometry(QtCore.QRect(480, 32, 37, 20))
        self.mcAbeBox.setMinimum(1)
        self.mcAbeBox.setMaximum(40)
        self.mcAbeBox.setObjectName("mcAbeBox")
        self.StandardTabs.addTab(self.ComplexityStandardTab, "")
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
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\JLMcB\\OneDrive\\Documents\\GitHub\\SourceCodeChecker\\plyj-master\\GUI\\UIFiles\\GUI/icons/red_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FileSubForm)
        self.MeasurementTabs.setCurrentIndex(1)
        self.InnerTab.setCurrentIndex(3)
        self.StandardTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FileSubForm)

    def retranslateUi(self, FileSubForm):
        _translate = QtCore.QCoreApplication.translate
        FileSubForm.setWindowTitle(_translate("FileSubForm", "Submit your .java file(s)"))
        FileSubForm.setToolTip(_translate("FileSubForm", "Please enter open your files"))
        self.label_6.setText(_translate("FileSubForm", "File Name(s)"))
        self.addBtn.setText(_translate("FileSubForm", "Add Files"))
        self.removeButton.setText(_translate("FileSubForm", "Remove Files"))
        self.SLOCwCBox.setToolTip(_translate("FileSubForm", "Count the number of lines of code including comments."))
        self.SLOCwCBox.setText(_translate("FileSubForm", "Source Lines of Code with Comments"))
        self.SLOCwoCBox.setToolTip(_translate("FileSubForm", "Count the number of lines of code not including comments"))
        self.SLOCwoCBox.setText(_translate("FileSubForm", "Source Lines of Code without Comments"))
        self.FunctionCallBox.setToolTip(_translate("FileSubForm", "Count the number of function calls."))
        self.FunctionCallBox.setText(_translate("FileSubForm", "Number of Function Calls"))
        self.SemicolonBox.setToolTip(_translate("FileSubForm", "Count the number of semicolons."))
        self.SemicolonBox.setText(_translate("FileSubForm", "Number of Semicolons"))
        self.CommentLinesBox.setToolTip(_translate("FileSubForm", "Count the number of lines in the code that are only comments."))
        self.CommentLinesBox.setText(_translate("FileSubForm", "Full Comment Lines"))
        self.BlankLineBox.setToolTip(_translate("FileSubForm", "Count the number of blank lines."))
        self.BlankLineBox.setText(_translate("FileSubForm", "Blank Lines"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.SizeTab), _translate("FileSubForm", "Code Size"))
        self.PassedParamBox.setToolTip(_translate("FileSubForm", "Count the number of parameters that are passed."))
        self.PassedParamBox.setText(_translate("FileSubForm", "Number of Passed Parameters"))
        self.SwitchComplexityBox.setToolTip(_translate("FileSubForm", "Determine switch complexity"))
        self.SwitchComplexityBox.setText(_translate("FileSubForm", "Switch Complexity"))
        self.ESLOCatMaxNestBox.setToolTip(_translate("FileSubForm", "Count the executable source lines of code at the maximum nesting level"))
        self.ESLOCatMaxNestBox.setText(_translate("FileSubForm", "ESLOC at Max Nesting Level"))
        self.MaxNestingBox.setToolTip(_translate("FileSubForm", "Determine the maximum nesting level within the source code"))
        self.MaxNestingBox.setText(_translate("FileSubForm", "Maximum Nesting Level"))
        self.HalsteadCompBox.setToolTip(_translate("FileSubForm", "Calculate Halstead\'s Software Science Primitives"))
        self.HalsteadCompBox.setText(_translate("FileSubForm", "Halstead\'s Software Science Primitives"))
        self.McCabeCompBox.setToolTip(_translate("FileSubForm", "Calculate McCab\'s Cyclomatic Complexity"))
        self.McCabeCompBox.setText(_translate("FileSubForm", "McCabe\'s Cyclomatic Complexity"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.ComplexityTab), _translate("FileSubForm", "Code Complexity"))
        self.ForLoopBox.setToolTip(_translate("FileSubForm", "Count the number of for loops"))
        self.ForLoopBox.setText(_translate("FileSubForm", "Number of For Loops"))
        self.WhileLoopBox.setToolTip(_translate("FileSubForm", "count the number of while loops"))
        self.WhileLoopBox.setText(_translate("FileSubForm", "Number of While Loops"))
        self.DoWhileLoopBox.setToolTip(_translate("FileSubForm", "count the number of repeat loops"))
        self.DoWhileLoopBox.setText(_translate("FileSubForm", "Number of Do-While Loops"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.LoopTab), _translate("FileSubForm", "Loop Types"))
        self.TotalVarBox.setToolTip(_translate("FileSubForm", "Count the total number of variables in the code"))
        self.TotalVarBox.setText(_translate("FileSubForm", "Total Number of Variables"))
        self.IntegerBox.setToolTip(_translate("FileSubForm", "Count the total number of integer variables in the code"))
        self.IntegerBox.setText(_translate("FileSubForm", "Integer"))
        self.FloatBox.setToolTip(_translate("FileSubForm", "Count the total number of float variables in the code"))
        self.FloatBox.setText(_translate("FileSubForm", "Float"))
        self.CharacterBox.setToolTip(_translate("FileSubForm", "Count the total number of character variables in the code"))
        self.CharacterBox.setText(_translate("FileSubForm", "Character"))
        self.StringBox.setToolTip(_translate("FileSubForm", "Count the total number of string variables in the code"))
        self.StringBox.setText(_translate("FileSubForm", "String"))
        self.UserDefBox.setToolTip(_translate("FileSubForm", "Count the total number of user defined variables in the code"))
        self.UserDefBox.setText(_translate("FileSubForm", "User Defined Variable"))
        self.StructBox.setToolTip(_translate("FileSubForm", "Count the number of structures in the code"))
        self.StructBox.setText(_translate("FileSubForm", "Structure"))
        self.checkBox_23.setToolTip(_translate("FileSubForm", "Count the number of arrays in the code"))
        self.checkBox_23.setText(_translate("FileSubForm", "Array"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.VariableTab), _translate("FileSubForm", "Variables"))
        self.LessThan3Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names that are less than 3 characters"))
        self.LessThan3Box.setText(_translate("FileSubForm", "Names Less Than 3 Characters"))
        self.MoreThan3LessThan10Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names more than 3 characters but less than 10 characters"))
        self.MoreThan3LessThan10Box.setText(_translate("FileSubForm", "Names More Than 3 but Less Than 10 Characters"))
        self.MoreThan10LessThan20Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names more than 10 characters but less than 20 characters"))
        self.MoreThan10LessThan20Box.setText(_translate("FileSubForm", "Names 10 or More but Less than 20 Characters"))
        self.MoreThan20Box.setToolTip(_translate("FileSubForm", "Count the number of variables with names mor than 20 characters"))
        self.MoreThan20Box.setText(_translate("FileSubForm", "Names 20 or More Characters"))
        self.InnerTab.setTabText(self.InnerTab.indexOf(self.NameLengthTab), _translate("FileSubForm", "Name Length"))
        self.MeasurementTabs.setTabText(self.MeasurementTabs.indexOf(self.MeasurementTab), _translate("FileSubForm", "Measurements"))
        self.FileNameBox.setToolTip(_translate("FileSubForm", "Check for the presence of filename in the user preamble"))
        self.FileNameBox.setText(_translate("FileSubForm", "Filename"))
        self.AuthorBox.setToolTip(_translate("FileSubForm", "Check for the presence of author in the user preamble"))
        self.AuthorBox.setText(_translate("FileSubForm", "Author"))
        self.PurposeBox.setToolTip(_translate("FileSubForm", "Check for the presence of purpose in the user preamble"))
        self.PurposeBox.setText(_translate("FileSubForm", "Purpose"))
        self.InterfaceBox.setToolTip(_translate("FileSubForm", "Check for the presence of interface in the user preamble"))
        self.InterfaceBox.setText(_translate("FileSubForm", "Interface"))
        self.ChangeLogBox.setToolTip(_translate("FileSubForm", "Check for the presence of a change log in the user preamble"))
        self.ChangeLogBox.setText(_translate("FileSubForm", "Change Log"))
        self.AssumptionsBox.setToolTip(_translate("FileSubForm", "Check for the presence of assumptions in the user preamble"))
        self.AssumptionsBox.setText(_translate("FileSubForm", "Assumptions"))
        self.StandardTabs.setTabText(self.StandardTabs.indexOf(self.PreambleTab), _translate("FileSubForm", "User Preamble"))
        self.GotoBox.setToolTip(_translate("FileSubForm", "Check for the presence of GoTo statements"))
        self.GotoBox.setText(_translate("FileSubForm", "Presence of GoTo\'s"))
        self.SingleEntryBox.setToolTip(_translate("FileSubForm", "Check that the code has only one entry point"))
        self.SingleEntryBox.setText(_translate("FileSubForm", "Singular Entry Point"))
        self.SingleExitBox.setToolTip(_translate("FileSubForm", "Check that the code has only one exit point"))
        self.SingleExitBox.setText(_translate("FileSubForm", "Singular Exit Point"))
        self.RecursionBox.setToolTip(_translate("FileSubForm", "Check for the presence of recursion"))
        self.RecursionBox.setText(_translate("FileSubForm", "Presence of Recursion"))
        self.StandardTabs.setTabText(self.StandardTabs.indexOf(self.FlowControlTab), _translate("FileSubForm", "Flow Control"))
        self.checkBox_38.setToolTip(_translate("FileSubForm", "Check that all variables are longer than the number \"X\" entered"))
        self.checkBox_38.setText(_translate("FileSubForm", "All Variable Names at Least X Characters Long"))
        self.VariableNameLessThanXBox.setToolTip(_translate("FileSubForm", "Check that all variables are not longer than the number \"X\" entered"))
        self.VariableNameLessThanXBox.setText(_translate("FileSubForm", "All Variable Names Not Longer than X Characters"))
        self.DefineParamBox.setToolTip(_translate("FileSubForm", "Check that all #define parameters are in all capital letters"))
        self.DefineParamBox.setText(_translate("FileSubForm", "All #define Parameters in All Capitals"))
        self.VariableAllCapsBox.setToolTip(_translate("FileSubForm", "Check that no standard variables are in all capital letters"))
        self.VariableAllCapsBox.setText(_translate("FileSubForm", "No Variable Names in All Capitals"))
        self.label_3.setText(_translate("FileSubForm", "Mininum Variable Length"))
        self.label.setText(_translate("FileSubForm", "Maximum Variable Length"))
        self.StandardTabs.setTabText(self.StandardTabs.indexOf(self.ClarityTab), _translate("FileSubForm", "Program Clarity"))
        self.McCabesLessThanXBox.setToolTip(_translate("FileSubForm", "Determine if the given source code\'s cyclomatic coplexity is less than the number \"X\" entered"))
        self.McCabesLessThanXBox.setText(_translate("FileSubForm", "McCabe\'s Cyclomatic Complexity Less Than X"))
        self.MaxNestingLessThanXBox.setToolTip(_translate("FileSubForm", "Determine if the source code\'s maximum nesting level is less than the number \"X\" entered"))
        self.MaxNestingLessThanXBox.setText(_translate("FileSubForm", "Maximum Nesting Level Less Than X"))
        self.ESLOCLessThanXInFunctionBox.setToolTip(_translate("FileSubForm", "Determine if the number of executable source lines of code within functions is less than the number \"X\" entered"))
        self.ESLOCLessThanXInFunctionBox.setText(_translate("FileSubForm", "ESLOC Less Than X Within Functions"))
        self.LocalizationBox.setToolTip(_translate("FileSubForm", "Check for localization of variables"))
        self.LocalizationBox.setText(_translate("FileSubForm", "Localization of Variables"))
        self.label_4.setText(_translate("FileSubForm", "McCabe\'s Complexity"))
        self.label_5.setText(_translate("FileSubForm", "Nesting Level"))
        self.StandardTabs.setTabText(self.StandardTabs.indexOf(self.ComplexityStandardTab), _translate("FileSubForm", "Complexity"))
        self.MeasurementTabs.setTabText(self.MeasurementTabs.indexOf(self.StandardTab), _translate("FileSubForm", "Coding Standards"))
        self.SubmitFileLink.setText(_translate("FileSubForm", "Submit Files"))
        self.cancel.setText(_translate("FileSubForm", "Cancel"))
