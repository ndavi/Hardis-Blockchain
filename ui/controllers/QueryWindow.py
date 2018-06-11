import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from api.GraphAPI import GraphAPI
from ui.views import queryUI
from api.BlockChainAPI import BlockChainAPI
from utils.Worker import Worker


class QueryWindow(QMainWindow, queryUI.Ui_Accueil):
    def __init__(self, api, geometry, parent=None):
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
        self.restoreGeometry(geometry)
        self.Enregistrer.clicked.connect(self.get_transactions)
        self.pushButton.clicked.connect(self.return_home)
        self.reload.clicked.connect(self.refresh_window)

    def set_values(self):
        self.valeur_entree.clear()
        self.gif_value.setMovie(self.movie)
        self.movie.start()
        current_txt = self.type_menu.currentText()
        self.type_menu.setDisabled(True)
        if current_txt == "Type de matériel":
            worker = Worker(self.api.get_streams)
        elif current_txt == "ID":
            worker = Worker(self.api.get_all_ids)
        elif current_txt == "Marque":
            worker = Worker(self.api.get_all_brands)
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
                                           QtCore.QCoreApplication.translate("MainWindow", str(result)))
        self.type_menu.setEnabled(True)

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def get_transactions(self):
        self.gif_results.setMovie(self.movie)
        self.movie.start()
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.currentText())
        if parameter == "Type de matériel":
            worker = Worker(self.api.get_transactions_by_type, value)
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "ID":
            worker = Worker(self.api.get_transactions_by_id, value)
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "Marque":
            worker = Worker(self.api.get_transactions_by_brand, value)
            worker.signals.result.connect(self.get_transactions_received)
        elif parameter == "Personne responsable":
            worker = Worker(self.api.get_transactions_by_owner, value)
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

    def refresh_window(self):
        self.get_transactions()
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueryWindow("multichain", [100,100])
    window.show()
    sys.exit(app.exec_())
