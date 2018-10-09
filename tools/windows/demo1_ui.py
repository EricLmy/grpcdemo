# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(717, 558)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 90, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(110, 170, 480, 193))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def closeEvent(self, event):
        print("demo22333222")
        event.accept()

