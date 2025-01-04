from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt QGraphic')

        scene = QGraphicsScene()

        greenBrush = QBrush(Qt.GlobalColor.green)
        yellowBrush = QBrush(Qt.GlobalColor.yellow)

        redPen = QPen(Qt.GlobalColor.red)
        redPen.setWidth(7)

        ellipse = scene.addEllipse(100, 100, 200, 200, redPen, greenBrush)
        rect = scene.addRect(-100, -100, 200, 200, redPen, yellowBrush)

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        view = QGraphicsView(scene, self)
        view.setGeometry(0, 0, 800, 600)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())