from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPen, QPainter, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing Ellipse')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.green, 5, Qt.PenStyle.DashLine))
        painter.setBrush(QBrush(Qt.GlobalColor.white, Qt.BrushStyle.CrossPattern))
        painter.drawEllipse(100, 100, 400, 200)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())