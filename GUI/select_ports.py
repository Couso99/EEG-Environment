from PyQt5 import QtWidgets, QtCore, QtGui, uic

from COM.open_bci_GCPDS import OpenBCIBoard as openbci


Ui_PortSelection, _ = uic.loadUiType("GUI/select_ports_dialog.ui")

class PortSelection(QtWidgets.QDialog, Ui_PortSelection):
    def __init__(self, parent=None, portAndChannelTuples=None, active_ports=None):
        super().__init__(parent)
        Ui_PortSelection.__init__(self)
        self.setupUi(self)

        self.checkboxes = []
        self.selected_ports = []
        self.active_ports = active_ports if active_ports else []

        if not portAndChannelTuples:
            self.update_available_ports()
            self.make_checkboxes()
        else:
            print(portAndChannelTuples)
            print(type(portAndChannelTuples))

            print(portAndChannelTuples[0])
            print(portAndChannelTuples[1])
            self.available_ports = portAndChannelTuples[0]# for portAndChannelTuple in portAndChannelTuples]
            self.available_ports_channel = portAndChannelTuples[1]# for portAndChannelTuple in portAndChannelTuples]
            self.make_checkboxes(True)

        self.okCancelButtonBox.accepted.connect(self.update_selected_ports)

    def update_available_ports(self):
        self.available_ports = self.get_ports()

    def get_ports(self):
        return openbci.find_ports(self.active_ports)#["ttyUSB0","ttyUSB1","ttyUSB2"]

    def make_checkboxes(self, isSerialConnected=0):
        for i, port in enumerate(self.available_ports):
            if port in self.active_ports:
                continue
            self.checkboxes.append(QtWidgets.QCheckBox(self.portsGroupBox))
            if not isSerialConnected:
                channel_number = openbci.get_channel_from_port(port)
            else:
                channel_number = self.available_ports_channel[i]
            self.checkboxes[-1].setText(f"Canal {channel_number}")
            self.portsVBoxLayout.addWidget(self.checkboxes[-1])

    def update_selected_ports(self):
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.isChecked():
                self.selected_ports.append(self.available_ports[i])

        print("Selected ports:",self.selected_ports)
