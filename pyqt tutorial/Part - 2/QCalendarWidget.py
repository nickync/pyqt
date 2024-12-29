from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QCalendarWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 600, 600, 400)
        self.setWindowTitle('PyQt6 QTableWidget')

        self.setStyleSheet('background-color:light')

        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.calendar_date)
        self.calendar.setGridVisible(True)

        hbox = QHBoxLayout()
        
        self.label = QLabel('Hello')
        self.label.setFont(QFont('Times New Roman', 20))

        hbox.addWidget(self.label)
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(hbox)
        
        vbox.addWidget(self.calendar)       

        self.setLayout(vbox)

    def calendar_date(self):
        dateSelected = self.calendar.selectedDate()
        self.label.setText(str(dateSelected.toPyDate()))

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())