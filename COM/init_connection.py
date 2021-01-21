# Modified by: Pablo Couso (cousop@gmail.com)
# IMPORTAR MÓDULOS
# Módulos Propios
from GENERAL.data_manager_openBCI import data_manager_openBCI        #Aplicación de los filtros a las medidas
from LOGGING import logger as log                                       #Modifica el log --> OpenBCI (driver)
from GENERAL.ring_buffer import RingBuffer as buffer                 #Gestiona el buffer de datos de los sensores
from GENERAL.constants import constants                              #Constantes de configuración del proceso --> Buffer, Trig_Server, SaveFile
from COM.open_bci_GCPDS import OpenBCIBoard as openBCI
from GUI.GUI_bci import GUI
from GENERAL.slots_manager import SlotsManager                          #Manejo de Lista de callbacks --> Buffer
from GENERAL.recording_manager import recording_manager              #Grabación de medidas para guardarlos en un archivo EDF
from EDF.writeEDFFile import edf_writter

# Módulos Externos
from PyQt5 import QtWidgets
from multiprocessing import Queue, Value


class OpenBCI_connection:
    def __init__(self, parent, port):
        ############# LOGIC CONTROL ##################
        self.isconnected = Value('b', 0)                    #Devuelve una "Envoltura de Sincronización" de tipo byte con valor 1

        self.parent = parent
        self.port = port

        # Iniciar Constantes
        self.constants = constants()

        # Escritor para archivos edf
        self.writter = edf_writter(self.constants)

        ######### slots manager for multiple callbacks settings #############
        self.slots = SlotsManager()

        # Iniciar Encolamiento
        self.queue = Queue()
        self.queue_even = Queue()
        self.queue_odd = Queue()

        # Iniciar buffer donde se guardan los datos de los sensores
        self.buffer = buffer(self.constants)
        self.buffer.emitter.connect(self.slots.trigger)     ##### Ejecuta el evento para los callbacks??

        # Iniciar manejo de datos
        self.eeg_dmg = data_manager_openBCI(self)           #Envía toda la clase MYAPP
        self.eeg_dmg.start()

        # Iniciar interfaz TCP/IP para adquisición de datos
        self.recording_manager = recording_manager(self)        #Introduce la propia aplicación

        # Iniciar Aplicación GUI: envía la aplicación completa y una lista de callbacks
        # CALLBACKS: conjunto de acciones ante las que debe dar una respuesta = conexión, adquisición, actualización, guardar o cargar/abrir
        self.gui = GUI(self, callbacks = [self.connection_manager, self.recording_manager.test_acquisition, self.recording_manager.update_state, self.save_fname_and_start_record])

        ########## LOGGER ####################
        self.log = log.logger(self.gui)         #Introducir la aplicación GUI previamente creada

        # Iniciar Driver
        self.driver = openBCI(self, self.queue, self.queue_even, self.queue_odd, self.recording_manager.streaming, self.isconnected, self.log, port=self.port)     #Introduce la cola, los estados del streaming y de conexión y el logger
        self.driver.start()

    def terminate(self):
        self.eeg_dmg.close_thread()
        self.eeg_dmg.join()
        self.queue.close()
        self.queue_even.close()
        self.queue_odd.close()
        self.gui.stop_plots()
        self.driver.end_process()

    def showAllChannels(self):
        self.gui.MainWindow.show()

    # Conexión con el dispositivo
    def connection_manager(self):
        # Si no está conectado, intenta conectarse al dispositivo y activa los filtros internos de la tarjeta
        if not self.isconnected.value:
            self.driver.connect()
            self.driver.enable_filters()
        # Si está conectado, se desconecta
        else:
            self.driver.disconnect()

    def start_record(self):
        self.app.eeg_dmg.reset_data_store()
        self.app.driver.send_start()
        #self.app.gui.eeg_timer.start(self.app.constants.refresh_rate)
        #self.app.gui.eeg_short_timer.start(self.app.constants.short_refresh_rate)
        #self.app.gui.freq_timer.start(self.app.constants.refresh_rate)

    # Guardar archivo
    def save_fname_and_start_record(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.gui.MainWindow,"Save EDF(+) file","","EDF Files (*.edf)", options=options)
        if fileName:
            self.constants.PATH = fileName
            self.constants.ispath = True
            self.recording_manager.update_state('start')
            #self.writter.new_file(self.constants.PATH)
            #self.writter.append(self.gui.curves_EEG)
            #self.writter.writeToEDF()
            #self.writter.close_file()

    def stop_recording(self):
        if self.constants.ispath:
            self.constants.ispath = False
            self.recording_manager.update_state("stop")
