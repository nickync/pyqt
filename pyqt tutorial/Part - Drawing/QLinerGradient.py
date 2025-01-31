from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QLinearGradient, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Linear Gradient')

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))

        grad1= QLinearGradient(25, 100, 150, 175)

        grad1.setColorAt(0.0, Qt.GlobalColor.red)
        grad1.setColorAt(0.5, Qt.GlobalColor.green)
        grad1.setColorAt(1, Qt.GlobalColor.cyan)

        painter.setBrush(QBrush(grad1))

        painter.drawRect(10, 10, 200, 200)



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())