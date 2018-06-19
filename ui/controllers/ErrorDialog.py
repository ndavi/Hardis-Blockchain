from PyQt5.QtWidgets import QDialog

from ui.views import dialogUI


class ErrorDialog(QDialog, dialogUI.Ui_Dialog):
    def __init__(self, message, parent=None):
        super(ErrorDialog, self).__init__(parent)
        self.setupUi(self)