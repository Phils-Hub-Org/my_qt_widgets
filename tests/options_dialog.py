import os, sys
from PySide6.QtWidgets import QApplication

# To import Dialogs from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from dialogs.options_dialog import displayOptionsDialog

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    result = displayOptionsDialog('Select an option', ['Call of Duty: Modern Warfare', 'Call of Duty: World at War', 'Call of Duty: Black Ops'], 'Some title!')
    print(f'Selected Option: {result}')

    sys.exit(0)