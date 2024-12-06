import os, sys
from PySide6.QtWidgets import QApplication

# To import Dialogs from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from dialogs.input_dialog import displayInputDialog, InputDialogResultEnum

if __name__ == '__main__':
    app = QApplication([])

    result = displayInputDialog('Enter a new tooltip!', 'Some title!')

    if result == InputDialogResultEnum.EMPTY:
        print('Input was empty')
    elif result == InputDialogResultEnum.CANCEL:
        print('Input was cancelled')
    else:
        print(f'Input was: {result.input}')

    sys.exit(0)