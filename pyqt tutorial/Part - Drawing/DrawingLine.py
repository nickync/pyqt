from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing')

        self.pos1 = [0, 0]
        self.pos2 = [0, 0]

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 4))

        painter.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = self.pos().x(), self.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = self.pos().x(), self.pos().y()
        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())