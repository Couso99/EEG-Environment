# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1250, 628)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.bottomHBoxLayout = QtWidgets.QHBoxLayout()
        self.bottomHBoxLayout.setObjectName("bottomHBoxLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.bottomHBoxLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setMinimumSize(QtCore.QSize(51, 0))
        self.deleteButton.setObjectName("deleteButton")
        self.bottomHBoxLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomHBoxLayout.addItem(spacerItem)
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setObjectName("signInButton")
        self.bottomHBoxLayout.addWidget(self.signInButton)
        self.gridLayout.addLayout(self.bottomHBoxLayout, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 2044, 611))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.allSubjectsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.allSubjectsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.allSubjectsLayout.setContentsMargins(0, 0, 0, 0)
        self.allSubjectsLayout.setObjectName("allSubjectsLayout")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.deleteButton.setText(_translate("MainWindow", "-"))
        self.signInButton.setText(_translate("MainWindow", "Sign in"))

