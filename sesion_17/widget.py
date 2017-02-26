from PyQt4 import QtGui, uic

class MiWidget(QtGui.QWidget):

    def __init__(self):
        super(MiWidget, self).__init__()

        uic.loadUi("widget.ui", self)

        self.miCajaTexto.setText("Hola mundo")

        self.miBoton.clicked.connect(self.onClick)

        self.lcdNumber.display(90)

        self.horizontalSlider.sliderMoved.connect(self.contador)

    def onClick(self):
        self.miCajaTexto.clear()

    def contador(self, valor):
        self.lcdNumber.display(valor)
        self.miCajaTexto.setText("%d" % valor)