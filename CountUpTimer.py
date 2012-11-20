#!/usr/bin/python
 
import sys
from PyQt4 import QtGui
 
class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle("Count Up Timer")
		self.resize(300, 300)
		self.show()

app = QtGui.QApplication(sys.argv)
f = MainWindow()
app.exec_()
