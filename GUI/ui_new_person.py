# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_person_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DetailsDialog(object):
    def setupUi(self, DetailsDialog):
        DetailsDialog.setObjectName("DetailsDialog")
        DetailsDialog.resize(365, 214)
        self.verticalLayout = QtWidgets.QVBoxLayout(DetailsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DetailsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.sexComboBox = QtWidgets.QComboBox(DetailsDialog)
        self.sexComboBox.setObjectName("sexComboBox")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.gridLayout.addWidget(self.sexComboBox, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DetailsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.ageSpinBox = QtWidgets.QSpinBox(DetailsDialog)
        self.ageSpinBox.setMinimum(-1)
        self.ageSpinBox.setMaximum(150)
        self.ageSpinBox.setProperty("value", -1)
        self.ageSpinBox.setObjectName("ageSpinBox")
        self.gridLayout.addWidget(self.ageSpinBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DetailsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.subjectIDLabel = QtWidgets.QLineEdit(DetailsDialog)
        self.subjectIDLabel.setObjectName("subjectIDLabel")
        self.gridLayout.addWidget(self.subjectIDLabel, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DetailsDialog)
        self.buttonBox.accepted.connect(DetailsDialog.accept)
        self.buttonBox.rejected.connect(DetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DetailsDialog)

    def retranslateUi(self, DetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        DetailsDialog.setWindowTitle(_translate("DetailsDialog", "Dialog"))
        self.label.setText(_translate("DetailsDialog", "Edad:"))
        self.sexComboBox.setItemText(0, _translate("DetailsDialog", "No especificar"))
        self.sexComboBox.setItemText(1, _translate("DetailsDialog", "M"))
        self.sexComboBox.setItemText(2, _translate("DetailsDialog", "F"))
        self.label_2.setText(_translate("DetailsDialog", "Sexo:"))
        self.label_3.setText(_translate("DetailsDialog", "Subject ID:"))

