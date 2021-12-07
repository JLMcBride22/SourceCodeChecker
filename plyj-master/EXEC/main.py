# main.py
# Purpose: Provides the launching point for the program. It creates the Analysis Report Interface
# and connects it to the MainWindow before starting the MainWindow.
# Authors: Jonathan Lewis.
# Build Date: December 3, 2021.
#********************************************************************************************
import sys
sys.path.append(".")
from GUI.mainWindow import ARI, MainWindow
from PyQt5 import QtWidgets as qtw

##The create the interface
a = ARI()


##creates the app and and main window
app = qtw.QApplication(sys.argv)
widget = MainWindow()

widget.__init__()
widget.setARI(a)

widget.show()

sys, sys.exit(app.exec_())
