from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 Push button')
        self.create_button()

        self.setStyleSheet('background-color:green')

        lineEdit = QLineEdit(self)
        lineEdit.setFont(QFont('Times New Roman', 15))
        lineEdit.setPlaceholderText('Enter username here')
        lineEdit.setStyleSheet('color:black')

        lineEdit2 = QLineEdit(self)
        lineEdit2.setEchoMode(lineEdit2.EchoMode.Password)
        lineEdit2.setPlaceholderText('**************')


    def create_button(self):
        btn = QPushButton('Click', self)
        btn.setGeometry(100, 100, 130, 40)
        btn.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraBold))

        menu = QMenu()
        menu.setStyleSheet('background-color:purple')
        menu.addAction('Copy')
        menu.addAction('Move')
        btn.setMenu(menu)



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())