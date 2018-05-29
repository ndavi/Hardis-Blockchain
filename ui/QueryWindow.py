import sys
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
        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.get_transactions)

    def get_transactions(self):
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.text())
        if parameter == "Type de matériel":
            results = self.api.get_transactions_by_type(value)
        elif parameter == "ID":
            results = self.api.get_transactions_by_id(value)
        elif parameter == "Marque":
            results = self.api.get_transactions_by_brand(value)
        elif parameter == "Personne responsable":
            results = self.api.get_transactions_by_owner(value)
        results = self.api.print_results(results)
        self.affichage.setText('\n'.join(list(results)))

    def translate_type(self, type_french):
        type_french = type_french.lower()
        if type_french == "ordinateur":
            return "computer"
        elif type_french == "table":
            return "table"
        elif type_french == "chaise":
            return "chair"
        elif type_french == "micro-ondes":
            return "microwave"
        elif type_french == "cafetière":
            return "coffeemaker"
        else:
            return type_french

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QueryWindow()
#     window.show()
#     sys.exit(app.exec_())
