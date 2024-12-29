from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 200, 600, 600)
        self.setWindowTitle('Label Test')

        vbox = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Label')
        self.label.setFont(QFont('Times New Roman', 20))
        self.label.setStyleSheet('background-color:green')
        

        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, 'Python')
        self.list_widget.insertItem(1, 'Java')
        self.list_widget.insertItem(2, 'C++')
        self.list_widget.setFont(QFont('Times', 14))
        self.list_widget.setStyleSheet('background-color:gray')
        self.list_widget.clicked.connect(self.on_click)

        vbox.addWidget(self.label)
        vbox.addWidget(self.list_widget)

        self.setLayout(vbox)

    def on_click(self):
        item = self.list_widget.currentItem()
        self.label.setText('You have selected: {}'.format(item.text()))


app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())