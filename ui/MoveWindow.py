import sys
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5 import QtCore
from graph.GraphAPI import GraphAPI
from ui import moveUI, dialogmoveUI
from blockchain.BlockChainAPI import BlockChainAPI
import datetime

class MoveWindow(QMainWindow, moveUI.Ui_Accueil):
    def __init__(self, api, position, parent=None):
        super(MoveWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = None
        self.api_name = api
        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()
        date_now = datetime.datetime.now()
        self.dateDeplacement.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.move_equipment)
        self.pushButton.clicked.connect(self.return_home)

    def return_home(self):
        from ui.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def move_equipment(self):
        type_french = str(self.type_txt.currentText())
        type_english = self.translate_type(type_french)
        id_equip = str(self.IDequipement.text())
        business_unit = str(self.type_txt_2.currentText())
        team = str(self.type_txt_3.currentText())
        owner = str(self.responsable.text())
        purchase_date = str(self.dateDeplacement.date().day())+"-"+str(self.dateDeplacement.date().month())+"-"+str(self.dateDeplacement.date().year())

        self.api.move_equipment(id_equip, type_english, owner, business_unit, team, purchase_date)
        self.open_home_window()
        self.open_dialog()

    def open_dialog(self):
        self.dialog = MoveDialog()
        self.dialog.show()

    def open_home_window(self):
        from ui.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

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


class MoveDialog(QDialog, dialogmoveUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MoveDialog, self).__init__(parent)
        self.setupUi(self)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MoveWindow()
#     window.show()
#     sys.exit(app.exec_())