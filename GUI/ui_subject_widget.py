# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 140)
        Form.setMinimumSize(QtCore.QSize(1100, 110))
        Form.setMaximumSize(QtCore.QSize(1200, 140))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(12, 9, -1, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.idLabel = QtWidgets.QLabel(self.frame)
        self.idLabel.setObjectName("idLabel")
        self.verticalLayout_5.addWidget(self.idLabel)
        self.detailsButton = QtWidgets.QPushButton(self.frame)
        self.detailsButton.setObjectName("detailsButton")
        self.verticalLayout_5.addWidget(self.detailsButton)
        self.recordHBoxLayout = QtWidgets.QHBoxLayout()
        self.recordHBoxLayout.setObjectName("recordHBoxLayout")
        self.recordButton = QtWidgets.QPushButton(self.frame)
        self.recordButton.setEnabled(True)
        self.recordButton.setObjectName("recordButton")
        self.recordHBoxLayout.addWidget(self.recordButton)
        self.saveRecordButton = QtWidgets.QPushButton(self.frame)
        self.saveRecordButton.setEnabled(False)
        self.saveRecordButton.setObjectName("saveRecordButton")
        self.recordHBoxLayout.addWidget(self.saveRecordButton)
        self.verticalLayout_5.addLayout(self.recordHBoxLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.channelPlotGraph = PlotWidget(self.frame)
        self.channelPlotGraph.setMinimumSize(QtCore.QSize(800, 50))
        self.channelPlotGraph.setObjectName("channelPlotGraph")
        self.verticalLayout_14.addWidget(self.channelPlotGraph)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.showAllButton = QtWidgets.QPushButton(self.frame)
        self.showAllButton.setObjectName("showAllButton")
        self.horizontalLayout_19.addWidget(self.showAllButton)
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_19.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.frame)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_19.addWidget(self.pauseButton)
        self.portLabel = QtWidgets.QLabel(self.frame)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout_19.addWidget(self.portLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_19.addWidget(self.pushButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.idLabel.setText(_translate("Form", "Sujeto ID"))
        self.detailsButton.setText(_translate("Form", "Details"))
        self.recordButton.setText(_translate("Form", "Record"))
        self.saveRecordButton.setText(_translate("Form", "Save"))
        self.showAllButton.setText(_translate("Form", "Show all channels"))
        self.startButton.setText(_translate("Form", "Start"))
        self.pauseButton.setText(_translate("Form", "Pause"))
        self.portLabel.setText(_translate("Form", "portLabel"))
        self.pushButton.setText(_translate("Form", "Settings"))

from pyqtgraph import PlotWidget
