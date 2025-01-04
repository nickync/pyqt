from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QFont
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('PyQt Mouse Event')
        self.setMouseTracking(True)
        vbox = QVBoxLayout()

        self.label = QLabel('Mouse Track')
        self.label.setFont(QFont("Times", 15))

        self.label_press = QLabel('Mouse Press')
        self.label_press.setFont(QFont("Times", 18))

        self.label_release = QLabel('Mouse Release')
        self.label_release.setFont(QFont("Times", 22))
    

        vbox.addWidget(self.label)
        vbox.addWidget(self.label_press)
        vbox.addWidget(self.label_release)

        self.setLayout(vbox)

    def mouseMoveEvent(self, event):
        x = self.x()
        y = self.y()

        text = "X: {0}, Y:{1}".format(x, y)
        self.label.setText(text)
        self.update()

    def mousePressEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton:
            x = self.x()
            y = self.y()
            text = "X: {0}, Y:{1}".format(x, y)
            self.label_press.setText(text)

    def mouseReleaseEvent(self, event):

        x = self.x()
        y = self.y()
        text = "X: {0}, Y:{1}".format(x, y)
        self.label_release.setText(text)
        self.update()


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())