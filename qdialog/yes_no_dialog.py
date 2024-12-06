# dialogs/yes_no_dialog.py

from PySide6.QtWidgets import QDialog

from .base import DialogBase

class YesNoDialog(DialogBase):
    def __init__(self):
        super().__init__()

        # Ui
        from resources.ui.ui_yes_no_dialog import Ui_YesNoDialog
        self.loadUI(Ui_YesNoDialog)

        # Signals
        self.ui.yes_btn.clicked.connect(self.accept)
        self.ui.no_btn.clicked.connect(self.reject)
    
    def set_text(self, title):
        self.ui.msg_label.setText(title)

    def set_title(self, text):
        self.ui.title_label.setText(text)

def displayYesNoDialog(message: str, title: str = 'Yes/No Dialog') -> bool:
    msg_box = YesNoDialog()
    msg_box.set_text(message)
    msg_box.set_title(title)
    result = msg_box.exec()  # returns QDialog.Accepted or QDialog.Rejected
    return result == QDialog.Accepted  # returns bool
