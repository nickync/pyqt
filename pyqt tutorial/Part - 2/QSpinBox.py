from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QSpinBox, QLineEdit
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 SpinBox')
        self.setGeometry(1400, 400, 400, 400)

        self.setStyleSheet('background-color:white')

        hbox = QHBoxLayout()

        label = QLabel('Laptop Price: ')
        label.setFont(QFont('Times', 15))

        self.lineEdit = QLineEdit()

        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.on_clicked)

        self.total_result = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinBox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)


    def on_clicked(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            totalPrice = price * self.spinBox.value()

            self.total_result.setText(str(totalPrice))
        else:
            print('Wrong value')

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())