from PyQt6.QtWidgets import QDialog, QApplication

import sys

app = QApplication(sys.argv)

window = QDialog()

window.show()

sys.exit(app.exec())