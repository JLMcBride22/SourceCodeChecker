from PyQt5 import QtWidgets as qtw


from UIFiles.GCMetricReport import Ui_Form
import xml.etree.ElementTree as et
from xml.etree.ElementTree import fromstring
class metricFormC(qtw.QWidget):
    
    
    def __init__(self, *args, **kwargs):
        super(metricFormC, self).__init__(*args, **kwargs)
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self)
        self.tree = None
    #converts string to xml tree. and prints the content of the xml file to the TreeWidget
    def strToXml(self, xmlStr):
        self.tree = et.fromstring(xmlStr)
        
        treeElement = qtw.QTreeWidgetItem([self.tree.tag])
        self.uiForm.treeWidget.addTopLevelItem(treeElement)

        def displaytree(a, s):
            for child in s:
                if child.text == None:
                    branch = qtw.QTreeWidgetItem([child.tag])
                    a.addChild(branch)
                    displaytree(branch, child)
                else:
                    branch = qtw.QTreeWidgetItem([child.text])
                    a.addChild(branch)
           
            



        displaytree(treeElement, self.tree)


    
    def findItemRemoves(self):
        return
        


    


    

        
        

