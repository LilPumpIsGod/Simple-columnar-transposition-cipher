# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDev.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Developer(object):
    def setupUi(self, About_Developer):
        About_Developer.setObjectName("About_Developer")
        About_Developer.setEnabled(True)
        About_Developer.resize(280, 90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About_Developer.sizePolicy().hasHeightForWidth())
        About_Developer.setSizePolicy(sizePolicy)
        About_Developer.setMinimumSize(QtCore.QSize(280, 90))
        About_Developer.setMaximumSize(QtCore.QSize(280, 90))
        self.label = QtWidgets.QLabel(About_Developer)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(About_Developer)
        QtCore.QMetaObject.connectSlotsByName(About_Developer)

    def retranslateUi(self, About_Developer):
        _translate = QtCore.QCoreApplication.translate
        About_Developer.setWindowTitle(_translate("About_Developer", "Про розробника"))
        self.label.setText(_translate("About_Developer", "Програму розробив студент _ групи _"))


