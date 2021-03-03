# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore, QtGui

from COM.open_bci_GCPDS import OpenBCIBoard as openbci
from GUI.ui_new_person import Ui_DetailsDialog

class NewPerson(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New subject")

        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)

        self.details = []

        self.ui.buttonBox.accepted.connect(self.update_person_details)

    def update_person_details(self):
        personID = self.ui.subjectIdLabel.text()
        self.details.append(personID)

        age = self.ui.ageSpinBox.value()
        self.details.append(age if age>=0 else None)

        sex = self.ui.sexComboBox.current_text()
        if sex == "M" or sex == "F":
            self.details.append(sex)
        else:
            self.details.append(None)
