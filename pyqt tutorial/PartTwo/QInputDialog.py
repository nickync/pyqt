from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QDialog, QInputDialog
from PyQt6.QtGui import QFont
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 600, 600, 400)
        self.setWindowTitle('PyQt6 Input Dialog')

        self.setStyleSheet('background-color:teal')

        self.create_dialog()

    def create_dialog(self):
        hbox = QHBoxLayout()

        label = QLabel('Choose a Country: ')
        label.setFont(QFont('Times New Roman'))

        self.lineEdit = QLineEdit()

        btn = QPushButton('Choose Country')
        btn.clicked.connect(self.get_int)

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(btn)

        self.setLayout(hbox)

    def show_dialog(self):
        countries = ['Algeria', 'USA', 'UK', 'CHINA', 'CANADA']
        country, ok = QInputDialog.getItem(self, 'Input Dialog', 'List of Countries', countries, 0, False)

        if ok and country:
            self.lineEdit.setText(country)

    def get_text(self):
        mytext, ok = QInputDialog.getText(self, 'Get Username', 'Enter Your Name :')
        if ok and mytext:
            self.lineEdit.setText(mytext)

    def get_int(self):
        myNumber, ok = QInputDialog.getInt(self, 'Order Quantity', 'Enter Quantity: ', 1, 2, 30, 50)
        if ok and myNumber:
            self.lineEdit.setText(str(myNumber))


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())