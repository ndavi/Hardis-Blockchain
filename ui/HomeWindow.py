import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import accueilUI
from blockchain.BlockChainAPI import BlockChainAPI
from ui.mainwindowUI import Ui_MainWindow


class HomeWindow(QMainWindow, accueilUI.Ui_Accueil):
    def __init__(self, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = BlockChainAPI()
        self.Register.clicked.connect(self.open_register_window)

    def open_register_window(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())