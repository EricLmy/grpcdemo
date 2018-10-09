# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(683, 498)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 90, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(360, 100, 117, 25))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(360, 150, 97, 25))
        self.checkBox.setObjectName("checkBox")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(370, 220, 187, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))

