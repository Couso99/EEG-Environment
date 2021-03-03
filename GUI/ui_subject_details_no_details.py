# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject_details_no_details.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoDetails(object):
    def setupUi(self, NoDetails):
        NoDetails.setObjectName("NoDetails")
        NoDetails.resize(400, 110)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(NoDetails)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.definePersonButton = QtWidgets.QPushButton(NoDetails)
        self.definePersonButton.setObjectName("definePersonButton")
        self.horizontalLayout.addWidget(self.definePersonButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NoDetails)
        QtCore.QMetaObject.connectSlotsByName(NoDetails)

    def retranslateUi(self, NoDetails):
        _translate = QtCore.QCoreApplication.translate
        NoDetails.setWindowTitle(_translate("NoDetails", "Details"))
        self.label.setText(_translate("NoDetails", "No subject selected yet!"))
        self.definePersonButton.setText(_translate("NoDetails", "Define subject"))

