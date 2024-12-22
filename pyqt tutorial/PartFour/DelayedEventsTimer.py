from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer, QElapsedTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('Timer and Delayed Events')

        vbox = QVBoxLayout()

        self.label = QLabel('Inital Text')
        vbox.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)

        self.elapsed_timer = QElapsedTimer()

        self.setLayout(vbox)

    def start_timer(self):
        self.timer.start()
        self.elapsed_timer.start()

    def update_label(self):
        self.label.setText(f"Elapsed Time: {self.elapsed_timer.elapsed() / 1000:.1f} seconds" )



app = QApplication(sys.argv)
window = Window()
window.show()
window.start_timer()

sys.exit(app.exec())