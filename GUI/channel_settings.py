from PyQt5 import QtWidgets, QtCore

from GUI.ui_channel_settings import Ui_Form
from GUI.set_channel_dialog import SetChannelDialog

class SettingsWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__()
        self.parent = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.actualChannel = self.parent.openbci_conn.driver.get_channel()

        self.ui.getChannelButton.clicked.connect(self.get_channel)
        self.ui.setChannelButton.clicked.connect(self.set_channel)
        self.ui.setChannelOverrideButton.clicked.connect(self.set_channel_override)
        self.ui.getSystemStatusButton.clicked.connect(self.get_system_status)

    def get_channel(self):
        self.actualChannel = self.parent.openbci_conn.driver.get_channel()
        self.ui.channelLabel.setText(f"Channel: {self.actualChannel}")
        QtCore.QTimer.singleShot(5000, lambda: self.ui.channelLabel.setText(""))

    def get_system_status(self):
        if self.parent.openbci_conn.driver.get_system_status():
            self.ui.channelLabel.setText("Cython board and dongle paired succesfully")
        else:
            self.ui.channelLabel.setText("Cython board is not paired")
        QtCore.QTimer.singleShot(5000, lambda: self.ui.channelLabel.setText(""))

    def set_channel_general(self, title, callback):
        self.newChannelDialog = SetChannelDialog(self, "Set channel", self.parent.openbci_conn.driver.set_channel)
        if self.newChannelDialog.exec_():
            self.ui.channelLabel.setText(f"Channel changed succesfully: {self.newChannelDialog.new_channel}")
        else:
            self.ui.channelLabel.setText("Channel was not changed")
        QtCore.QTimer.singleShot(5000, lambda: self.ui.channelLabel.setText(""))

    def set_channel(self):
        self.set_channel_general("Set channel", self.parent.openbci_conn.driver.set_channel)

    def set_channel_override(self):
        self.set_channel_general("Set dongle channel only", self.parent.openbci_conn.driver.set_channel_override)
