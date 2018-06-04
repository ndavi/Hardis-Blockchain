import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore

from graph.GraphAPI import GraphAPI
from ui import registerUI, dialogUI
from blockchain.BlockChainAPI import BlockChainAPI
import datetime


class RegisterWindow(QMainWindow, registerUI.Ui_MainWindow):
    def __init__(self, api, position, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.api = None
        self.api_name = api
        self.setupUi(self)

        if self.api_name == "multichain":
            self.api = BlockChainAPI()
            self.streams = self.api.get_streams()
            for stream in self.streams:
                self.type_txt.addItem("")
                self.type_txt.setItemText(self.streams.index(stream), QtCore.QCoreApplication.translate("MainWindow", str(stream).capitalize()))
        elif self.api_name == "iota":
            self.api = GraphAPI()

        date_now = datetime.datetime.now()
        self.Date.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.register_equipment)
        self.pushButton.clicked.connect(self.return_home)

    def return_home(self):
        from ui.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def register_equipment(self):
        type_french = str(self.type_txt.currentText())
        type_english = self.translate_type(type_french)
        identifier = str(self.Identifiant_txt.text())
        brand = str(self.Marque_txt.text())
        serial_number = str(self.NoSerie_txt.text())
        business_unit = str(self.type_txt_2.currentText())
        team = str(self.type_txt_3.currentText())
        owner = str(self.Responsable_txt.text())
        purchase_date = str(self.Date.date().day())+"-"+str(self.Date.date().month())+"-"+str(self.Date.date().year())

        self.api.register_equipment(type_english, identifier, brand, serial_number, purchase_date, business_unit, team, owner)
        self.open_home_window()
        self.open_dialog()

    def translate_type(self, type_french):
        type_french = type_french.lower()
        if type_french == "ordinateur et accessoires":
            return "computer"
        elif type_french == "bureau":
            return "table"
        elif type_french == "chaise":
            return "chair"
        elif type_french == "micro-ondes":
            return "microwave"
        elif type_french == "cafetière":
            return "coffeemaker"
        else:
            return type_french

    def open_dialog(self):
        self.dialog = RegisterDialog(self.position)
        self.dialog.show()

    def open_home_window(self):
        from ui.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()


class RegisterDialog(QDialog, dialogUI.Ui_Dialog):
    def __init__(self, position, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)
        self.move(position[0]+200,position[1]+200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow("multichain",[100,100])
    window.show()
    sys.exit(app.exec_())
