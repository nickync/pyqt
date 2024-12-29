from PyQt6.QtWidgets import QMainWindow, QApplication

import sys

app = QApplication(sys.argv)

window = QMainWindow()

window.statusBar().showMessage('Welcome to PyQt6 course!')
window.menuBar().addMenu('File')

window.show()

sys.exit(app.exec())