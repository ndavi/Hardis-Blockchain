# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Hardis-Blockchain/ui/accueil.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accueil(object):
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.resize(845, 568)
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 70, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(240, 180, 171, 101))
        self.Register.setObjectName("Register")
        self.Move = QtWidgets.QPushButton(self.centralwidget)
        self.Move.setGeometry(QtCore.QRect(430, 180, 171, 101))
        self.Move.setObjectName("Move")
        self.Empty = QtWidgets.QPushButton(self.centralwidget)
        self.Empty.setGeometry(QtCore.QRect(430, 300, 171, 101))
        self.Empty.setObjectName("Empty")
        self.Query = QtWidgets.QPushButton(self.centralwidget)
        self.Query.setGeometry(QtCore.QRect(240, 300, 171, 101))
        self.Query.setObjectName("Query")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 131, 71))
        self.logo.setMaximumSize(QtCore.QSize(282, 160))
        self.logo.setSizeIncrement(QtCore.QSize(1, 2))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        Accueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        self.menuHardis_Materiel = QtWidgets.QMenu(self.menubar)
        self.menuHardis_Materiel.setObjectName("menuHardis_Materiel")
        self.menuEnregistrer_materiel = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrer_materiel.setObjectName("menuEnregistrer_materiel")
        self.menuDeplacer_materiel = QtWidgets.QMenu(self.menubar)
        self.menuDeplacer_materiel.setObjectName("menuDeplacer_materiel")
        self.menuConsulter = QtWidgets.QMenu(self.menubar)
        self.menuConsulter.setObjectName("menuConsulter")
        Accueil.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accueil)
        self.statusbar.setObjectName("statusbar")
        Accueil.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHardis_Materiel.menuAction())
        self.menubar.addAction(self.menuEnregistrer_materiel.menuAction())
        self.menubar.addAction(self.menuDeplacer_materiel.menuAction())
        self.menubar.addAction(self.menuConsulter.menuAction())

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "MainWindow"))
        self.Title.setText(_translate("Accueil", "<html><head/><body><p align=\"center\">HARDIS Matériel</p></body></html>"))
        self.Register.setText(_translate("Accueil", " Enregistrer \n"
"un équipement"))
        self.Move.setText(_translate("Accueil", "Déplacer \n"
"un équipement"))
        self.Empty.setText(_translate("Accueil", "Paramètres \n"
"du logiciel"))
        self.Query.setText(_translate("Accueil", "Consulter le\n"
" matériel enregistré"))
        self.menuHardis_Materiel.setTitle(_translate("Accueil", "Hardis Matériel"))
        self.menuEnregistrer_materiel.setTitle(_translate("Accueil", "Enregistrer matériel"))
        self.menuDeplacer_materiel.setTitle(_translate("Accueil", "Déplacement matériel"))
        self.menuConsulter.setTitle(_translate("Accueil", "Consulter matériel"))

