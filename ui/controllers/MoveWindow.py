import sys

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5 import QtCore
from api.GraphAPI import GraphAPI
from ui.services.RulesService import RulesService
from ui.views import moveUI, dialogmoveUI
from api.BlockChainAPI import BlockChainAPI
import datetime

from utils.Worker import Worker, QThreadPool


class MoveWindow(QMainWindow, moveUI.Ui_Accueil):

    def __init__(self, api, geometry, parent=None):
        super(MoveWindow, self).__init__(parent)
        self.setupUi(self)
        self.api_name = api
        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()

        date_now = datetime.datetime.now()
        self.threadpool = QThreadPool()


        self.get_types()
        self.type_txt.currentTextChanged.connect(self.set_id_values)

        self.dateDeplacement.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
        self.restoreGeometry(geometry)
        self.Enregistrer.clicked.connect(self.move_equipment)
        self.pushButton.clicked.connect(self.return_home)
        self.reload.clicked.connect(self.refresh_window)


    def get_types(self):
        self.gif_type.setMovie(self.movie)
        self.movie.start()
        worker = Worker(self.api.get_streams)
        worker.signals.result.connect(self.get_types_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_types_received(self, streams):
        self.movie.stop()
        self.gif_type.clear()
        self.type_txt.clear()
        for stream in streams:
            self.type_txt.addItem("")
            self.type_txt.setItemText(streams.index(stream),
                                      QtCore.QCoreApplication.translate("MainWindow", str(stream)))
        self.set_id_values()

    def set_id_values(self):
        self.IDequipement.clear()
        self.gif_id.setMovie(self.movie)
        self.movie.start()
        worker = Worker(self.api.get_id_by_type, self.type_txt.currentText())
        worker.signals.result.connect(self.set_id_values_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def set_id_values_received(self, results):
        if(results == []):
            return
        self.movie.stop()
        self.gif_id.clear()
        self.IDequipement.clear()
        for result in results_id:
        results = RulesService.filterMyObjects(results)
        for result in results:
            id, owner = result
            self.IDequipement.addItem("")
            self.IDequipement.setItemText(results.index(result),
                                      QtCore.QCoreApplication.translate("MainWindow", str(id)))

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def move_equipment(self):
        type_equip = str(self.type_txt.currentText())
        id_equip = str(self.IDequipement.currentText())
        business_unit = str(self.type_txt_2.currentText())
        team = str(self.type_txt_3.currentText())
        owner = str(self.responsable.text())
        purchase_date = str(self.dateDeplacement.date().day())+"-"+str(self.dateDeplacement.date().month())+"-"+str(self.dateDeplacement.date().year())

        self.api.move_equipment(id_equip, type_equip, owner, business_unit, team, purchase_date)
        self.open_home_window()
        self.open_dialog()

    def refresh_window(self):
        self.get_types()
        self.repaint()

    def open_dialog(self):
        self.dialog = MoveDialog(self.saveGeometry())
        self.dialog.show()

    def open_home_window(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()


class MoveDialog(QDialog, dialogmoveUI.Ui_Dialog):
    def __init__(self, geometry, parent=None):
        super(MoveDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoveWindow("multichain", [100,100])
    window.show()
    sys.exit(app.exec_())

