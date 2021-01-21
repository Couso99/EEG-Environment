# -*- coding: utf-8 -*-
# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from EDF.readEDFFile import read_signal_data
from GUI.ui_historic_plots import Ui_MainWindow

class HistoricPlot(QtWidgets.QMainWindow):
    def __init__(self, edf_fname, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fname = edf_fname

        pg.setConfigOptions(antialias=True)

        self.load_buffer()
        self.plot_all_time()
        self.plot_zoomed()


    def load_buffer(self):
        self.buffers, duration = read_signal_data(self.fname)
        self.x2 = np.linspace(0,duration,len(self.buffers[0]))


    def plot_all_time(self):
        self.ui.allTimePlot.plot(self.x2, self.buffers[0])
        self.lr = pg.LinearRegionItem([400,700])
        self.lr.setZValue(-10)
        self.ui.allTimePlot.addItem(self.lr)

    def plot_zoomed(self):
        for i, data in enumerate(self.buffers):
             self.ui.zoomedPlot.plot(self.x2, data+i*200)#, pen=(250, 250, 250))

        def updatePlot():
            self.ui.zoomedPlot.setXRange(*self.lr.getRegion(), padding=0)
        def updateRegion():
            self.lr.setRegion(self.ui.zoomedPlot.getViewBox().viewRange()[0])
        self.lr.sigRegionChanged.connect(updatePlot)
        self.ui.zoomedPlot.sigXRangeChanged.connect(updateRegion)
        updatePlot()
