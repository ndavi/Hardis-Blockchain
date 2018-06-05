import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5 import QtCore
from graph.GraphAPI import GraphAPI
from ui.views import moveUI, dialogmoveUI
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
            self.streams = self.api.get_streams()
            for stream in self.streams:
                self.type_txt.addItem("")
                self.type_txt.setItemText(self.streams.index(stream),
                                          QtCore.QCoreApplication.translate("MainWindow", str(stream).capitalize()))
        elif self.api_name == "iota":
            self.api = GraphAPI()

        date_now = datetime.datetime.now()

        self.set_id_values()
        self.type_txt.currentTextChanged.connect(self.set_id_values)

        self.dateDeplacement.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.move_equipment)
        self.pushButton.clicked.connect(self.return_home)

    def set_id_values(self):
        self.IDequipement.clear()
        results_id = self.api.get_id_by_type(self.type_txt.currentText())
        for result in results_id:
            self.IDequipement.addItem("")
            self.IDequipement.setItemText(results_id.index(result),
                                      QtCore.QCoreApplication.translate("MainWindow", str(result)))

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def move_equipment(self):
        type_french = str(self.type_txt.currentText())
        type_english = self.translate_type(type_french)
        id_equip = str(self.IDequipement.currentText())
        business_unit = str(self.type_txt_2.currentText())
        team = str(self.type_txt_3.currentText())
        owner = str(self.responsable.text())
        purchase_date = str(self.dateDeplacement.date().day())+"-"+str(self.dateDeplacement.date().month())+"-"+str(self.dateDeplacement.date().year())

        self.api.move_equipment(id_equip, type_english, owner, business_unit, team, purchase_date)
        self.open_home_window()
        self.open_dialog()

    def open_dialog(self):
        self.dialog = MoveDialog(self.position)
        self.dialog.show()

    def open_home_window(self):
        from ui.controllers.HomeWindow import HomeWindow
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
        else:
            return type_french


class MoveDialog(QDialog, dialogmoveUI.Ui_Dialog):
    def __init__(self, position, parent=None):
        super(MoveDialog, self).__init__(parent)
        self.setupUi(self)
        self.move(position[0]+200, position[1]+200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoveWindow("multichain", [100,100])
    window.show()
    sys.exit(app.exec_())