from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from random import randint

from Health import Health

class Enemy(QGraphicsPixmapItem):

    def __init__(self):
        super().__init__()

        random_number = randint(10, 1000) % 700

        self.setPos(random_number, 0)

        #self.setRect(0, 0, 100, 100)
        self.setPixmap(QPixmap('QtGame/enemy.png'))

        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() + 5)

        if self.pos().y() + self.pixmap().height() < 0:
            self.scene().removeItem(self)
            print('Deleted')

        colliding_items = self.collidingItems()

        for item in colliding_items:
            from Player import Player
            if isinstance(item, Player):
                for scene_item in self.scene().items():
                    if isinstance(scene_item, Health):
                        scene_item.decrease()
                        print("Player is hit")

                        if not scene_item.is_alive():
                            print("You're DEAD")
                            self.scene().views()[0].close()

            self.scene().removeItem(self) # remove enemy after collison
            self.timer.stop()
            return