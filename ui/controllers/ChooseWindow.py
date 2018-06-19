import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui.views.chooseapiUI import Ui_Accueil
from ui.controllers.HomeWindow import HomeWindow


class ChooseWindow(QMainWindow, Ui_Accueil):
    def __init__(self, geometry=None, parent=None):
        super(ChooseWindow, self).__init__(parent)
        self.setupUi(self)
        self.Multichain.clicked.connect(self.open_home_window_multichain)
        self.IOTA.clicked.connect(self.open_home_window_iota)
        if geometry:
            self.restoreGeometry(geometry)


    def open_home_window_multichain(self):
        self.new_window = HomeWindow("multichain", self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_home_window_iota(self):
        self.new_window = HomeWindow("iota", self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_dialog(self, message):
        from ui.controllers.Dialog import Dialog
        self.dialog = Dialog(message, parent=self)
        self.dialog.show()

    def start(self, app):
        window = ChooseWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChooseWindow()
    window.show()
    sys.exit(app.exec_())
