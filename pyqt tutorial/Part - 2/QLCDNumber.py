from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 QLCD Number')

        self.setStyleSheet('background-color:green')

        timer = QTimer()
        timer.timeout.connect(self.showLCD)

        
        timer.start(1000)
        self.showLCD()

    def showLCD(self):
        vbox = QVBoxLayout()

        lcd = QLCDNumber()

        lcd.setStyleSheet('background-color:red')

        vbox.addWidget(lcd)

        time = QTime.currentTime()
        text = time.toString('hh:mm')

        lcd.display(text)

        self.setLayout(vbox)



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())