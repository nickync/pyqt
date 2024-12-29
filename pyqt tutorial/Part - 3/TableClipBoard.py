from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTreeView, QTableWidget, QTableWidgetItem, QTabWidget, QLineEdit, QVBoxLayout, QMenu
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QAction, QKeySequence
from PyQt6.QtCore import Qt, QMimeData
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

        self.table_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.create_context_menu_options()
        self.table_widget.addAction(self.copy_action)
        self.table_widget.addAction(self.paste_action)

    def create_context_menu_options(self):
        self.copy_action = QAction('Copy')
        self.copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        self.copy_action.triggered.connect(self.copy_selected_cell)


        self.paste_action = QAction('Paste')
        self.paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        self.paste_action.triggered.connect(self.paste_selected_cell)

    def copy_selected_cell(self):
        selection = self.table_widget.selectedRanges()
        if not selection:
            return
        cells_text = []
        for selection_range in selection:
            for row in range(selection_range.topRow(), selection_range.bottomRow() + 1):
                for col in range(selection_range.leftColumn(), selection_range.rightColumn() + 1):
                    item = self.table_widget.item(row, col)
                    if item:
                        cells_text.append(item.text())


        mimeData = QMimeData()
        mimeData.setText('\t'.join(cells_text))
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def paste_selected_cell(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasText():
            text = mimeData.text()
            cells_text = text.split('\t')

            cuurrent_range = self.table_widget.selectedRanges()[0]

            toprow = cuurrent_range.topRow()
            leftcolumn = cuurrent_range.leftColumn()

            for row in range(cuurrent_range.rowCount()):
                for col in range(cuurrent_range.columnCount()):
                    item = self.table_widget.item(toprow + row, leftcolumn + col)

                    if item:
                        if cells_text:
                            item.setText(cells_text.pop(0))
                        else:
                            return
                        
    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.addAction(self.copy_action)
        context_menu.addAction(self.paste_action)
        context_menu.exec(event.globalPos())


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