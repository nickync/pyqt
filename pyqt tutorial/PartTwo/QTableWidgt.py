from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLineEdit, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 600, 600, 400)
        self.setWindowTitle('PyQt6 QTableWidget')

        self.setStyleSheet('background-color:light')

        self.label_result = QLabel('')
        self.label_result.setFont(QFont('Times', 16))

        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem('Name'))
        table_widget.setItem(0, 1, QTableWidgetItem('Email'))
        table_widget.setItem(0, 2, QTableWidgetItem('Phone'))

        table_widget.setItem(1, 0, QTableWidgetItem('Leo'))
        table_widget.setItem(1, 1, QTableWidgetItem('email@email.com'))
        table_widget.setItem(1, 2, QTableWidgetItem('321456789'))

        table_widget.setItem(2, 0, QTableWidgetItem('Kim'))
        table_widget.setItem(2, 1, QTableWidgetItem('email@email.com'))
        table_widget.setItem(2, 2, QTableWidgetItem('321456789'))

        vbox.addWidget(table_widget)

        self.setLayout(vbox)

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())