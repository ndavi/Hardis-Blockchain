# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/moveequip.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accueil(object):
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.setFixedSize(845, 568)
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 30, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 131, 71))
        self.logo.setMaximumSize(QtCore.QSize(282, 160))
        self.logo.setSizeIncrement(QtCore.QSize(1, 2))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 10, 31, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 26))
        self.pushButton.setObjectName("pushButton")
        self.reload = QtWidgets.QPushButton(self.centralwidget)
        self.reload.setGeometry(QtCore.QRect(760, 10, 31, 31))
        self.reload.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon1)
        self.reload.setIconSize(QtCore.QSize(21, 21))
        self.reload.setObjectName("reload")
        self.IDequipement_label = QtWidgets.QLabel(self.centralwidget)
        self.IDequipement_label.setGeometry(QtCore.QRect(60, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IDequipement_label.setFont(font)
        self.IDequipement_label.setObjectName("IDequipement_label")
        self.dateDeplcement_label = QtWidgets.QLabel(self.centralwidget)
        self.dateDeplcement_label.setGeometry(QtCore.QRect(60, 310, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateDeplcement_label.setFont(font)
        self.dateDeplcement_label.setObjectName("dateDeplcement_label")
        self.Enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.Enregistrer.setGeometry(QtCore.QRect(260, 450, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.Enregistrer.setFont(font)
        self.Enregistrer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Enregistrer.setMouseTracking(False)
        self.Enregistrer.setFlat(False)
        self.Enregistrer.setObjectName("Enregistrer")
        self.IDequipement = QtWidgets.QComboBox(self.centralwidget)
        self.IDequipement.setGeometry(QtCore.QRect(220, 260, 191, 31))
        self.IDequipement.setObjectName("IDequipement")
        self.deplacer_vers = QtWidgets.QLabel(self.centralwidget)
        self.deplacer_vers.setGeometry(QtCore.QRect(580, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deplacer_vers.setFont(font)
        self.deplacer_vers.setObjectName("deplacer_vers")
        self.responsable = QtWidgets.QLineEdit(self.centralwidget)
        self.responsable.setGeometry(QtCore.QRect(620, 320, 191, 31))
        self.responsable.setText("")
        self.responsable.setObjectName("responsable")
        self.dateDeplacement = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDeplacement.setGeometry(QtCore.QRect(220, 320, 191, 31))
        self.dateDeplacement.setObjectName("dateDeplacement")
        self.BU_label = QtWidgets.QLabel(self.centralwidget)
        self.BU_label.setGeometry(QtCore.QRect(490, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BU_label.setFont(font)
        self.BU_label.setObjectName("BU_label")
        self.responsable_label = QtWidgets.QLabel(self.centralwidget)
        self.responsable_label.setGeometry(QtCore.QRect(490, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.responsable_label.setFont(font)
        self.responsable_label.setObjectName("responsable_label")
        self.Type = QtWidgets.QLabel(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(60, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.equipe_label = QtWidgets.QLabel(self.centralwidget)
        self.equipe_label.setGeometry(QtCore.QRect(490, 250, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.equipe_label.setFont(font)
        self.equipe_label.setObjectName("equipe_label")
        self.type_txt = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt.setGeometry(QtCore.QRect(220, 200, 191, 31))
        self.type_txt.setObjectName("type_txt")
        self.type_txt_3 = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt_3.setGeometry(QtCore.QRect(620, 260, 191, 31))
        self.type_txt_3.setObjectName("type_txt_3")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_3.addItem("")
        self.type_txt_2 = QtWidgets.QComboBox(self.centralwidget)
        self.type_txt_2.setGeometry(QtCore.QRect(620, 200, 191, 31))
        self.type_txt_2.setObjectName("type_txt_2")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")
        self.type_txt_2.addItem("")

        gif = os.path.relpath("images/loader.gif")
        self.movie = QtGui.QMovie(gif)
        self.movie.setScaledSize(QtCore.QSize(31, 31))
        self.gif_type = QtWidgets.QLabel(self.centralwidget)
        self.gif_type.setGeometry(QtCore.QRect(420, 200, 31, 31))
        self.gif_id = QtWidgets.QLabel(self.centralwidget)
        self.gif_id.setGeometry(QtCore.QRect(420, 260, 31, 31))
        self.gif_register = QtWidgets.QLabel(self.centralwidget)
        self.gif_register.setGeometry(QtCore.QRect(590, 455, 31, 31))
        Accueil.setCentralWidget(self.centralwidget)

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "MainWindow"))
        self.Title.setText(_translate("Accueil", "<html><head/><body><p align=\"center\">Déplacer ou modifier un équipement</p></body></html>"))
        self.IDequipement_label.setText(_translate("Accueil", "ID équipement"))
        self.dateDeplcement_label.setText(_translate("Accueil", "Date de modification"))
        self.Enregistrer.setText(_translate("Accueil", "Enregistrer"))
        self.deplacer_vers.setText(_translate("Accueil", "Déplacer vers ..."))
        self.BU_label.setText(_translate("Accueil", "BU"))
        self.responsable_label.setText(_translate("Accueil", "Personne\n"
"responsable"))
        self.Type.setText(_translate("Accueil", "Type de matériel"))
        self.equipe_label.setText(_translate("Accueil", "Equipe"))
        self.type_txt_3.setItemText(0, _translate("Accueil", "Pole Digital"))
        self.type_txt_3.setItemText(1, _translate("Accueil", "Pole TSI"))
        self.type_txt_3.setItemText(2, _translate("Accueil", "Salesforce"))
        self.type_txt_3.setItemText(3, _translate("Accueil", "Indifférent"))
        self.type_txt_3.setItemText(4, _translate("Accueil", "Autre"))
        self.type_txt_2.setItemText(0, _translate("Accueil", "Business Applications"))
        self.type_txt_2.setItemText(1, _translate("Accueil", "Business Consulting"))
        self.type_txt_2.setItemText(2, _translate("Accueil", "Cloud Platform"))
        self.type_txt_2.setItemText(3, _translate("Accueil", "Cloud Operations"))
        self.type_txt_2.setItemText(4, _translate("Accueil", "Reflex"))
        self.type_txt_2.setItemText(5, _translate("Accueil", "Indifférent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())
