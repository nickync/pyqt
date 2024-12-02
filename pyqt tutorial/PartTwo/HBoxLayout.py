from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QHBoxLayout
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 HBox')

        hbox = QHBoxLayout()

        btn1 = QPushButton('Click 1')
        btn2 = QPushButton('Click 2')
        btn3 = QPushButton('Click 3')
        btn4 = QPushButton('Click 4')

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        #hbox.addSpacing(100)
        #hbox.addStretch(10)

        self.setLayout(hbox)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())