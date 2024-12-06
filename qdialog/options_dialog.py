# dialogs/options_dialog.py

from PySide6.QtWidgets import QButtonGroup

from .base import DialogBase

class OptionsDialog(DialogBase):
    def __init__(self, options_count: int):
        super().__init__()

        # Ui
        from resources.ui.ui_options_dialog import Ui_OptionsDialog
        self.loadUI(Ui_OptionsDialog)

        # Signals
        self.ui.submit_btn.clicked.connect(self.on_submit)

        # Attribute
        self.options_count = options_count
        self.result = None

        # Initialize the button group
        self.button_group = QButtonGroup(self)
        if self.options_count == 2:
            self.button_group.addButton(self.ui.option1, 1)
            self.button_group.addButton(self.ui.option2, 2)
            # hide option from layout
            self.ui.option3.hide()
        elif self.options_count == 3:
            self.button_group.addButton(self.ui.option1, 1)
            self.button_group.addButton(self.ui.option2, 2)
            self.button_group.addButton(self.ui.option3, 3)

    def set_text(self, title):
        self.ui.msg_label.setText(title)

    def set_title(self, text):
        self.ui.title_label.setText(text)
    
    def set_options(self, options: list):
        if self.options_count == 2:
            self.ui.option1.setText(options[0])
            self.ui.option2.setText(options[1])
        elif self.options_count == 3:
            self.ui.option1.setText(options[0])
            self.ui.option2.setText(options[1])
            self.ui.option3.setText(options[2])

    def on_submit(self):
        # Retrieve the selected option from the button group
        selected_option = self.button_group.checkedId()

        # Store the selected option in the result attribute
        self.result = selected_option

        # Close the dialog
        self.close()

    def get_result(self):
        return self.result

def displayOptionsDialog(message: str, options: list, title: str = 'Options Dialog') -> str | None:
    """
    Display a message box with an options list and return the selected option index.
    Options count must be 2 or 3. This can simply be set via the amount of options specified in the passed list.
    """
    msg_box = OptionsDialog(options_count=len(options))
    msg_box.set_text(message)
    msg_box.set_options(options)
    msg_box.set_title(title)
    msg_box.exec()

    # Retrieve and return the result from the dialog
    return msg_box.get_result()
