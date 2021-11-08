from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialogButtonBox, QFileDialog, QListWidgetItem, QMessageBox, QTableView

from UIFiles.GCHistory import Ui_HistoryForm

from UIFiles.GCFileSubGUI import Ui_FileSubForm
class historyForm(qtw.QWidget):
    
    uiForm = Ui_HistoryForm()
    def __init__(self, *args, **kwargs):
        super(historyForm, self).__init__(*args, **kwargs)

        self.uiForm.setupUi(self)
        self.uiForm.pushButton.clicked.connect(self.close)
        