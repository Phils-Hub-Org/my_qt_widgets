# dialogs/input_dialog.py

from typing import Union

from enum import Enum, auto

from .base import DialogBase

class InputDialogResult:
    def __init__(self, _input: str) -> None:
        self.input = _input

class InputDialogResultEnum(Enum):
    EMPTY = auto()
    CANCEL = auto()

class InputDialog(DialogBase):
    """
    A simple message box with an input field and two buttons: submit and cancel.

    The submit button closes the dialog and returns the InputDialogResult or InputDialogResultEnum.EMPTY
    The cancel button closes the dialog and returns InputDialogResultEnum.CANCEL
    """
    def __init__(self) -> None:
        super().__init__()

        # Ui
        from resources.ui.ui_input_dialog import Ui_InputDialog
        self.loadUI(Ui_InputDialog)

        # Signals
        self.ui.submit_btn.clicked.connect(self.on_submit)
        self.ui.cancel_btn.clicked.connect(self.on_cancel)
    
        # Attribute
        self.result = None
    
    def set_text(self, title):
        self.ui.msg_label.setText(title)

    def set_title(self, text):
        self.ui.title_label.setText(text)

    def on_submit(self) -> None:
        text_input = self.ui.input_field.text().strip()
        if text_input:
            self.result = InputDialogResult(text_input)
        else:
            self.result = InputDialogResultEnum.EMPTY
        self.close()
    
    def on_cancel(self) -> None:
        self.result = InputDialogResultEnum.CANCEL
        self.close()

    def get_result(self) -> Union[InputDialogResult, InputDialogResultEnum]:
        return self.result

def displayInputDialog(message: str, title: str = 'Input Dialog') -> Union[InputDialogResult, InputDialogResultEnum]:
    msg_box = InputDialog()
    msg_box.set_text(message)
    msg_box.set_title(title)
    msg_box.exec()

    # Retrieve and return the result from the dialog
    return msg_box.get_result()
