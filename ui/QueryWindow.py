import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from graph.GraphAPI import GraphAPI
from ui import queryUI
from blockchain.BlockChainAPI import BlockChainAPI


class QueryWindow(QMainWindow, queryUI.Ui_Accueil):
    def __init__(self, api, position, parent=None):
        super(QueryWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = None
        self.api_name = api
        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()

        self.set_values()
        self.type_menu.currentTextChanged.connect(self.set_values)

        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.get_transactions)
        self.pushButton.clicked.connect(self.return_home)

    def set_values(self):
        self.valeur_entree.clear()
        current_txt = self.type_menu.currentText()
        if current_txt == "Type de matériel":
            results = self.api.get_streams()
        elif current_txt == "ID":
            results = self.api.get_all_ids()
        elif current_txt == "Marque":
            results = self.api.get_all_brands()
        elif current_txt == "Personne responsable":
            results = self.api.get_all_owners()
        for result in results:
            self.valeur_entree.addItem("")
            self.valeur_entree.setItemText(results.index(result),
                                           QtCore.QCoreApplication.translate("MainWindow", str(result).capitalize()))


    def return_home(self):
        from ui.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def get_transactions(self):
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.currentText())
        if parameter == "Type de matériel":
            value_stream = self.translate_type(value)
            results = self.api.get_transactions_by_type(value_stream)
        elif parameter == "ID":
            results = self.api.get_transactions_by_id(value)
        elif parameter == "Marque":
            results = self.api.get_transactions_by_brand(value)
        elif parameter == "Personne responsable":
            results = self.api.get_transactions_by_owner(value)
        results = self.api.print_results(results)
        if results[0] == "No result found":
            results = ["Aucun résultat"]
        self.affichage.setText('\n'.join(list(results)))

    def translate_type(self, type_french):
        type_french = type_french.lower()
        if type_french == "ordinateur":
            return "computer"
        elif type_french == "table" or type_french == "bureau":
            return "table"
        elif type_french == "chaise":
            return "chair"
        elif type_french == "micro-ondes":
            return "microwave"
        elif type_french == "cafetière":
            return "coffeemaker"
        else:
            return type_french

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueryWindow("multichain", [100,100])
    window.show()
    sys.exit(app.exec_())
