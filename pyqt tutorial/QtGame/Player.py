from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt, QUrl
from Bullet import Bullet
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class Player(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        self.sound = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setVolume(0.1)
        self.sound.setAudioOutput(self.audio)

        file = QUrl.fromLocalFile('QtGame/bullet2.mp3')
        self.sound.setSource(file)
      
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.sound.play()
            print('Space is pressed')
            bullet = Bullet()
            bullet.setPos(self.x() + self.rect().width()/2 - bullet.rect().width()/2, self.y())
            self.scene().addItem(bullet)
            
        elif event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())
        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())
        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)
        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)