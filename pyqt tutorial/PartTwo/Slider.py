from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QSlider
from PyQt6.QtGui import QFont
import sys
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 600, 600, 400)
        self.setWindowTitle('PyQt6 Slider')

        self.setStyleSheet('background-color:green')

        self.label_result = QLabel('Hi')
        self.label_result.setFont(QFont('Times', 16))

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(1)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changed_slider)

        self.label = QLabel('Test')
        self.label.setFont(QFont('Times', 16))


        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)


    def changed_slider(self):
        value = self.slider.value()
        self.label.setNum(value)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())