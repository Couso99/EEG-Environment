# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore

from GUI.select_subject import SubjectSelection

from GUI.subject_details_no_details import Ui_NoDetails
from GUI.subject_details_show import Ui_Details

class SubjectDetails(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.details = []
        self.update_details()

    def update_details(self):
        if self.parent.personID:
            self.ui = Ui_Details()
            self.details = self.parent.db.get_person_details(self.parent.personID)
        else:
            self.ui = Ui_NoDetails()
            self.details = []

        self.ui.setupUi(self)

        if self.details:
            self.ui.sujetoIdLabel.setText(self.details[0])
            self.ui.ageLabel.setText(self.details[1])
            self.ui.sexLabel.setText(self.details[2])

        self.ui.definePersonButton.clicked.connect(self.select_subject)


    def select_subject(self):
        self.selectSubjectDialog = SubjectSelection(self.parent.db)

        if self.selectSubjectDialog.exec_():
            personID = self.selectSubjectDialog.personID
            self.parent.personID = personID
            self.parent.update_subject_label()
            self.update_details()
