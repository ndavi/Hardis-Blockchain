# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/query.ui'
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
        self.Title.setGeometry(QtCore.QRect(180, 30, 561, 71))
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
        self.Enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.Enregistrer.setGeometry(QtCore.QRect(350, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.Enregistrer.setFont(font)
        self.Enregistrer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Enregistrer.setMouseTracking(False)
        self.Enregistrer.setFlat(False)
        self.Enregistrer.setObjectName("Enregistrer")
        self.type_menu = QtWidgets.QComboBox(self.centralwidget)
        self.type_menu.setGeometry(QtCore.QRect(210, 140, 191, 31))
        self.type_menu.setObjectName("type_menu")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.chercher = QtWidgets.QLabel(self.centralwidget)
        self.chercher.setGeometry(QtCore.QRect(60, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chercher.setFont(font)
        self.chercher.setObjectName("chercher")
        self.valeur_entree = QtWidgets.QComboBox(self.centralwidget)
        self.valeur_entree.setGeometry(QtCore.QRect(570, 140, 181, 31))
        self.valeur_entree.setObjectName("valeur_entree")
        self.valeur = QtWidgets.QLabel(self.centralwidget)
        self.valeur.setGeometry(QtCore.QRect(480, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valeur.setFont(font)
        self.valeur.setObjectName("valeur")
        # self.affichage = QtWidgets.QTextBrowser(self.centralwidget)
        # self.affichage.setGeometry(QtCore.QRect(95, 250, 655, 260))
        # self.affichage.setObjectName("affichage")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 250, 821, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        self.columns = ["Entrée", "ID", "Marque", "N° série", "Date", "BU", "Equipe", "Responsable"]
        for column in self.columns:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(self.columns.index(column), item)
            item.setText(column)

        gif = os.path.relpath("images/loader.gif")
        self.movie = QtGui.QMovie(gif)
        self.movie.setScaledSize(QtCore.QSize(31, 31))
        self.gif_value = QtWidgets.QLabel(self.centralwidget)
        self.gif_value.setGeometry(QtCore.QRect(760, 140, 31, 31))
        self.gif_results = QtWidgets.QLabel(self.centralwidget)
        self.gif_results.setGeometry(QtCore.QRect(490, 190, 31, 31))

        Accueil.setCentralWidget(self.centralwidget)

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Consultation - Hardis Matériel"))
        self.Title.setText(_translate("Accueil", "<html><head/><body><p align=\"center\">Consulter le matériel enregistré</p></body></html>"))
        self.Enregistrer.setText(_translate("Accueil", "Valider"))
        self.type_menu.setItemText(0, _translate("Accueil", "Type de matériel"))
        self.type_menu.setItemText(1, _translate("Accueil", "ID"))
        self.type_menu.setItemText(2, _translate("Accueil", "Marque"))
        self.type_menu.setItemText(3, _translate("Accueil", "Personne responsable"))
        self.chercher.setText(_translate("Accueil", "Chercher par ..."))
        self.valeur.setText(_translate("Accueil", "Valeur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

