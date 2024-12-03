from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 QLCD Number')

        self.setStyleSheet('background-color:green')

        self.showLCD()

    def showLCD(self):
        vbox = QVBoxLayout()

        self.lcd = QLCDNumber()

        btn = QPushButton()
        btn.setText('Push me')
        btn.clicked.connect(self.on_click)

        self.lcd.setStyleSheet('background-color:red')

        vbox.addWidget(self.lcd)
        vbox.addWidget(btn)

        self.setLayout(vbox)

    def on_click(self):
        import random
        num = random.random()
        self.lcd.display(str(num))


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())