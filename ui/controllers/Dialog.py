from PyQt5.QtWidgets import QDialog

from ui.views import dialogUI


class Dialog(QDialog, dialogUI.Ui_Dialog):
    def __init__(self, message, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.Texte.setText(message)
        self.Texte.setWordWrap(True)
