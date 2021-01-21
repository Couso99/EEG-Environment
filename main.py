# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets
import sys

from GUI.main_window import EnvironmentWindow

class EnvironmentApp(QtWidgets.QApplication):
    # Inicialización
    def __init__(self):
        QtWidgets.QApplication.__init__(self, [''])         #Inicia la aplicación de QT

        self.window = EnvironmentWindow()
        #with open("GUI/style.css") as f:
        #    self.app.setStyleSheet(f.read())
        self.aboutToQuit.connect(self.window.close_all)



if __name__ == '__main__':
    app = EnvironmentApp()
    app.window.show()
    app.exec_()

    #sys.exec("pkill -9 ")
