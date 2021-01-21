# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore

from GUI.ui_set_channel import Ui_Dialog

class SetChannelDialog(QtWidgets.QDialog):
    def __init__(self, parent, title, callback):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.channelSpinBox.setValue(parent.actualChannel)
        self.callback = callback
        self.ui.buttonBox.accepted.connect(self.set_new_channel)

    def set_new_channel(self):
        self.new_channel = self.ui.channelSpinBox.value()
        self.callback(self.new_channel)
