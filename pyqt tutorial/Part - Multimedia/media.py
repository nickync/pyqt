from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QUrl
import sys
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 700, 400)
        self.setWindowTitle("Media")
        
        self.mediaPlayer = QMediaPlayer()

        videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videoWidget)

        openBtn = QPushButton("Open Video")
        openBtn.clicked.connect(self.open_video)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay ))
        self.playBtn.clicked.connect(self.play_video)
        hbox = QHBoxLayout()

        #slider
        self.slider = QSlider()
        self.slider.setRange(0 ,0)


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
        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())