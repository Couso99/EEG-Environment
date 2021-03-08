# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg

from COM.init_connection import OpenBCI_connection
from COM.open_bci_GCPDS import OpenBCIBoard as openbci

from GUI.channel_settings import SettingsWindow
from GUI.subject_details import SubjectDetails
from GUI.select_subject import SubjectSelection
from GUI.ui_subject_widget import Ui_Form

class SubjectWidget(QtWidgets.QWidget):
    def __init__(self, db, port):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.port = port
        self.ui.portLabel.setText(f"Canal {openbci.get_channel_from_port(port)}")

        self.CHANNELS_PER_GRAPH = 2

        self.db = db
        self.personID = None

        self.openbci_connect()
        self.init_channel_plot()

        self.ui.saveRecordButton.clicked.connect(self.openbci_conn.stop_recording)
        self.ui.showAllButton.clicked.connect(self.openbci_conn.showAllChannels)
        self.ui.recordButton.clicked.connect(self.start_recording)
        self.ui.startButton.clicked.connect(self.send_start)
        self.ui.pauseButton.clicked.connect(self.send_stop)
        self.ui.settingsButton.clicked.connect(self.open_settings)
        self.ui.detailsButton.clicked.connect(self.show_details)

    def openbci_disconnect(self):
        self.openbci_conn.terminate()
        self.deleteLater() #sip.delete(self.widget_name)
        self = None

    def openbci_connect(self):
        self.openbci_conn = OpenBCI_connection(self, self.port)

    def start_recording(self):
        if not self.openbci_conn.constants.ispath:
            self.openbci_conn.save_fname_and_start_record()
        if self.openbci_conn.constants.ispath:
            self.send_start()
            self.ui.recordButton.setEnabled(False)
            self.ui.saveRecordButton.setEnabled(True)

    def stop_recording(self):
        if self.openbci_conn.constants.ispath:
            self.openbci_conn.stop_recording()
            self.send_stop()
        self.ui.recordButton.setEnabled(True)
        self.ui.saveRecordButton.setEnabled(False)
        while not self.personID:
            self.selectPerson = SubjectSelection(self.db)

            if self.selectPerson.exec_():
                personID = self.selectPerson.personID
                self.personID = personID
        self.db.new_session(self.personID, self.openbci_conn.constants.PATH)

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

    def open_settings(self):
        self.settingsWindow = SettingsWindow(self)
        self.settingsWindow.show()

    def show_details(self):
        self.detailsWindow = SubjectDetails(self)
        self.detailsWindow.show()

    def update_subject_label(self):
        self.ui.subjectIdLabel.setText(self.personID)


    """
    def define_person(self, personID):
        self.personID = personID

    def define_new_person(self):
        self.newPerson = NewPerson()

        if self.newPerson.exec_():
            details = self.newPerson.details
            edad = details[0]
            sexo = details[1]

            self.db.new_person(personID, edad, sexo)
            self.define_person(personID)"""

    def init_channel_plot(self):
        self.channelCurve = []
        self.ui.channelPlotGraph.clear()

        for i in range(self.CHANNELS_PER_GRAPH):
            c = pg.PlotCurveItem(pen = (i, self.CHANNELS_PER_GRAPH*1.3))
            c.setPos(0, 0)
            self.ui.channelPlotGraph.addItem(c)  #Agregar la curva al widget
            self.channelCurve.append(c)           #Se asocia los valores a la gráfica

        self.set_plot()

        #self.openbci_conn.gui.styleQwtPlot('EEG one channel', self.ui.channelPlotGraph)
        self.ui.channelPlotGraph.setBackground((250,250,250))

    def set_plot(self):
        channels = self.openbci_conn.constants.CHANNEL_IDS
        # Gráfica EEG

        # Selecciona los elementos a mostrar
        self.ui.channelPlotGraph.setYRange(100, 500*(2+self.CHANNELS_PER_GRAPH), padding=0)

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
