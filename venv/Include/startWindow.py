# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartForm(object):
    def setupUi(self, StartForm):
        StartForm.setObjectName("StartForm")
        StartForm.resize(400, 300)
        StartForm.setMinimumSize(QtCore.QSize(400, 300))
        StartForm.setMaximumSize(QtCore.QSize(400, 300))
        self.pushButton_StartProg = QtWidgets.QPushButton(StartForm)
        self.pushButton_StartProg.setGeometry(QtCore.QRect(150, 230, 101, 23))
        self.pushButton_StartProg.setObjectName("pushButton_StartProg")
        self.label = QtWidgets.QLabel(StartForm)
        self.label.setGeometry(QtCore.QRect(280, 240, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StartForm)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"D:\Programs\Python\Projects\Course_Work_471.2\venv\Include\img.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton_StartProg.raise_()

        self.retranslateUi(StartForm)
        QtCore.QMetaObject.connectSlotsByName(StartForm)

    def retranslateUi(self, StartForm):
        _translate = QtCore.QCoreApplication.translate
        StartForm.setWindowTitle(_translate("StartForm", "Початок роботи"))
        self.pushButton_StartProg.setText(_translate("StartForm", "Розпочати роботу"))
        self.label.setText(_translate("StartForm", "Розробив студент _ групи _"))


