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
        # self.api = GraphAPI()
        self.Register.clicked.connect(self.open_register_window)
        self.Move.clicked.connect(self.open_move_window)
        self.Query.clicked.connect(self.open_query_window)

    def open_register_window(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.close()

    def open_move_window(self):
        pass

    def open_query_window(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())