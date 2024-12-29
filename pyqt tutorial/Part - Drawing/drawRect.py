from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing Rectangle')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.darkCyan, Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(200, 15, 300, 100)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())