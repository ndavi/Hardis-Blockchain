# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.type_txt = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt.setGeometry(QtCore.QRect(190, 150, 191, 31))
        self.type_txt.setObjectName("type_txt")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
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
        self.Type = QtWidgets.QLabel(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(50, 140, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.BU = QtWidgets.QLabel(self.centralwidget)
        self.BU.setGeometry(QtCore.QRect(470, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BU.setFont(font)
        self.BU.setObjectName("BU")
        self.Equipe = QtWidgets.QLabel(self.centralwidget)
        self.Equipe.setGeometry(QtCore.QRect(470, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Equipe.setFont(font)
        self.Equipe.setObjectName("Equipe")
        self.Marque_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.Marque_txt.setGeometry(QtCore.QRect(190, 270, 191, 31))
        self.Marque_txt.setObjectName("Marque_txt")
        self.Marque = QtWidgets.QLabel(self.centralwidget)
        self.Marque.setGeometry(QtCore.QRect(50, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Marque.setFont(font)
        self.Marque.setObjectName("Marque")
        self.NoSerie_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.NoSerie_txt.setGeometry(QtCore.QRect(190, 330, 191, 31))
        self.NoSerie_txt.setObjectName("NoSerie_txt")
        self.NoSerie = QtWidgets.QLabel(self.centralwidget)
        self.NoSerie.setGeometry(QtCore.QRect(50, 320, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NoSerie.setFont(font)
        self.NoSerie.setObjectName("NoSerie")
        self.DateAchat = QtWidgets.QLabel(self.centralwidget)
        self.DateAchat.setGeometry(QtCore.QRect(470, 320, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateAchat.setFont(font)
        self.DateAchat.setObjectName("DateAchat")
        self.Responsable_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.Responsable_txt.setGeometry(QtCore.QRect(600, 270, 191, 31))
        self.Responsable_txt.setText("")
        self.Responsable_txt.setObjectName("Responsable_txt")
        self.Responsable = QtWidgets.QLabel(self.centralwidget)
        self.Responsable.setGeometry(QtCore.QRect(470, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Responsable.setFont(font)
        self.Responsable.setObjectName("Responsable")
        self.Date = QtWidgets.QDateEdit(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(600, 330, 191, 31))
        self.Date.setAutoFillBackground(False)
        self.Date.setCalendarPopup(False)
        self.Date.setDate(QtCore.QDate(2018, 5, 23))
        self.Date.setObjectName("Date")
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
        self.logo.setPixmap(QtGui.QPixmap("../../Hardis-Blockchain/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 10, 31, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 26))
        self.pushButton.setObjectName("pushButton")
        self.type_txt_2 = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt_2.setGeometry(QtCore.QRect(600, 150, 191, 31))
        self.type_txt_2.setObjectName("type_txt_2")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_3 = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt_3.setGeometry(QtCore.QRect(600, 210, 191, 31))
        self.type_txt_3.setObjectName("type_txt_3")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.Identifiant = QtWidgets.QLabel(self.centralwidget)
        self.Identifiant.setGeometry(QtCore.QRect(50, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Identifiant.setFont(font)
        self.Identifiant.setObjectName("Identifiant")
        self.Identifiant_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.Identifiant_txt.setGeometry(QtCore.QRect(190, 210, 191, 31))
        self.Identifiant_txt.setObjectName("Identifiant_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        self.menuHardis_Mat_riel = QtWidgets.QMenu(self.menubar)
        self.menuHardis_Mat_riel.setObjectName("menuHardis_Mat_riel")
        self.menuOp_rations = QtWidgets.QMenu(self.menubar)
        self.menuOp_rations.setObjectName("menuOp_rations")
        MainWindow.setMenuBar(self.menubar)
        self.actionD_placement_mat_riel = QtWidgets.QAction(MainWindow)
        self.actionD_placement_mat_riel.setObjectName("actionD_placement_mat_riel")
        self.actionEnregistrer_mat_riel = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_mat_riel.setObjectName("actionEnregistrer_mat_riel")
        self.actionConsulter_mat_riel = QtWidgets.QAction(MainWindow)
        self.actionConsulter_mat_riel.setObjectName("actionConsulter_mat_riel")
        self.actionAccueil = QtWidgets.QAction(MainWindow)
        self.actionAccueil.setObjectName("actionAccueil")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionParam_tres = QtWidgets.QAction(MainWindow)
        self.actionParam_tres.setObjectName("actionParam_tres")
        self.menuHardis_Mat_riel.addAction(self.actionAccueil)
        self.menuHardis_Mat_riel.addAction(self.actionParam_tres)
        self.menuHardis_Mat_riel.addAction(self.actionQuitter)
        self.menuOp_rations.addAction(self.actionEnregistrer_mat_riel)
        self.menuOp_rations.addAction(self.actionD_placement_mat_riel)
        self.menuOp_rations.addAction(self.actionConsulter_mat_riel)
        self.menubar.addAction(self.menuHardis_Mat_riel.menuAction())
        self.menubar.addAction(self.menuOp_rations.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HARDIS Matériel"))
        self.type_txt.setItemText(0, _translate("MainWindow", "Ordinateur et accessoires"))
        self.type_txt.setItemText(1, _translate("MainWindow", "Bureau"))
        self.type_txt.setItemText(2, _translate("MainWindow", "Chaise"))
        self.type_txt.setItemText(3, _translate("MainWindow", "Micro-ondes"))
        self.type_txt.setItemText(4, _translate("MainWindow", "Cafetière"))
        self.Titre.setText(_translate("MainWindow", "Enregistrer un nouvel équipement"))
        self.Type.setText(_translate("MainWindow", "Type de matériel"))
        self.BU.setText(_translate("MainWindow", "BU"))
        self.Equipe.setText(_translate("MainWindow", "Equipe"))
        self.Marque.setText(_translate("MainWindow", "Marque"))
        self.NoSerie.setText(_translate("MainWindow", "Numéro de série"))
        self.DateAchat.setText(_translate("MainWindow", "Date d\'achat"))
        self.Responsable.setText(_translate("MainWindow", "Personne\n"
"responsable"))
        self.Enregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.type_txt_2.setItemText(0, _translate("MainWindow", "Business Applications"))
        self.type_txt_2.setItemText(1, _translate("MainWindow", "Business Consulting"))
        self.type_txt_2.setItemText(2, _translate("MainWindow", "Cloud Operations"))
        self.type_txt_2.setItemText(3, _translate("MainWindow", "Cloud Platform"))
        self.type_txt_2.setItemText(4, _translate("MainWindow", "Reflex"))
        self.type_txt_2.setItemText(5, _translate("MainWindow", "Indifférent"))
        self.type_txt_3.setItemText(0, _translate("MainWindow", "Pole Digital"))
        self.type_txt_3.setItemText(1, _translate("MainWindow", "Pole TSI"))
        self.type_txt_3.setItemText(2, _translate("MainWindow", "Salesforce"))
        self.type_txt_3.setItemText(3, _translate("MainWindow", "Autre"))
        self.type_txt_3.setItemText(4, _translate("MainWindow", "Indifférent"))
        self.Identifiant.setText(_translate("MainWindow", "Identifiant"))
        self.menuHardis_Mat_riel.setTitle(_translate("MainWindow", "Accueil"))
        self.menuOp_rations.setTitle(_translate("MainWindow", "Opérations"))
        self.actionD_placement_mat_riel.setText(_translate("MainWindow", "Déplacement matériel"))
        self.actionEnregistrer_mat_riel.setText(_translate("MainWindow", "Enregistrer matériel"))
        self.actionConsulter_mat_riel.setText(_translate("MainWindow", "Consulter matériel"))
        self.actionAccueil.setText(_translate("MainWindow", "Accueil"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionParam_tres.setText(_translate("MainWindow", "Paramètres "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

