from PyQt5 import QtWidgets, QtCore, QtGui, uic

from GUI.subject_widget import SubjectWidget
from GUI.select_ports import PortSelection
from GUI.ui_main_windsow import Ui_MainWindow

#Ui_MainWindow, _ = uic.loadUiType("GUI/main_window.ui")

class EnvironmentWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

        self.subjects = []
        self.active_ports = []

        self.ui.addButton.clicked.connect(self.add_subject)
        self.ui.deleteButton.clicked.connect(self.remove_subject)

    def add_subject(self):
        self.portSelection = PortSelection(active_ports=self.active_ports)
        ports = []
        if self.portSelection.exec_():
            ports = self.portSelection.selected_ports
        # Se van añadiendo nuevos widgets, el indice 0 se situa arriba del layout
        for port in ports:
            # Check if port selected is already shown
            if port in self.active_ports:
                continue
            self.active_ports.append(port)
            new_widget = SubjectWidget(port)
            self.subjects.append(new_widget)
            self.ui.allSubjectsLayout.addWidget(self.subjects[-1])

    def remove_subject(self):
        self.portSelection = PortSelection(portAndChannelTuples=(self.active_ports, [widget.portLabel.text() for widget in self.subjects]))
        ports = []
        if self.portSelection.exec_():
            ports = self.portSelection.selected_ports

        for port in ports:
            index = self.active_ports.index(port)
            self.ui.allSubjectsLayout.removeWidget(self.subjects[index])
            self.subjects[index].openbci_disconnect()
            del self.active_ports[index]
            del self.subjects[index]

    def close_all(self):
        for i, port in enumerate(self.active_ports):
            print("port removed:",port)
            self.ui.allSubjectsLayout.removeWidget(self.subjects[i])
            self.subjects[i].openbci_disconnect()
        del self.active_ports
        del self.subjects
