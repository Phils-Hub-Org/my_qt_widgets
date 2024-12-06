# dialogs/ok_dialog.py

from .base import DialogBase

class OKDialog(DialogBase):
    def __init__(self) -> None:
        super().__init__()

        # Ui
        from resources.ui.ui_ok_dialog import Ui_OkDialog
        self.loadUI(Ui_OkDialog)
    
        # Signals
        self.ui.ok_btn.clicked.connect(self.close)
    
    def set_text(self, title):
        self.ui.msg_label.setText(title)

    def set_title(self, text):
        self.ui.title_label.setText(text)

def displayOkDialog(message: str, title: str = 'Ok Dialog') -> None:
    msg_box = OKDialog()
    msg_box.set_text(message)
    msg_box.set_title(title)
    msg_box.exec()