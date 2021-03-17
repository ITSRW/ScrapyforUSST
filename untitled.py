# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 300)
        Form.setMinimumSize(QtCore.QSize(471, 300))
        Form.setMaximumSize(QtCore.QSize(471, 300))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 90, 451, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 0, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 0, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 0, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.path = QtWidgets.QLineEdit(Form)
        self.path.setGeometry(QtCore.QRect(110, 50, 351, 21))
        self.path.setObjectName("path")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 130, 451, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.info = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.info.setGeometry(QtCore.QRect(0, 0, 451, 161))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.info.setFont(font)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.term = QtWidgets.QComboBox(Form)
        self.term.setGeometry(QtCore.QRect(110, 20, 351, 22))
        self.term.setObjectName("term")
        for index in range(-1,9):

            self.term.addItem(
                (str)(datetime.datetime.now().year-index-1)+"-"+(str)(datetime.datetime.now().year-index)+"-2",
                (str)(datetime.datetime.now().year-1-index)+"-"+(str)(datetime.datetime.now().year-index)+"-2")
            self.term.addItem(
                (str)(datetime.datetime.now().year - 1-index) + "-" + (str)(datetime.datetime.now().year-index) + "-1",
                (str)(datetime.datetime.now().year - 1-index) + "-" + (str)(datetime.datetime.now().year-index) + "-1")



        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.quit)
        self.pushButton_2.clicked.connect(Form.termi)
        self.pushButton.clicked.connect(Form.acti)
        self.info.textChanged.connect(Form.totheend)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Active"))
        self.pushButton_2.setText(_translate("Form", "Terminate"))
        self.pushButton_3.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "Save Path"))
        self.path.setText(_translate("Form", "C:/Users/83810/Desktop/2019_2020_1 USST开课信息爬取.xls"))
        self.label_2.setText(_translate("Form", "Term Select"))
