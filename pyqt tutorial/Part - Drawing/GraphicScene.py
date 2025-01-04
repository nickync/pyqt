from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.show()

        scene = QGraphicsScene()

        # create rect item
        rect = QGraphicsRectItem()
        rect.setRect(0, 0, 100, 100)
        scene.addItem(rect)

        self.setScene(scene)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())