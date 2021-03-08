# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_person_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewPerson(object):
    def setupUi(self, NewPerson):
        NewPerson.setObjectName("NewPerson")
        NewPerson.resize(365, 214)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewPerson)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(NewPerson)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.sexComboBox = QtWidgets.QComboBox(NewPerson)
        self.sexComboBox.setObjectName("sexComboBox")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.gridLayout.addWidget(self.sexComboBox, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(NewPerson)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.ageSpinBox = QtWidgets.QSpinBox(NewPerson)
        self.ageSpinBox.setMinimum(-1)
        self.ageSpinBox.setMaximum(150)
        self.ageSpinBox.setProperty("value", -1)
        self.ageSpinBox.setObjectName("ageSpinBox")
        self.gridLayout.addWidget(self.ageSpinBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(NewPerson)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.subjectIdLabel = QtWidgets.QLineEdit(NewPerson)
        self.subjectIdLabel.setObjectName("subjectIdLabel")
        self.gridLayout.addWidget(self.subjectIdLabel, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewPerson)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPerson)
        self.buttonBox.accepted.connect(NewPerson.accept)
        self.buttonBox.rejected.connect(NewPerson.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPerson)

    def retranslateUi(self, NewPerson):
        _translate = QtCore.QCoreApplication.translate
        NewPerson.setWindowTitle(_translate("NewPerson", "Dialog"))
        self.label.setText(_translate("NewPerson", "Edad:"))
        self.sexComboBox.setItemText(0, _translate("NewPerson", "No especificar"))
        self.sexComboBox.setItemText(1, _translate("NewPerson", "M"))
        self.sexComboBox.setItemText(2, _translate("NewPerson", "F"))
        self.label_2.setText(_translate("NewPerson", "Sexo:"))
        self.label_3.setText(_translate("NewPerson", "Subject ID:"))

