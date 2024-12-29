from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QRadialGradient
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing Radial Gradient')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))

        radialGradient = QRadialGradient(100, 100, 100)

        radialGradient.setColorAt(0.4, Qt.GlobalColor.darkGray)
        radialGradient.setColorAt(0.8, Qt.GlobalColor.green)
        radialGradient.setColorAt(1, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(radialGradient))

        painter.drawRect(10, 0, 300, 300)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())