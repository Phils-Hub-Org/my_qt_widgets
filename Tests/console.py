import os, sys
from PySide6.QtWidgets import QApplication

# To import Widgets from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from Widgets.console import Console

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    console = Console()
    console.initialize()
    console.show()
    
    sys.exit(app.exec())