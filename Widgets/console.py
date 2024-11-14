import logging
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from Resources.UI.ui_console import Ui_ConsoleWidget

logger = logging.getLogger(__name__)

class Console(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)
    
    def initialize(self):
        self.ui.close_console_btn.clicked.connect(self.hide)
        self.ui.clear_console_btn.clicked.connect(self.ui.console.clear)
        