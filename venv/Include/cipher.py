import re
import math
import string
import random
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow  # импорт нашего сгенерированного файла
from aboutDev import Ui_About_Developer
from helpWindow import Ui_helpForm
from startWindow import Ui_StartForm

#Main code of app

class Mywindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Mywindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Encrypt.clicked.connect(self.encryption)
        self.ui.pushButton_Decrypt.clicked.connect(self.decryption)
        self.ui.pushButton_SavetoFile.clicked.connect(self.writeFile)
        self.ui.pushButton_ReadfromFile.clicked.connect(self.readFile)


        self.ui.action_AboutDev.triggered.connect(self.openAboutDev)
        self.ui.action_Help.triggered.connect(self.openHelp)


        def openMenu(position):

            menu = QMenu()
            quitAction = menu.addAction("Quit")
            action = menu.exec_(tableWidget.mapToGlobal(position))
            if action == quitAction:
                qApp.quit()

    def encryption(self):
        print("begin - encr")
        text = str(self.ui.plainTextEdit_Encr.toPlainText())
        print(text)
        text = re.sub(r'\W+', '', text)
        if (text.__len__() % 6 != 0):
            trashVal = math.ceil(text.__len__() / 6) * 6 - text.__len__()
            print(trashVal)
            for x in range(trashVal):
                text += random.choice(string.ascii_letters)
        print(text)
        encrypt = ""
        for x in range(6):
            encrypt += text[x::6]
        print(encrypt)
        self.ui.textBrowser_Encrypt.setText(encrypt)

    def decryption(self):
        print("begin - decr")
        text = self.ui.plainTextEdit_Decr.toPlainText()
        decrypt = ""
        for x in range(math.ceil(text.__len__() / 6)):
            decrypt += text[x::math.ceil(text.__len__() / 6)]
        print(decrypt)
        self.ui.textBrowser_Decrypt.setText(decrypt)


    def openAboutDev(self):
        self.application1 = AboutDevWindow()
        self.application1.show()

    def openHelp(self):
        self.application1 = HelpWindow()
        self.application1.show()

    def writeFile(self):
        with open("savedFile.txt", "w") as file:
            file.write(self.ui.textBrowser_Decrypt.toPlainText())

    def readFile(self):
        with open("readFile.txt","r") as file:
            text = str(file.readlines())
        text = re.sub(r'\W+', '', text)
        print(text)
        if (text.__len__() % 6 != 0):
            trashVal = math.ceil(text.__len__() / 6) * 6 - text.__len__()
            for x in range(trashVal):
                text += random.choice(string.ascii_letters)
        encrypt = ""
        for x in range(6):
            encrypt += text[x::6]
        self.ui.textBrowser_Encrypt.setText(encrypt)


class AboutDevWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutDevWindow, self).__init__()
        self.ui = Ui_About_Developer()
        self.ui.setupUi(self)


class HelpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.ui = Ui_helpForm()
        self.ui.setupUi(self)

class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_StartForm()
        self.ui.setupUi(self)

        self.ui.pushButton_StartProg.clicked.connect(self.openMainWin)

    def openMainWin(self):
        application.hide()
        self.application = Mywindow()
        self.application.show()


if __name__=="__main__":
    app = QtWidgets.QApplication([])
    application = StartWindow()
    application.show()
    sys.exit(app.exec())

