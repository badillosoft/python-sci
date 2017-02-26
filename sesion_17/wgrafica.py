from PyQt4 import QtGui, uic

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class WGrafica(QtGui.QWidget):

    def __init__(self):
        super(WGrafica, self).__init__()

        uic.loadUi("grafica.ui", self)

        fig, ax = plt.subplots()
        
        ax.plot([1, 2, 3], [1, 2, 3])

        self.ax = ax

        self.canvas = FigureCanvasQTAgg(fig)

        self.verticalLayout.addWidget(self.canvas)

