from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 HBox')

        grid = QGridLayout()

        btn1 = QPushButton('Click 1')
        btn2 = QPushButton('Click 2')
        btn3 = QPushButton('Click 3')
        btn4 = QPushButton('Click 4')

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 1, 1)

        self.setLayout(grid)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())