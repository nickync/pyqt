import sys
import time
from random import randint
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget, QLabel

class Worker(QThread):
    result_ready = pyqtSignal(int)

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        time.sleep(randint(1, 5))
        result = self.worker_id * 10
        self.result_ready.emit(result)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sync example')
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()
        self.button = QPushButton('Start')
        self.button.clicked.connect(self.start_tasks)

        self.scroll_area = QScrollArea()
        self.results_label = QLabel("Results : ")
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.results_label)

        vbox.addWidget(self.button)
        vbox.addWidget(self.scroll_area)
        self.setLayout(vbox)

        self.worker_threads = []

    def start_tasks(self):
        self.button.setEnabled(False)

        for i in range(1, 6):
            worker = Worker(i)
            worker.result_ready.connect(self.collect_result)
            self.worker_threads.append(worker)
            worker.start()

    def collect_result(self, result):
        current_result = self.results_label.text()
        new_result = f"Worker Result : {result}"
        self.results_label.setText(current_result + "\n" + new_result)

        if len(self.worker_threads) == len([t for t in self.worker_threads if not t.isRunning() ]):
            self.button.setEnabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())