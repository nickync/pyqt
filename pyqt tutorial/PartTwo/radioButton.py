from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QRadioButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 Push button')
        self.setGeometry(200, 200, 400, 400)
        self.create_button()

        self.setStyleSheet('background-color:gray')


    def create_button(self):
        qbox = QVBoxLayout()

        btn1 = QRadioButton('Python')
        btn1.setGeometry(100, 100, 130, 40)
        btn1.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraBold))
        btn1.toggled.connect(self.on_clicked)

        btn2 = QRadioButton('Java')
        btn2.setGeometry(100, 100, 130, 40)
        btn2.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraBold))
        btn2.setChecked(True)
        btn2.toggled.connect(self.on_clicked)

        btn3 = QRadioButton('C++')
        btn3.setGeometry(100, 100, 130, 40)
        btn3.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraBold))
        btn3.toggled.connect(self.on_clicked)

        self.label = QLabel('Radio s')
        qbox.addWidget(self.label)

        qbox.addWidget(btn1)
        qbox.addWidget(btn2)
        qbox.addWidget(btn3)

        self.setLayout(qbox)


    def on_clicked(self):
        btn = self.sender()
        if btn.isChecked():
            self.label.setText(btn.text())


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())