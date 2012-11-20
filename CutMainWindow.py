#!/usr/bin/python
 
import sys
import CutUtilQt
from PyQt4 import QtGui
from PyQt4 import QtCore

class CutMainWindow(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle("Count Up Timer")
		self._timeDisplay = CutUtilQt.TimeDisplay()
		self._controlPanel = CutUtilQt.ControlPanel()
		self._centralWidget = QtGui.QWidget()
		containerLayout = QtGui.QVBoxLayout()
		containerLayout.addLayout(self._timeDisplay)
		containerLayout.addLayout(self._controlPanel)
		self._centralWidget.setLayout(containerLayout)
		self.setCentralWidget(self._centralWidget)
		#self._centralWidget = StaticMethods.getContainerWidget()
		self.initializeSlots()
		self.show()
	
	def initializeSlots(self):
		QtCore.QObject.connect(self._controlPanel.getStartButton(), QtCore.SIGNAL("clicked()"), self.onStartButtonClicked)
		QtCore.QObject.connect(self._controlPanel.getStopButton(), QtCore.SIGNAL("clicked()"), self.onStopButtonClicked)
		QtCore.QObject.connect(self._controlPanel.getResetButton(), QtCore.SIGNAL("clicked()"), self.onResetButtonClicked)
	
	def onStartButtonClicked(self):
		print "START"

	def onStopButtonClicked(self):
		print "STOP"

	def onResetButtonClicked(self):
		print "RESET"

application = QtGui.QApplication(sys.argv)
cutMainWindow = CutMainWindow()
application.exec_()
