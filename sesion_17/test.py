import sys
from PyQt4 import QtGui
from mi_app import MiApp

app = QtGui.QApplication(sys.argv)

w = MiApp()

w.show()

sys.exit(app.exec_())