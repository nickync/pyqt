import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag


class DraggableLabel(QLabel):

    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)

            mime_data = QMimeData()
            mime_data.setText(self.text())
            
            drag.setMimeData(mime_data)
            drag.exec(Qt.DropAction.MoveAction)


class DropableLabel(QLabel):

    def __init__(self, text):
        super().__init__(text)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        text = event.mimeData().text()
        self.setText(text)
        event.acceptProposedAction()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Drag and drop')
        self.setGeometry(100, 100, 300, 200)

        self.init_ui()


    def init_ui(self):
        vbox = QVBoxLayout()

        draggable_label = DraggableLabel('Drag Me')
        droppable_label = DropableLabel('Drop Label Field')

        vbox.addWidget(draggable_label)
        vbox.addWidget(droppable_label)

        self.setLayout(vbox)
    

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
            