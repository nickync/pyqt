from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt, QRect
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt Drawingx')

        self.pos1 = [0, 0]
        self.pos2 = [0, 0]

    def paintEvent(self, event):
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]

        painter = QPainter()

        painter.begin(self)
        painter.setBrush(Qt.GlobalColor.white)

        rect = QRect(self.pos1[0], self.pos1[1], width, height)
        painter.setPen(QPen(Qt.GlobalColor.red, 4))

        startAngle = 0
        arLength = 360 * 16
        painter.drawArc(rect, startAngle, arLength)
        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = self.pos().x(), self.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = self.pos().x()+100, self.pos().y()+100
        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())