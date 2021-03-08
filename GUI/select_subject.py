# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore

from GUI.ui_select_subject import Ui_SubjectSelection
from GUI.new_person_dialog import NewPerson

class SubjectSelection(QtWidgets.QDialog):
    def __init__(self, db):#):
        super().__init__()
        self.ui = Ui_SubjectSelection()
        self.ui.setupUi(self)

        #self.parent = parent
        self.personID = None

        """try:
            self.db = parent.parent.db
        except Exception as e:
            self.db = parent.db"""
        self.db = db

        all_personId = self.db.get_all_personId()

        self.ui.subjectIdComboBox.addItems(all_personId)
        #if self.parent.personID:
            #self.ui.subjectIdComboBox.setText(self.parent.personID)
        self.ui.buttonBox.accepted.connect(self.set_person)
        self.ui.newSubjectButton.clicked.connect(self.define_new_person)

    def set_person(self):
        self.personID = self.ui.subjectIdComboBox.currentText()

    def define_new_person(self):
        self.newPerson = NewPerson()

        if self.newPerson.exec_():
            details = self.newPerson.details
            personID = details[0]
            edad = details[1]
            sexo = details[2]

            self.db.new_person(personID, edad, sexo)
            self.ui.subjectIdComboBox.addItem(personID)
            self.ui.subjectIdComboBox.itemText(self.ui.subjectIdComboBox.count()-1)
