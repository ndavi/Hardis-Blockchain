import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import queryUI
from blockchain.BlockChainAPI import BlockChainAPI


class QueryWindow(QMainWindow, queryUI.Ui_Accueil):
    def __init__(self, parent=None):
        super(QueryWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = BlockChainAPI()

        self.Enregistrer.clicked.connect(self.get_transactions)

    def get_transactions(self):
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.text())
        if parameter == "Type de matériel":
            results = self.api.getByType(value)
            # results = self.api.get_transactions_by_type(value)
        elif parameter == "ID":
            results = self.api.getByID(value)
            # results = self.api.get_transactions_by_id(value)
        elif parameter == "Marque":
            results = self.api.getByBrand(value)
            # results = self.api.get_transactions_by_brand(value)
        elif parameter == "Personne responsable":
            results = self.api.getByOwner(value)
            # results = self.api.get_transactions_by_owner(value)
        self.affichage.setText(results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueryWindow()
    window.show()
    sys.exit(app.exec_())
