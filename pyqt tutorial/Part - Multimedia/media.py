from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QUrl
import sys
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 700, 400)
        self.setWindowTitle("Media")
        
        self.mediaPlayer = QMediaPlayer()
        self.audio = QAudioOutput()

        videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setAudioOutput(self.audio)

        self.mediaPlayer.mediaStatusChanged.connect(self.mediaState_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        openBtn = QPushButton("Open Video")
        openBtn.clicked.connect(self.open_video)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay ))
        self.playBtn.clicked.connect(self.play_video)
        hbox = QHBoxLayout()

        #slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0 , 0)
        self.slider.sliderMoved.connect(self.set_position)


        hbox.addWidget(openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videoWidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        

    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != "":
            self.mediaPlayer.setSource(QUrl.fromLocalFile(filename))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediaState_changed(self):
        if self.mediaPlayer.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))


    def position_changed(self, position):
        self.slider.setValue(position)


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self,position):
        self.mediaPlayer.setPosition(position)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())