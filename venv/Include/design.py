# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(497, 346)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(497, 346))
        MainWindow.setMaximumSize(QtCore.QSize(497, 346))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 91, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Encrypt.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.pushButton_Encrypt.setObjectName("pushButton_Encrypt")
        self.pushButton_Decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Decrypt.setGeometry(QtCore.QRect(270, 140, 75, 23))
        self.pushButton_Decrypt.setObjectName("pushButton_Decrypt")
        self.textBrowser_Encrypt = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Encrypt.setGeometry(QtCore.QRect(20, 180, 171, 81))
        self.textBrowser_Encrypt.setObjectName("textBrowser_Encrypt")
        self.textBrowser_Decrypt = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Decrypt.setGeometry(QtCore.QRect(270, 180, 171, 81))
        self.textBrowser_Decrypt.setObjectName("textBrowser_Decrypt")
        self.plainTextEdit_Encr = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Encr.setGeometry(QtCore.QRect(20, 50, 171, 71))
        self.plainTextEdit_Encr.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.plainTextEdit_Encr.setAutoFillBackground(False)
        self.plainTextEdit_Encr.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit_Encr.setObjectName("plainTextEdit_Encr")
        self.plainTextEdit_Decr = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Decr.setGeometry(QtCore.QRect(270, 50, 171, 71))
        self.plainTextEdit_Decr.setObjectName("plainTextEdit_Decr")
        self.pushButton_ReadfromFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ReadfromFile.setGeometry(QtCore.QRect(20, 270, 111, 23))
        self.pushButton_ReadfromFile.setObjectName("pushButton_ReadfromFile")
        self.pushButton_SavetoFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SavetoFile.setGeometry(QtCore.QRect(270, 270, 111, 23))
        self.pushButton_SavetoFile.setObjectName("pushButton_SavetoFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_AboutDev = QtWidgets.QAction(MainWindow)
        self.action_AboutDev.setObjectName("action_AboutDev")
        self.action_Help = QtWidgets.QAction(MainWindow)
        self.action_Help.setObjectName("action_Help")
        self.menu.addAction(self.action_AboutDev)
        self.menu.addAction(self.action_Help)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Шифрувати"))
        self.label_2.setText(_translate("MainWindow", "Дешифрувати"))
        self.pushButton_Encrypt.setText(_translate("MainWindow", "Виконати"))
        self.pushButton_Decrypt.setText(_translate("MainWindow", "Виконати"))
        self.plainTextEdit_Encr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Для вводу пробілу використовуйте знак &quot;_&quot;.</p></body></html>"))
        self.pushButton_ReadfromFile.setText(_translate("MainWindow", "Прочитати з файлу"))
        self.pushButton_SavetoFile.setText(_translate("MainWindow", "Зберегти в файл"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.action_AboutDev.setText(_translate("MainWindow", "Про розробника"))
        self.action_Help.setText(_translate("MainWindow", "Довідка"))


