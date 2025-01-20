import sys
from PyQt6.QtCore import QThread, pyqtSignal
import time
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class WorkerThread(QThread):
    
    progress_updated = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.progress_updated.emit(i)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QThread example')
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()
        self.button = QPushButton('Start')
        self.button.clicked.connect(self.start_thread)

        vbox.addWidget(self.button)

        self.progess_label = QLabel('Progress: ')
        vbox.addWidget(self.progess_label)

        self.setLayout(vbox)

        self.workerThread = WorkerThread()
        self.workerThread.progress_updated.connect(self.update_progress)

    def start_thread(self):
        self.button.setEnabled(False)
        self.workerThread.start()

    def update_progress(self, value):
        self.progess_label.setText(f'Progress : {value}%')
        if value == 100:
            self.button.setEnabled(True)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())