import getpass
import sys

from PyQt5.QtCore import pyqtSlot, QThreadPool
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore

from api.GraphAPI import GraphAPI
from ui.controllers.NewtypeWindow import NewtypeWindow
from ui.views import registerUI, dialogUI
from api.BlockChainAPI import BlockChainAPI
import datetime

from utils.Worker import Worker


class RegisterWindow(QMainWindow, registerUI.Ui_MainWindow):
    def __init__(self, api, geometry, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.api = None
        self.api_name = api
        self.setupUi(self)

        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()

        self.threadpool = QThreadPool()
        self.restoreGeometry(geometry)
        self.get_types()
        date_now = datetime.datetime.now()
        self.Responsable_txt.setText(getpass.getuser())
        self.Responsable_txt.setDisabled(True)
        self.Date.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
        self.Enregistrer.clicked.connect(self.register_equipment)
        self.pushButton.clicked.connect(self.return_home)
        self.ajout_type.clicked.connect(self.add_new_type)
        self.reload.clicked.connect(self.reload_window)

    def get_types(self):
        self.gif_types.setMovie(self.movie)
        self.movie.start()
        worker = Worker(self.api.get_streams)
        worker.signals.result.connect(self.get_types_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_types_received(self, streams):
        self.movie.stop()
        self.gif_types.clear()
        self.type_txt.clear()
        for stream in streams:
            self.type_txt.addItem("")
            self.type_txt.setItemText(streams.index(stream),
                                      QtCore.QCoreApplication.translate("MainWindow", str(stream)))

    def return_home(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def add_new_type(self):
        self.new_window = NewtypeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def register_equipment(self):
        type_equip = str(self.type_txt.currentText())
        identifier = str(self.Identifiant_txt.text())
        brand = str(self.Marque_txt.text())
        serial_number = str(self.NoSerie_txt.text())
        business_unit = str(self.type_txt_2.currentText())
        team = str(self.type_txt_3.currentText())
        owner = str(self.Responsable.text())
        purchase_date = str(self.Date.date().day())+"-"+str(self.Date.date().month())+"-"+str(self.Date.date().year())

        self.gif_register.setMovie(self.movie)
        self.movie.start()

        worker = Worker(self.api.register_equipment, type_equip, identifier, brand, serial_number, purchase_date, business_unit, team, owner)
        worker.signals.finished.connect(self.register_equipment_confirmed)
        self.threadpool.start(worker)

    @pyqtSlot()
    def register_equipment_confirmed(self):
        self.movie.stop()
        self.gif_register.clear()
        self.open_home_window()
        self.open_dialog()

    def reload_window(self):
        self.get_types()
        self.repaint()

    def open_dialog(self):
        self.dialog = RegisterDialog(parent=self)
        self.dialog.show()

    def open_home_window(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()


class RegisterDialog(QDialog, dialogUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow("multichain", [100, 100])
    window.show()
    sys.exit(app.exec_())
