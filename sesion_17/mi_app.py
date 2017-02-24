from PyQt4 import QtCore, QtGui, uic

class MiApp(QtGui.QWidget):
	
	def __init__(self):
		super(MiApp, self).__init__()
		
		uic.loadUi('test.ui', self)

		self.pushButton.clicked.connect(self.hello)
		self.pushButton_2.clicked.connect(self.hello)
		self.horizontalSlider.valueChanged.connect(self.count)

	def count(self, value):
		print value

	def hello(self):
		sender = self.sender()

		print sender.objectName()
