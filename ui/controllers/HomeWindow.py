from PyQt5.QtWidgets import QMainWindow

from api.GraphAPI import GraphAPI
from ui.views import accueilUI
from api.BlockChainAPI import BlockChainAPI
from ui.controllers.MoveWindow import MoveWindow
from ui.controllers.QueryWindow import QueryWindow
from ui.controllers.RegisterWindow import RegisterWindow


class HomeWindow(QMainWindow, accueilUI.Ui_Accueil):
    def __init__(self, api, position, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = None
        self.api_name = api
        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()
        self.position = position
        self.move(self.position[0], self.position[1])
        self.Empty.setEnabled(False)
        self.Register.clicked.connect(self.open_register_window)
        self.Move.clicked.connect(self.open_move_window)
        self.Query.clicked.connect(self.open_query_window)

    def open_register_window(self):
        self.new_window = RegisterWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def open_move_window(self):
        self.new_window = MoveWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

    def open_query_window(self):
        self.new_window = QueryWindow(self.api_name, self.position)
        self.new_window.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = HomeWindow()
#     window.show()
#     sys.exit(app.exec_())
