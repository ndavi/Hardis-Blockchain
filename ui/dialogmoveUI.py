# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ophelia/Documents/Qt_Projets/Appli/dialog_move.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        Dialog.setFont(font)
        self.Texte = QtWidgets.QLabel(Dialog)
        self.Texte.setGeometry(QtCore.QRect(70, 100, 291, 81))
        self.Texte.setObjectName("Texte")
        self.Titre = QtWidgets.QLabel(Dialog)
        self.Titre.setGeometry(QtCore.QRect(110, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Titre.setFont(font)
        self.Titre.setObjectName("Titre")
        self.BoutonOK = QtWidgets.QPushButton(Dialog)
        self.BoutonOK.setGeometry(QtCore.QRect(160, 240, 89, 25))
        self.BoutonOK.setObjectName("BoutonOK")

        self.retranslateUi(Dialog)
        self.BoutonOK.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Texte.setText(_translate("Dialog", "L\'enregistrement de l\'équipement \n"
"a bien été modifié !\n"
"Merci d\'avoir contribué."))
        self.Titre.setText(_translate("Dialog", "Hardis Matériel"))
        self.BoutonOK.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

