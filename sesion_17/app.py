from PyQt4 import QtGui
from widget import MiWidget
from wgrafica import WGrafica
import sys

app = QtGui.QApplication(sys.argv)

w = MiWidget()

w2 = WGrafica()

w.show()
w2.show()

sys.exit(app.exec_())