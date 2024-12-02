from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QHBoxLayout, QGridLayout, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 HBox')

        self.create_widge()

    def create_widge(self):
        hbox = QHBoxLayout()
        btn = QPushButton('Change Text')
        btn.clicked.connect(self.on_click)
        
        self.label = QLabel('Default Text')

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def on_click(self):
        self.label.setText('button Clicked')
        self.label.setFont(QFont('Times New Roman', 30))
        self.setStyleSheet('color:red')



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())