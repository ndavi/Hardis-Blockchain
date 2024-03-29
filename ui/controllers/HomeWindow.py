from PyQt5.QtWidgets import QMainWindow

from api.GraphAPI import GraphAPI
from ui.views import accueilUI
from api.BlockChainAPI import BlockChainAPI
from ui.controllers.MoveWindow import MoveWindow
from ui.controllers.QueryWindow import QueryWindow
from ui.controllers.RegisterWindow import RegisterWindow


class HomeWindow(QMainWindow, accueilUI.Ui_Accueil):
    def __init__(self, api, geometry, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        self.api = None
        self.api_name = api
        if self.api_name == "multichain":
            self.api = BlockChainAPI()
        elif self.api_name == "iota":
            self.api = GraphAPI()
        self.technologie.setText(self.api_name.capitalize())
        self.restoreGeometry(geometry)
        self.Empty.setEnabled(False)
        self.Register.clicked.connect(self.open_register_window)
        self.Move.clicked.connect(self.open_move_window)
        self.Query.clicked.connect(self.open_query_window)
        self.retour.clicked.connect(self.open_choose_window)

    def open_register_window(self):
        self.new_window = RegisterWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_move_window(self):
        self.new_window = MoveWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_query_window(self):
        self.new_window = QueryWindow(self.api_name, self.saveGeometry())
        self.new_window.show()
        self.close()

    def open_choose_window(self):
        from ui.controllers.ChooseWindow import ChooseWindow
        self.new_window = ChooseWindow(self.saveGeometry())
        self.new_window.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = HomeWindow()
#     window.show()
#     sys.exit(app.exec_())
