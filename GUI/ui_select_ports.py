# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_ports.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 171)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.portsGroupBox = QtWidgets.QGroupBox(Dialog)
        self.portsGroupBox.setObjectName("portsGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.portsGroupBox)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, -1, 12, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.portsVBoxLayout = QtWidgets.QVBoxLayout()
        self.portsVBoxLayout.setObjectName("portsVBoxLayout")
        self.verticalLayout.addLayout(self.portsVBoxLayout)
        self.verticalLayout_2.addWidget(self.portsGroupBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.okCancelButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.okCancelButtonBox.setOrientation(QtCore.Qt.Vertical)
        self.okCancelButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelButtonBox.setObjectName("okCancelButtonBox")
        self.horizontalLayout.addWidget(self.okCancelButtonBox)

        self.retranslateUi(Dialog)
        self.okCancelButtonBox.accepted.connect(Dialog.accept)
        self.okCancelButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select port(s):"))

