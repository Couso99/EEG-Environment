# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject_details_show.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Details(object):
    def setupUi(self, Details):
        Details.setObjectName("Details")
        Details.resize(400, 136)
        self.verticalLayout = QtWidgets.QVBoxLayout(Details)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Details)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ageLabel = QtWidgets.QLabel(Details)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Details)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.subjectIdLabel = QtWidgets.QLabel(Details)
        self.subjectIdLabel.setObjectName("subjectIdLabel")
        self.gridLayout.addWidget(self.subjectIdLabel, 0, 1, 1, 1)
        self.sexLabel = QtWidgets.QLabel(Details)
        self.sexLabel.setObjectName("sexLabel")
        self.gridLayout.addWidget(self.sexLabel, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Details)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.definePersonButton = QtWidgets.QPushButton(Details)
        self.definePersonButton.setObjectName("definePersonButton")
        self.horizontalLayout.addWidget(self.definePersonButton)
        self.okButton = QtWidgets.QPushButton(Details)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Details)
        QtCore.QMetaObject.connectSlotsByName(Details)

    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Details"))
        self.label_2.setText(_translate("Details", "Age:"))
        self.ageLabel.setText(_translate("Details", "TextLabel"))
        self.label_3.setText(_translate("Details", "Sex:"))
        self.subjectIdLabel.setText(_translate("Details", "TextLabel"))
        self.sexLabel.setText(_translate("Details", "TextLabel"))
        self.label.setText(_translate("Details", "ID:"))
        self.definePersonButton.setText(_translate("Details", "New subject"))
        self.okButton.setText(_translate("Details", "Ok"))

