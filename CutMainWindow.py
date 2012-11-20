#!/usr/bin/python
 
import sys
from CutUtil import *
from CutUtilQt import *
from time import time
from PyQt4 import QtGui
from PyQt4 import QtCore

class CutMainWindow(QtGui.QMainWindow):

	def __init__(self):
		#general initialization
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle("Count Up Timer")
		#private variables
		self._timeDisplay = TimeDisplay()
		self._controlPanel = ControlPanel()
		self._seconds = 0
		self._timer = QtCore.QTimer(self)
		self._timer.setInterval(1000)
		#self._timer.start()
		#ui building
		containerLayout = QtGui.QVBoxLayout()
		containerLayout.addLayout(self._timeDisplay)
		containerLayout.addLayout(self._controlPanel)
		self._centralWidget = QtGui.QWidget()
		self._centralWidget.setLayout(containerLayout)
		self.setCentralWidget(self._centralWidget)
		#event handling
		self.initializeSlots()
		#finally
		self.show()
	
	def initializeSlots(self):
		self._controlPanel.getStartButton().clicked.connect(self.onStartButtonClicked)
		self._controlPanel.getStopButton().clicked.connect(self.onStopButtonClicked)
		self._controlPanel.getResetButton().clicked.connect(self.onResetButtonClicked)
		self._timer.timeout.connect(self.onTimeout)
	
	def onStartButtonClicked(self):
		self._timer.start()

	def onStopButtonClicked(self):
		self._timer.stop()

	def onResetButtonClicked(self):
		self._timeDisplay.setText('00:00:00')
	
	def onTimeout(self):
		self._seconds += 1
		print str(self._seconds)

application = QtGui.QApplication(sys.argv)
cutMainWindow = CutMainWindow()
application.exec_()
