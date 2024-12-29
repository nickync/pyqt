from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTreeView, QTableWidget, QTableWidgetItem, QTabWidget, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 400, 700, 400)
        self.setWindowTitle('PyQt6 Table Sorting')

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.filter_edit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.filter_edit)
        vbox.addWidget(self.table_widget)

        main_widget = QWidget()
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)
        self.setup_table()
        self.setup_connection()

    def setup_table(self):
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['Name', 'Category', 'Price', 'Date'])

        data = [
            ('p1', 'A', '10', '2023-10-15'),
            ('p2', 'B', '30', '2023-11-15'),
            ('p4', 'V', '220', '2023-12-15'),
            ('p5', 'D', '110', '2024-10-15')
        ]
        
        self.table_widget.setRowCount(len(data))

        for row, (name, category, price, date) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(category))
            self.table_widget.setItem(row, 2, QTableWidgetItem(price))
            self.table_widget.setItem(row, 3, QTableWidgetItem(date))

    def setup_connection(self):
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.filter_edit.textChanged.connect(self.filter_table)

    def sort_table(self, col):
        self.table_widget.sortItems(col, Qt.SortOrder.AscendingOrder)

    def filter_table(self, filter_text):
        for row in range(self.table_widget.rowCount()):
            match = False
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if filter_text.lower() in item.text().lower():
                    match = True
                    break
            self.table_widget.setRowHidden(row, not match)

    


app = QApplication([])

window = Window()

window.show()

sys.exit(app.exec())