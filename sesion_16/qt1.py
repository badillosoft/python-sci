from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(600, 400)
w.setWindowTitle("Mi App")
w.show()

sys.exit(app.exec_())