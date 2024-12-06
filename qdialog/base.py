# xSS/ui/ui_base.py

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

logger = logging.getLogger(__name__)

class DialogBase(QDialog):
    """
    Base class for dialog windows.

    Set Attributes:
        self.setAttribute(Qt.WA_TranslucentBackground, True)
    
    Set Window Flags:
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    Class Attributes:
        ui (object): The user interface object for the dialog window.
    
    Methods:
        __init__(): Initializes the DialogBase class.
        loadUI(ui_module: object): Loads the user interface for the dialog window.
    
    Example:
        dialog = DialogBase()
        dialog.loadUI(Ui_Dialog)
    
    Note:
        This class should be used as the base class for all dialog windows in the application.
    """
    def __init__(self) -> None:
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    
    def loadUI(self, ui_module: object) -> None:
        self.ui = ui_module()
        self.ui.setupUi(self)