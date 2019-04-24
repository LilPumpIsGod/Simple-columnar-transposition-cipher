# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpForm(object):
    def setupUi(self, helpForm):
        helpForm.setObjectName("helpForm")
        helpForm.setEnabled(True)
        helpForm.resize(356, 186)
        self.label = QtWidgets.QLabel(helpForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(helpForm)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 311, 51))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(helpForm)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 301, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(helpForm)
        QtCore.QMetaObject.connectSlotsByName(helpForm)

    def retranslateUi(self, helpForm):
        _translate = QtCore.QCoreApplication.translate
        helpForm.setWindowTitle(_translate("helpForm", "Довідка"))
        self.label.setText(_translate("helpForm", "Програма шифрації простим стовпчиковим перестановочним шифром."))
        self.label_2.setText(_translate("helpForm", "Для шифрування даних введіть данні в поле вводу та натиснуть кнопку, після з\'явиться зашифрований текст. Або виберіть файл для шифрації даних з файлу."))
        self.label_3.setText(_translate("helpForm", "Для дешифрації введіть шифр в поле вводу та натиснуть кнопку \"Виконати\", після з\'явиться розшифрований текст. Розшифрований текст можна зберегти в файл."))


