import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from api.GraphAPI import GraphAPI
from ui.views import queryUI
from api.BlockChainAPI import BlockChainAPI
from utils.Worker import Worker


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

        self.threadpool = QThreadPool()

        self.set_values()
        self.type_menu.currentTextChanged.connect(self.set_values)

        self.position = position
        self.move(self.position[0], self.position[1])
        self.Enregistrer.clicked.connect(self.get_transactions)
        self.pushButton.clicked.connect(self.return_home)

    def set_values(self):
        self.valeur_entree.clear()
        self.gif_value.setMovie(self.movie)
        self.movie.start()
        current_txt = self.type_menu.currentText()
        if current_txt == "Type de matériel":
            worker = Worker(self.api.get_streams)
            worker.signals.result.connect(self.get_results_received)
        elif current_txt == "ID":
            worker = Worker(self.api.get_all_ids)
            worker.signals.result.connect(self.get_results_received)
        elif current_txt == "Marque":
            worker = Worker(self.api.get_all_brands)
            worker.signals.result.connect(self.get_results_received)
        elif current_txt == "Personne responsable":
            worker = Worker(self.api.get_all_owners)
            worker.signals.result.connect(self.get_results_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_results_received(self, results):
        self.movie.stop()
        self.gif_value.clear()
        for result in results:
            self.valeur_entree.addItem("")
            self.valeur_entree.setItemText(results.index(result),
                                           QtCore.QCoreApplication.translate("MainWindow", str(result).capitalize()))

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def get_transactions(self):
        self.gif_results.setMovie(self.movie)
        self.movie.start()
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.currentText())
        if parameter == "Type de matériel":
            value_stream = self.translate_type(value)
            worker = Worker(self.api.get_transactions_by_type, value_stream)
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "ID":
            worker = Worker(self.api.get_transactions_by_id, value.lower())
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "Marque":
            worker = Worker(self.api.get_transactions_by_brand, value)
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "Personne responsable":
            worker = Worker(self.api.get_transactions_by_owner, value.upper())
            worker.signals.result.connect(self.get_transactions_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_transactions_received(self, results):
        self.movie.stop()
        self.gif_results.clear()
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
