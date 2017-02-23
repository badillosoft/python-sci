from PyQt4 import QtGui
import sys

class MiApp(QtGui.QWidget):
    def __init__(self):
        super(MiApp, self).__init__()

        self.construir()

    def construir(self):
        boton = QtGui.QPushButton(self)
        boton.setText("Hola")

        self.resize(600, 400)
        self.setWindowTitle("Mi App")
        #self.show()

app = QtGui.QApplication(sys.argv)

w = MiApp()
w.show()

sys.exit(app.exec_())