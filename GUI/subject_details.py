# Author: Pablo Couso (cousop@gmail.com)
from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.select_subject import SubjectSelection

from GUI.ui_subject_details_no_details import Ui_NoDetails
from GUI.ui_subject_details_show import Ui_Details

class NoDetails(QtWidgets.QWidget):
    def __init__(self, parent):
        super(NoDetails, self).__init__(parent)
        self.ui = Ui_NoDetails()
        self.ui.setupUi(self)
        self.ui.definePersonButton.clicked.connect(parent.select_subject)
        self.ui.okButton.clicked.connect(parent.close)

class Details(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Details, self).__init__(parent)
        self.ui = Ui_Details()
        self.ui.setupUi(self)
        self.ui.definePersonButton.clicked.connect(parent.select_subject)
        self.ui.okButton.clicked.connect(parent.close)

class SubjectDetails(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.details = []

        self.resize(300,150)
        self.stackedWidget = QtGui.QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.no_details = NoDetails(self)
        self.stackedWidget.addWidget(self.no_details)
        self.yes_details = Details(self)
        self.stackedWidget.addWidget(self.yes_details)

        self.update_details()

    def update_details(self):
        if self.parent.personID:
            self.stackedWidget.setCurrentIndex(1)
            #self.ui = Ui_Details()
            self.details = self.parent.db.get_person_details(self.parent.personID)
            if self.details:
                self.yes_details.ui.subjectIdLabel.setText(self.details[0])
                self.yes_details.ui.ageLabel.setText(str(self.details[1]))
                self.yes_details.ui.sexLabel.setText(self.details[2])

        else:
            self.stackedWidget.setCurrentIndex(0)
            self.details = []

    def select_subject(self):
        self.selectSubjectDialog = SubjectSelection(self.parent.db)

        if self.selectSubjectDialog.exec_():
            personID = self.selectSubjectDialog.personID
            self.parent.personID = personID
            self.parent.update_subject_label()
            self.update_details()
