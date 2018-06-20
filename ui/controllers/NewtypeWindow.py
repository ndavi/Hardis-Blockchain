from PyQt5.QtCore import pyqtSlot, QThreadPool
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from api.GraphAPI import GraphAPI
from ui.views import newtypeUI
from api.BlockChainAPI import BlockChainAPI


from utils.Worker import Worker


class NewtypeWindow(QMainWindow, newtypeUI.Ui_MainWindow):
    def __init__(self, api, geometry, parent=None):
        super(NewtypeWindow, self).__init__(parent)
        self.api = None
        self.api_name = api
        self.setupUi(self)

        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()

        self.threadpool = QThreadPool()

        self.get_types()

        self.restoreGeometry(geometry)

        self.Enregistrer.clicked.connect(self.create_type)
        self.pushButton.clicked.connect(self.open_home_window)
        self.reload.clicked.connect(self.refresh_window)


    def get_types(self):
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.Enregistrer.setDisabled(True)
        worker = Worker(self.api.get_streams)
        worker.signals.result.connect(self.get_types_received)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def get_types_received(self, streams):
        self.movie.stop()
        self.gif_label.clear()
        types = ""
        for stream in streams:
            types = types + str(stream) + "\n"
        self.types_affichage.setText(types)
        self.Enregistrer.setEnabled(True)

    def create_type(self):
        new_type = str(self.nouveau_type.text())
        try:
            assert new_type is not ''
            assert new_type not in self.types_affichage.toPlainText()
        except AssertionError:
            self.open_dialog("Ce type est déjà existant !")
        else:
            self.gif_register.setMovie(self.movie)
            self.movie.start()
            worker = Worker(self.api.add_new_type, new_type)
            worker.signals.finished.connect(self.create_type_confirmed)
            self.threadpool.start(worker)

    @pyqtSlot()
    def create_type_confirmed(self):
        self.movie.stop()
        self.gif_register.clear()
        self.open_register_window()

    def open_dialog(self, message):
        from ui.controllers.Dialog import Dialog
        self.dialog = Dialog(message, parent=self)
        self.dialog.show()

    def open_register_window(self):
        from ui.controllers.RegisterWindow import RegisterWindow
        self.new_window = RegisterWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_home_window(self):
        from ui.controllers.HomeWindow import HomeWindow
        self.new_window = HomeWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def refresh_window(self):
        self.get_types()
        self.repaint()
