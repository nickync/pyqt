from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(20, 40, 700, 400)
        self.setWindowTitle('Python PyQt6 GUI Dev')
        self.setWindowIcon(QIcon('./PartOne/Images/CN.svg'))
        
        # self.setFixedHeight(200)
        # self.setFixedWidth(1200)

        self.setStyleSheet('background-color:green')
        self.setWindowOpacity(0.2)



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())