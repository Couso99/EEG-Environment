# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(396, 172)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 2)
        self.getChannelButton = QtWidgets.QPushButton(Form)
        self.getChannelButton.setObjectName("getChannelButton")
        self.gridLayout.addWidget(self.getChannelButton, 3, 0, 1, 1)
        self.getSystemStatusButton = QtWidgets.QPushButton(Form)
        self.getSystemStatusButton.setObjectName("getSystemStatusButton")
        self.gridLayout.addWidget(self.getSystemStatusButton, 3, 1, 1, 1)
        self.setChannelButton = QtWidgets.QPushButton(Form)
        self.setChannelButton.setObjectName("setChannelButton")
        self.gridLayout.addWidget(self.setChannelButton, 4, 0, 1, 1)
        self.setChannelOverrideButton = QtWidgets.QPushButton(Form)
        self.setChannelOverrideButton.setObjectName("setChannelOverrideButton")
        self.gridLayout.addWidget(self.setChannelOverrideButton, 4, 1, 1, 1)
        self.channelLabel = QtWidgets.QLabel(Form)
        self.channelLabel.setText("")
        self.channelLabel.setObjectName("channelLabel")
        self.gridLayout.addWidget(self.channelLabel, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Radio Configuration"))
        self.getChannelButton.setText(_translate("Form", "Get Channel"))
        self.getSystemStatusButton.setText(_translate("Form", "System Status"))
        self.setChannelButton.setText(_translate("Form", "Set Channel"))
        self.setChannelOverrideButton.setText(_translate("Form", "Set Channel Override"))

