from PyQt5 import QtWidgets as qtw


from UIFiles.GCUIHelp import Ui_Form

class userHelpC(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(userHelpC, self).__init__(*args, **kwargs)
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self)
        self.tree = None
