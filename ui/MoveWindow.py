import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import mainwindowUI, moveUI
from blockchain.BlockChainAPI import BlockChainAPI


class MoveWindow(QMainWindow, moveUI.Ui_Accueil):
    def __init__(self, parent=None):
        super(MoveWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = BlockChainAPI()

        self.Enregistrer.clicked.connect(self.move_equipment)

    def move_equipment(self):
        type_french = str(self.type_txt.currentText())
        type_english = self.translate_type(type_french)
        id_equip = str(self.id.currentText())
        brand = str(self.Marque_txt.text())
        serial_number = str(self.NoSerie_txt.text())
        business_unit = str(self.BU_txt.text())
        team = str(self.Equipe_txt.text())
        owner = str(self.Responsable_txt.text())
        purchase_date = str(self.Date.date().day())+"-"+str(self.Date.date().month())+"-"+str(self.Date.date().year())
        self.api.moveEquipment(id_equip, type_english, brand, serial_number, purchase_date, business_unit, team, owner)

    def translate_type(self, type_french):
        if type_french == "Ordinateur et accessoires":
            return "computer"
        elif type_french == "Table":
            return "table"
        elif type_french == "Chaise":
            return "chair"
        elif type_french == "Micro-ondes":
            return "microwave"
        elif type_french == "Cafetière":
            return "coffeemaker"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoveWindow()
    window.show()
    sys.exit(app.exec_())