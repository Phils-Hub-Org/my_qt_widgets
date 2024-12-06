import os, sys
from PySide6.QtWidgets import QApplication

# To import Dialogs from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from dialogs.yes_no_dialog import displayYesNoDialog

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    result = displayYesNoDialog('Would you like to exit?', 'Some title!')
    print(result)
    
    sys.exit(0)