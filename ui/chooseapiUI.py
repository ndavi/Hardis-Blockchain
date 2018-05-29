# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/chooseapi.ui'
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
        self.Multichain = QtWidgets.QPushButton(self.centralwidget)
        self.Multichain.setGeometry(QtCore.QRect(240, 280, 171, 101))
        self.Multichain.setObjectName("Multichain")
        self.IOTA = QtWidgets.QPushButton(self.centralwidget)
        self.IOTA.setGeometry(QtCore.QRect(430, 280, 171, 101))
        self.IOTA.setObjectName("IOTA")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 131, 71))
        self.logo.setMaximumSize(QtCore.QSize(282, 160))
        self.logo.setSizeIncrement(QtCore.QSize(1, 2))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../../Hardis-Blockchain/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.logout = QtWidgets.QLabel(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(816, 10, 21, 21))
        self.logout.setText("")
        self.logout.setPixmap(QtGui.QPixmap("../../Hardis-Blockchain/log-out.jpg"))
        self.logout.setScaledContents(True)
        self.logout.setObjectName("logout")
        self.Techno = QtWidgets.QLabel(self.centralwidget)
        self.Techno.setGeometry(QtCore.QRect(200, 190, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Techno.setFont(font)
        self.Techno.setObjectName("Techno")
        Accueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        self.menuHardis_Materiel = QtWidgets.QMenu(self.menubar)
        self.menuHardis_Materiel.setObjectName("menuHardis_Materiel")
        self.menuEnregistrer_materiel = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrer_materiel.setObjectName("menuEnregistrer_materiel")
        Accueil.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accueil)
        self.statusbar.setObjectName("statusbar")
        Accueil.setStatusBar(self.statusbar)
        self.actionEnregistrer_mat_riel = QtWidgets.QAction(Accueil)
        self.actionEnregistrer_mat_riel.setObjectName("actionEnregistrer_mat_riel")
        self.actionD_placer_mat_riel = QtWidgets.QAction(Accueil)
        self.actionD_placer_mat_riel.setObjectName("actionD_placer_mat_riel")
        self.actionConsulter_mat_riel = QtWidgets.QAction(Accueil)
        self.actionConsulter_mat_riel.setObjectName("actionConsulter_mat_riel")
        self.actionAccueil = QtWidgets.QAction(Accueil)
        self.actionAccueil.setObjectName("actionAccueil")
        self.actionParam_tres = QtWidgets.QAction(Accueil)
        self.actionParam_tres.setObjectName("actionParam_tres")
        self.actionQuitter = QtWidgets.QAction(Accueil)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuHardis_Materiel.addAction(self.actionAccueil)
        self.menuHardis_Materiel.addAction(self.actionParam_tres)
        self.menuHardis_Materiel.addAction(self.actionQuitter)
        self.menuEnregistrer_materiel.addAction(self.actionEnregistrer_mat_riel)
        self.menuEnregistrer_materiel.addAction(self.actionD_placer_mat_riel)
        self.menuEnregistrer_materiel.addAction(self.actionConsulter_mat_riel)
        self.menubar.addAction(self.menuHardis_Materiel.menuAction())
        self.menubar.addAction(self.menuEnregistrer_materiel.menuAction())

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "MainWindow"))
        self.Title.setText(_translate("Accueil", "<html><head/><body><p align=\"center\">HARDIS Matériel</p></body></html>"))
        self.Multichain.setText(_translate("Accueil", "Multichain\n"
"(Blockchain)"))
        self.IOTA.setText(_translate("Accueil", "IOTA\n"
"(Graphe DAG)"))
        self.Techno.setText(_translate("Accueil", "<html><head/><body><p align=\"center\">Quelle technologie voulez-vous utiliser ?</p></body></html>"))
        self.menuHardis_Materiel.setTitle(_translate("Accueil", "Accueil"))
        self.menuEnregistrer_materiel.setTitle(_translate("Accueil", "Opérations"))
        self.actionEnregistrer_mat_riel.setText(_translate("Accueil", "Enregistrer matériel"))
        self.actionD_placer_mat_riel.setText(_translate("Accueil", "Déplacer matériel"))
        self.actionConsulter_mat_riel.setText(_translate("Accueil", "Consulter matériel"))
        self.actionAccueil.setText(_translate("Accueil", "Accueil"))
        self.actionParam_tres.setText(_translate("Accueil", "Paramètres"))
        self.actionQuitter.setText(_translate("Accueil", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

