import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from Player import Player
from PyQt6.QtCore import Qt, QTimer, QUrl
from Enemy import Enemy
from Score import Score
from Health import Health
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class Window(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setGeometry(0 ,0, 800, 600)
        self.scene = QGraphicsScene()

        #rect = QGraphicsRectItem()
        #rect.setRect(0, 0, 100, 100)

        self.player = Player()
        self.player.setRect(0, 0, 100, 100)
        self.scene.addItem(self.player)

        self.setScene(self.scene)

        self.player.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.player.setFocus()

        self.setWindowTitle('Game')

        # no infinite bullet screen
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFixedSize(800, 600)
        self.scene.setSceneRect(0, 0, 800, 600)
        self.player.setPos(self.scene.width()/2 - self.player.rect().width()/2, self.scene.height() - self.player.rect().height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.spawn_enemy)
        self.timer.start(3000)

        # score
        self.score = Score()
        self.scene.addItem(self.score)

        # health
        self.health = Health()
        self.health.setPos(self.health.x(), self.health.y() + 20)
        self.scene.addItem(self.health)

        self.setup_bgm()

    def spawn_enemy(self):
        enemy = Enemy()
        self.scene.addItem(enemy)

    def setup_bgm(self):
        self.mediaPlayer = QMediaPlayer()
        self.audio = QAudioOutput()

        self.audio.setVolume(0.1)
        self.mediaPlayer.setAudioOutput(self.audio)

        music = QUrl.fromLocalFile('QtGame/bg3.mp3')
        self.mediaPlayer.setSource(music)

        self.mediaPlayer.play()



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())