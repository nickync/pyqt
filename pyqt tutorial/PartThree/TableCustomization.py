from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTreeView, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QStandardItem, QStandardItemModel
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 400, 700, 400)
        self.setWindowTitle('PyQt6 QtreeView')

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.setup_table()

    def setup_table(self):
        self.table_widget.setColumnCount(5)
        self.table_widget.setRowCount(5)

        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = QTableWidgetItem(f'Row {row + 1}, Column {col +1}')
                self.table_widget.setItem(row, col, item)

        self.table_widget.setStyleSheet(
            """
                QTableWidget::item{
                    background-color:green;
                    font-family:'Times New Roman';
                    border: 1px solid blue;
                    padding:5px;
                }

                QTableWidget::item:selected{
                background-color:#A9D9F7;
                }
            """
        )


app = QApplication([])

window = Window()

window.show()

sys.exit(app.exec())