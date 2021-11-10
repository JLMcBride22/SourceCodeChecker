from PyQt5 import QtWidgets as qtw


from UIFiles.GCMetricReport import Ui_Form

class metricFormC(qtw.QWidget):
    
    
    def __init__(self, *args, **kwargs):
        super(metricFormC, self).__init__(*args, **kwargs)
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self)
        
        

