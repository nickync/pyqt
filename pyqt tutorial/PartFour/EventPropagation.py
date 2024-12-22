from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('Event Propagation')

        vbox = QVBoxLayout()

        self.parent_button = QPushButton('Parent Button')
        vbox.addWidget(self.parent_button)
        self.parent_button.clicked.connect(self.parent_button_clicked)

        self.child_button = QPushButton('Child Button')
        vbox.addWidget(self.child_button)
        self.child_button.clicked.connect(self.child_button_clicked)

        self.setLayout(vbox)

    def parent_button_clicked(self):
        print('Parent Button Clicked')
        self.parent_button.setStyleSheet('background-color:green;')


    def child_button_clicked(self):
        print('Child Button Clicked')
        self.child_button.setStyleSheet('background-color:red')
        self.parent_button_clicked()

        


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())