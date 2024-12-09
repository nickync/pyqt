import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QStackedLayout, QTextEdit
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QFormLayout')
        self.setGeometry(600, 100, 700, 700)
        
        main_layout = QVBoxLayout()

        form_layout = QFormLayout()

        label1 = QLabel('Name : ')
        line1 = QLineEdit()

        label2 = QLabel('Email : ')
        line2 = QLineEdit()

        label3 = QLabel('Phone : ')
        line3 = QLineEdit()

        form_layout.addRow(label1, line1)
        form_layout.addRow(label2, line2)
        form_layout.addRow(label3, line3)

        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            