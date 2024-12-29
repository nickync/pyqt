from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle('Event handling')

        button = QPushButton('Click Me')
        button.clicked.connect(self.handle_clicked)
        vbox = QVBoxLayout()
        vbox.addWidget(button)

        self.label = QLabel('No button clicked')
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.installEventFilter(self)

    def handle_clicked(self):
        self.label.setText('clickked')

    def eventFilter(self, obj, event):
        if obj is self and event.type() == event.Type.KeyPress:
            print(' Key Pressed : ', event.key())
            self.label.setText(str(event.key()))
            return True
        return super().eventFilter(obj, event)



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())