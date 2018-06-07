# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/newtype.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(845, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setGeometry(QtCore.QRect(160, 20, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Titre.setFont(font)
        self.Titre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Titre.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Titre.setTextFormat(QtCore.Qt.AutoText)
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")
        self.Enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.Enregistrer.setGeometry(QtCore.QRect(250, 460, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.Enregistrer.setFont(font)
        self.Enregistrer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Enregistrer.setMouseTracking(False)
        self.Enregistrer.setFlat(False)
        self.Enregistrer.setObjectName("Enregistrer")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 131, 71))
        self.logo.setMaximumSize(QtCore.QSize(282, 160))
        self.logo.setSizeIncrement(QtCore.QSize(1, 2))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.Nouveau_type = QtWidgets.QLabel(self.centralwidget)
        self.Nouveau_type.setGeometry(QtCore.QRect(520, 140, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Nouveau_type.setFont(font)
        self.Nouveau_type.setObjectName("Nouveau_type")
        self.nouveau_type = QtWidgets.QLineEdit(self.centralwidget)
        self.nouveau_type.setGeometry(QtCore.QRect(470, 190, 201, 31))
        self.nouveau_type.setObjectName("nouveau_type")
        self.types_affichage = QtWidgets.QTextBrowser(self.centralwidget)
        self.types_affichage.setGeometry(QtCore.QRect(150, 190, 211, 241))
        self.types_affichage.setObjectName("types_affichage")
        self.Types_existants = QtWidgets.QLabel(self.centralwidget)
        self.Types_existants.setGeometry(QtCore.QRect(200, 140, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Types_existants.setFont(font)
        self.Types_existants.setObjectName("Types_existants")
        gif = os.path.relpath("images/loader.gif")
        self.movie = QtGui.QMovie(gif)
        self.movie.setScaledSize(QtCore.QSize(31, 31))
        self.gif_label = QtWidgets.QLabel(self.centralwidget)
        self.gif_label.setGeometry(QtCore.QRect(410, 150, 31, 31))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 10, 31, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 26))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HARDIS Matériel"))
        self.Titre.setText(_translate("MainWindow", "Créer un nouveau type de matériel"))
        self.Enregistrer.setText(_translate("MainWindow", "Valider"))
        self.Nouveau_type.setText(_translate("MainWindow", "Nouveau type"))
        self.Types_existants.setText(_translate("MainWindow", "Types existants"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

