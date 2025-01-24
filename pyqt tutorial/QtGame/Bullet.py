from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import QTimer
from Enemy import Enemy
from Score import Score

class Bullet(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        self.setRect(0, 0, 10, 50)

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)

        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() - 10)

        colliding_items = self.collidingItems()

        for item in colliding_items:
            if isinstance(item, Enemy):
                
                for scene_item in self.scene().items():
                    if isinstance(scene_item, Score):
                        scene_item.increase()
                        print('Score increased')

                self.scene().removeItem(item)
                self.scene().removeItem(self)

                print('Bullet hit enemy!')
                
                self.timer.stop()

                del item
                del self

            return
        
        if self.y() + self.rect().height() < 0:
            self.scene().removeItem(self)
            self.timer.stop()