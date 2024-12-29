from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QHBoxLayout, QLabel, QComboBox, QVBoxLayout
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 600, 600, 400)
        self.setWindowTitle('PyQt6 Combo BOX')

        self.setStyleSheet('background-color:green')

        self.label_result = QLabel('')
        self.label_result.setFont(QFont('Times', 16))

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel('Select account type: ')
        label.setFont(QFont('Times' , 16))

        self.combo = QComboBox()
        self.combo.currentTextChanged.connect(self.combo_changed)
        self.combo.addItem('Current Account')
        self.combo.addItem('Checking Account')
        self.combo.addItem('Savings Account')
        #self.combo.setEditable(True)

        vbox = QVBoxLayout()

        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)

        hbox.addWidget(label)
        hbox.addWidget(self.combo)
        self.setLayout(vbox)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText('You Account Type is : {}'.format(item))

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())