from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 200, 600, 600)
        self.setWindowTitle('Label Test')

        label = QLabel('Python Gui Dev', self)
        # label.setText('New Label')
        # label.move(100, 100)
        # label.setFont(QFont('Times New Roman', 15))
        # label.setStyleSheet('background-color: gray; color:blue')
        
        # pixmap = QPixmap('img/0.png')
        # label.setPixmap(pixmap)

        movie = QMovie('img/one.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())