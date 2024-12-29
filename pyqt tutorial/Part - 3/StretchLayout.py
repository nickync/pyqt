import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpacerItem, QLayoutItem, QSizePolicy, QPushButton
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Stretch')
        self.setGeometry(600, 100, 300, 200)

        vbox = QVBoxLayout()

        label1 = QLabel('Strech Label')
        label2 = QLabel('Fixed Label')

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        vbox.setStretch(0, 1)
        vbox.setStretch(1, 0)

        btn = QPushButton('Add Spacer')
        
        # click add spacer
        btn.clicked.connect(self.add_spacer)

        vbox.addWidget(btn)

        self.setLayout(vbox)

    def add_spacer(self):
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = self.layout()

        layout.addItem(spacer)



app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            