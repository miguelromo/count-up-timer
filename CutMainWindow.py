#!/usr/bin/python
 
import sys
from CutUtilQt import *
from PyQt4 import QtGui

class CutMainWindow(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle("Count Up Timer")
		self.resize(300, 300)
		self.setCentralWidget(CutUtilQt.getContainerWidget())
		self.show()


app = QtGui.QApplication(sys.argv)
f = CutMainWindow()
app.exec_()
