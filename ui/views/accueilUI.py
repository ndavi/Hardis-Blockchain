# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/accueil.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accueil(object):
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.setFixedSize(845, 568)
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
        self.logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.retour = QtWidgets.QToolButton(self.centralwidget)
        self.retour.setGeometry(QtCore.QRect(640, 10, 191, 41))
        self.retour.setObjectName("toolButton")
        self.technologie = QtWidgets.QLabel(self.centralwidget)
        self.technologie.setGeometry(QtCore.QRect(365, 130, 111, 21))
        self.technologie.setAlignment(QtCore.Qt.AlignCenter)
        self.technologie.setObjectName("technologie")
        Accueil.setCentralWidget(self.centralwidget)


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
        self.Empty.setText(_translate("Accueil", "Paramètres"))
        self.Query.setText(_translate("Accueil", "Consulter le\n"
" matériel enregistré"))
        self.retour.setText(_translate("Accueil", "Retour aux technologies"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

