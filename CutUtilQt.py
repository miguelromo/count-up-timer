#!/usr/bin/python

from PyQt4 import QtGui

class CutUtilQt:

	@staticmethod
	def getContainerWidget():
		containerWidget = QtGui.QWidget()
		containerWidget.setLayout(CutUtilQt.getContainerLayout())
		return containerWidget
	
	@staticmethod
	def getContainerLayout():
		r1 = QtGui.QRadioButton("Radio")
		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(r1)
		return vbox
