import sys

from PyQt5 import QtCore, QtGui, QtWidgets
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

        self.set_parameter_for_query()
        self.type_menu.currentTextChanged.connect(self.set_parameter_for_query)
        self.restoreGeometry(geometry)
        self.Enregistrer.clicked.connect(self.get_transactions)
        self.pushButton.clicked.connect(self.return_home)
        self.reload.clicked.connect(self.refresh_window)

    def set_parameter_for_query(self):
        self.valeur_entree.clear()
        self.gif_value.setMovie(self.movie)
        self.movie.start()
        current_txt = self.type_menu.currentText()
        self.type_menu.setDisabled(True)
        self.Enregistrer.setDisabled(True)
        if current_txt == "Type de matériel":
            worker = Worker(self.api.get_streams)
        elif current_txt == "ID":
            worker = Worker(self.api.get_all_ids)
        elif current_txt == "Marque":
            worker = Worker(self.api.get_all_brands)
        elif current_txt == "Personne responsable":
            worker = Worker(self.api.get_all_owners)
        worker.signals.result.connect(self.get_parameter_for_query_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_parameter_for_query_received(self, results):
        self.movie.stop()
        self.gif_value.clear()
        for result in results:
            self.valeur_entree.addItem("")
            self.valeur_entree.setItemText(results.index(result),
                                           QtCore.QCoreApplication.translate("MainWindow", str(result)))
        self.type_menu.setEnabled(True)
        self.Enregistrer.setEnabled(True)

    def get_transactions(self):
        self.gif_results.setMovie(self.movie)
        self.movie.start()
        parameter = str(self.type_menu.currentText())
        value = str(self.valeur_entree.currentText())
        self.valeur_entree.setDisabled(True)
        self.type_menu.setDisabled(True)
        self.Enregistrer.setDisabled(True)
        if parameter == "Type de matériel":
            worker = Worker(self.api.get_transactions_by_type, value)
        elif parameter == "ID":
            worker = Worker(self.api.get_transactions_by_id, value)
        elif parameter == "Marque":
            worker = Worker(self.api.get_transactions_by_brand, value)
        elif parameter == "Personne responsable":
            worker = Worker(self.api.get_transactions_by_owner, value)
        worker.signals.result.connect(self.get_transactions_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_transactions_received(self, results):
        self.movie.stop()
        self.gif_results.clear()
        results = self.api.print_results(results)
        self.display_data(results)
        self.valeur_entree.setEnabled(True)
        self.type_menu.setEnabled(True)
        self.Enregistrer.setEnabled(True)

    def display_data(self, transactions):
        self.tableWidget.setRowCount(0)
        if not transactions:
            self.tableWidget.insertRow(0)
            for index in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(0, index, QtWidgets.QTableWidgetItem("/"))
        else:
            for tr in transactions:
                tr_number = transactions.index(tr)
                self.tableWidget.insertRow(tr_number)
                if tr['action'] == 'register':
                    self.tableWidget.setItem(tr_number, 0, QtWidgets.QTableWidgetItem("Enregistrement"))
                    self.tableWidget.setItem(tr_number, 2, QtWidgets.QTableWidgetItem(tr['brand']))
                    self.tableWidget.setItem(tr_number, 3, QtWidgets.QTableWidgetItem(tr['serial']))
                    self.tableWidget.setItem(tr_number, 4, QtWidgets.QTableWidgetItem(tr['purchase_date']))
                elif tr['action'] == 'move':
                    self.tableWidget.setItem(tr_number, 0, QtWidgets.QTableWidgetItem("Déplacement"))
                    self.tableWidget.setItem(tr_number, 4, QtWidgets.QTableWidgetItem(tr['change_date']))
                self.tableWidget.setItem(tr_number, 1, QtWidgets.QTableWidgetItem(tr['id']))
                self.tableWidget.setItem(tr_number, 5, QtWidgets.QTableWidgetItem(tr['business_unit']))
                self.tableWidget.setItem(tr_number, 6, QtWidgets.QTableWidgetItem(tr['team']))
                self.tableWidget.setItem(tr_number, 7, QtWidgets.QTableWidgetItem(tr['owner']))

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def refresh_window(self):
        self.get_transactions()
        self.repaint()