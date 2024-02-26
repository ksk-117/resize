import sys
from PySide6.QtWidgets import QApplication
from fixed_size import FileDialogApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileDialogApp()
    window.show()
    sys.exit(app.exec())
