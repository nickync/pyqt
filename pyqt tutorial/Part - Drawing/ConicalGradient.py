from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QConicalGradient
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 3, Qt.PenStyle.DashDotLine))

        conicalGradient = QConicalGradient(100, 100, 10)

        conicalGradient.setColorAt(0, Qt.GlobalColor.red)
        conicalGradient.setColorAt(0.8, Qt.GlobalColor.green)
        conicalGradient.setColorAt(1, Qt.GlobalColor.yellow)

        painter.setBrush(QBrush(conicalGradient))
        painter.drawRect(50, 10, 400, 400)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())