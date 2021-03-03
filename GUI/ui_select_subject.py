# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_subject.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubjectSelection(object):
    def setupUi(self, SubjectSelection):
        SubjectSelection.setObjectName("SubjectSelection")
        SubjectSelection.resize(416, 112)
        self.gridLayout = QtWidgets.QGridLayout(SubjectSelection)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(SubjectSelection)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SubjectSelection)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.subjectIdComboBox = QtWidgets.QComboBox(SubjectSelection)
        self.subjectIdComboBox.setObjectName("subjectIdComboBox")
        self.horizontalLayout.addWidget(self.subjectIdComboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.newSubjectButton = QtWidgets.QPushButton(SubjectSelection)
        self.newSubjectButton.setObjectName("newSubjectButton")
        self.gridLayout.addWidget(self.newSubjectButton, 1, 2, 1, 1)

        self.retranslateUi(SubjectSelection)
        self.buttonBox.accepted.connect(SubjectSelection.accept)
        self.buttonBox.rejected.connect(SubjectSelection.reject)
        QtCore.QMetaObject.connectSlotsByName(SubjectSelection)

    def retranslateUi(self, SubjectSelection):
        _translate = QtCore.QCoreApplication.translate
        SubjectSelection.setWindowTitle(_translate("SubjectSelection", "Select subjects"))
        self.label.setText(_translate("SubjectSelection", "ID:"))
        self.newSubjectButton.setText(_translate("SubjectSelection", "New subject"))

