import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLayoutItem, QSizePolicy, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Nested Layout')
        self.setGeometry(600, 100, 700, 700)

        main_layout = QVBoxLayout()

        row1_layout = QHBoxLayout()

        label1 = QLabel('First name :  ')
        line1 = QLineEdit()

        row1_layout.addWidget(label1)
        row1_layout.addWidget(line1)

        row2_layout = QHBoxLayout()

        label2 = QLabel('Last name :  ')
        line2 = QLineEdit()

        row2_layout.addWidget(label2)
        row2_layout.addWidget(line2)

        row3_layout = QHBoxLayout()
        btn = QPushButton('Submit')
        row3_layout.addWidget(btn)

        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row2_layout)
        main_layout.addLayout(row3_layout)

        self.setLayout(main_layout)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            