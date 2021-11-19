from PyQt5 import QtGui, QtWidgets as qtw


from UIFiles.GCHistory import Ui_HistoryForm
from PyQt5 import QtGui
from UIFiles.GCFileSubGUI import Ui_FileSubForm
class historyForm(qtw.QWidget):
    
    uiForm = Ui_HistoryForm()
    def __init__(self, *args, **kwargs):
        
        super(historyForm, self).__init__(*args, **kwargs)
        self.uiForm.setupUi(self)
        self.uiForm.pushButton.clicked.connect(self.close)
        self.uiForm.tableWidget.insertRow(3)
        
        