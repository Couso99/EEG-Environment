from PyQt5 import QtWidgets, QtCore, QtGui, uic
import pyqtgraph as pg
#import sip

from COM.init_connection import OpenBCI_connection
from COM.open_bci_GCPDS import OpenBCIBoard as openbci

from GUI.ui_subject_widget import Ui_Form
#Ui_SubjectWidget, _ = uic.loadUiType("GUI/subject_widget.ui")

class SubjectWidget(QtWidgets.QWidget):#, Ui_SubjectWidget):
    def __init__(self, port):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.port = port
        self.ui.portLabel.setText(f"Canal {openbci.get_channel_from_port(port)}")

        self.CHANNELS_PER_GRAPH = 2

        self.openbci_connect()
        self.init_channel_plot()

        self.ui.saveRecordButton.clicked.connect(self.openbci_conn.saveFileDialog)
        self.ui.showAllButton.clicked.connect(self.openbci_conn.showAllChannels)
        self.ui.recordButton.clicked.connect(self.start_stop_recording)
        self.ui.startButton.clicked.connect(self.send_start)
        self.ui.pauseButton.clicked.connect(self.send_stop)

    def openbci_disconnect(self):
        self.openbci_conn.terminate()
        self.deleteLater() #sip.delete(self.widget_name)
        self = None

    def openbci_connect(self):
        self.openbci_conn = OpenBCI_connection(self.port)

    def start_stop_recording(self):
        '''self.openbci_conn.gui.launch_trigger_server(self.openbci_conn.recording_manager.update_state)
        if not self.app.trigger_server.activated:
            self.saveRecordButton.setEnabled(True)
            self.recordButton.setText("Stop")
        else:
            self.saveRecordButton.setEnabled(False)
            self.recordButton.setText("Record")'''
        self.openbci_conn.start_record()
        self.ui.recordButton.setText("Stop")


    def send_start(self):
        if not self.openbci_conn.recording_manager.streaming.value:
            self.openbci_conn.recording_manager.test_acquisition()
            self.ui.startButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(True)
            self.eeg_channel_timer.start(self.openbci_conn.constants.refresh_rate)

    def send_stop(self):
        if self.openbci_conn.recording_manager.streaming.value:
            self.openbci_conn.recording_manager.test_acquisition()
            self.ui.startButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.eeg_channel_timer.stop()

    def init_channel_plot(self):
        self.channelCurve = []
        self.ui.channelPlotGraph.clear()

        for i in range(self.CHANNELS_PER_GRAPH):
            c = pg.PlotCurveItem(pen = (i, self.CHANNELS_PER_GRAPH*1.3))
            c.setPos(0, 0)
            self.ui.channelPlotGraph.addItem(c)  #Agregar la curva al widget
            self.channelCurve.append(c)           #Se asocia los valores a la gráfica

        self.set_plot()

        self.openbci_conn.gui.styleQwtPlot('EEG one channel', self.ui.channelPlotGraph)
        self.ui.channelPlotGraph.setBackground((250,250,250))

    def set_plot(self, reset=False):
        channels = self.openbci_conn.constants.CHANNEL_IDS
        # Gráfica EEG

        #self.channelPlotGraph.setLabel('bottom', 'Samples', units='n')        #Etiqueta del eje inferior
        # Selecciona los elementos a mostrar
        #self.channelPlotGraph.getAxis('left').setTicks([[((i+1)*100,channels[i]) for i in range(self.CHANNELS_PER_GRAPH)]])              #([[(100, channels[0]), (200, channels[1])]])
        self.ui.channelPlotGraph.setYRange(-100, 100*(2+self.CHANNELS_PER_GRAPH), padding=0)

        # Fija los valores de los ejes
        self.ui.channelPlotGraph.setXRange(0, self.openbci_conn.constants.LARGE_WINDOW, padding=0)
        self.ui.channelPlotGraph.setLimits(xMin=0, xMax=self.openbci_conn.constants.LARGE_WINDOW)
        #self.channelPlotGraph.showGrid(False, False, alpha=0.3)  # Mostrar cuadrícula
        self.ui.channelPlotGraph.hideAxis("bottom")
        self.ui.channelPlotGraph.hideAxis("left")

        # Crear temporizadores para actualizar las gráficas
        # Temporizador del gráfico de las señales de los sensores = Electroencefaloframa
        self.eeg_channel_timer = QtCore.QTimer()
        self.eeg_channel_timer.setTimerType(QtCore.Qt.PreciseTimer)     #Tipo de temporizador que tiene precisión de milisegundos
        self.eeg_channel_timer.timeout.connect(self.channel_plot_update)         #Función se ejecuta cuando la temporización finaliza
        #self.eeg_channel_timer.start(self.openbci_conn.constants.refresh_rate)

    def channel_plot_update(self):
        for i in range(self.CHANNELS_PER_GRAPH):
            self.channelCurve[i].setData(self.openbci_conn.gui.last_sample[i+5,:])#= self.openbci_conn.gui.curves_EEG[i]#
