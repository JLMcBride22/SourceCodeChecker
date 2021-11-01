import sys
sys.path.append(".")
from GUI.mainWindow import ARI, MainWindow
from PyQt5 import QtWidgets as qtw

##The interface
a = ARI()

app = qtw.QApplication(sys.argv)
widget = MainWindow()



widget.__init__()
widget.setARI(a)

w = qtw.QMainWindow()

widget.show()

sys, exit(app.exec_())
