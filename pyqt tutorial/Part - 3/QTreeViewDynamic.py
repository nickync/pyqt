from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QFileSystemModel
from PyQt6.QtCore import Qt, QFileSystemWatcher, QModelIndex
import sys
import os


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 400, 700, 400)
        self.setWindowTitle('PyQt6 QtreeView Dynamic')

        self.tree_view = QTreeView()

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree_view.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        
        self.setup_file_watcher()
    
    def setup_file_watcher(self):
        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.directoryChanged.connect(self.handle_directory)
        self.file_watcher.fileChanged.connect(self.handle_file_changed)

    def handle_directory(self, directory):
        index = self.model.index(directory)
        self.tree_view.update(index)

    def handle_file_changed(self, file):
        directory = os.path.dirname(file)
        index = self.model.index(directory)
        self.tree_view.update(index)

    def add_directory_to_watch(self, directory):
        self.file_watcher.addPath(directory)

app = QApplication([])

window = Window()
window.add_directory_to_watch(os.getcwd())
window.show()

sys.exit(app.exec())