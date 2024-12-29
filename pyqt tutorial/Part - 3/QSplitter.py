import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSplitter, QStackedLayout, QTextEdit
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QStackedWidget Layout')
        self.setGeometry(600, 100, 700, 700)
        
        main_layout = QVBoxLayout()

        splitter = QSplitter()

        edit1 = QTextEdit()
        edit2 = QTextEdit()

        splitter.addWidget(edit1)
        splitter.addWidget(edit2)

        splitter.setSizes([200, 400])

        main_layout.addWidget(splitter)

        self.setLayout(main_layout)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            