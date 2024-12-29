from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPen, QPainter, QBrush, QTextDocument
from PyQt6.QtCore import Qt, QRect, QRectF
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Drawing text')

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.drawText(100, 100, 'PyQt6')

        rect = QRect(100, 150, 250, 25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, 'PyQt6 Tutorial')

        document = QTextDocument()
        rect2 = QRectF(0, 0, 250, 250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>This is a PyQt6 text doc </b><i>HTML syntax</i>\n <font size='15' color='red'> Test Color text</font>")

        document.drawContents(painter, rect2)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())