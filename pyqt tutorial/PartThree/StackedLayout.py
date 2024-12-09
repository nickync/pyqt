import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QStackedLayout
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QStackedWidget Layout')
        self.setGeometry(600, 100, 700, 700)
        self.init_ui()


    def init_ui(self):
        main_layout = QVBoxLayout()

        stackedLayout = QStackedLayout()

        view1 = QLabel('View 1')
        view2 = QLabel('View 2')
        view3 = QLabel('View 3')

        stackedLayout.addWidget(view1)
        stackedLayout.addWidget(view2)
        stackedLayout.addWidget(view3)

        stackedLayout.setCurrentIndex(0)

        button1 = QPushButton('View 1')
        button2 = QPushButton('View 2')
        button3 = QPushButton('View 3')

        button1.clicked.connect(lambda : stackedLayout.setCurrentIndex(0))
        button2.clicked.connect(lambda : stackedLayout.setCurrentIndex(1))
        button3.clicked.connect(lambda : stackedLayout.setCurrentIndex(2))

        btnLayout = QHBoxLayout()

        btnLayout.addWidget(button1)
        btnLayout.addWidget(button2)
        btnLayout.addWidget(button3)

        main_layout.addLayout(stackedLayout)

        main_layout.addLayout(btnLayout)

        self.setLayout(main_layout)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            