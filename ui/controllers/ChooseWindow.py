import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui.views.chooseapiUI import Ui_Accueil
from ui.controllers.HomeWindow import HomeWindow


class ChooseWindow(QMainWindow, Ui_Accueil):
    def __init__(self, parent=None):
        super(ChooseWindow, self).__init__(parent)
        self.setupUi(self)
        self.position = [250,100]
        a = self.pos()
        x = a.x()
        y = a.y()
        self.move(self.position[0],self.position[1])
        self.Multichain.clicked.connect(self.open_home_window_multichain)
        self.IOTA.clicked.connect(self.open_home_window_iota)


    def open_home_window_multichain(self):
        self.new_window = HomeWindow("multichain", self.position)
        self.new_window.show()
        self.close()

    def open_home_window_iota(self):
        self.new_window = HomeWindow("iota", self.position)
        self.new_window.show()
        self.close()

    def start(self, app):
        window = ChooseWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChooseWindow()
    window.show()
    sys.exit(app.exec_())
