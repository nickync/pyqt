from PyQt6.QtWidgets import QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Health(QGraphicsTextItem):
    def __init__(self):
        super().__init__()

        self.health = 3

        self.setPlainText('Health : ' + str(self.health))
        self.setDefaultTextColor(Qt.GlobalColor.darkRed)
        self.setFont(QFont('Times New Roman', 14))


    def decrease(self):
        self.health -= 1

        if self.health < 0:
            self.health = 0

        self.setPlainText(f"Health : {self.health}")

    def is_alive(self):
        return self.health > 0