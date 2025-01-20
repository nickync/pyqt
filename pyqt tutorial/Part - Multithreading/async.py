import sys
import time
from random import randint
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget, QLabel


class WorkerSignals(QObject):
    result_ready = pyqtSignal(int)


class Worker(QRunnable):
    def __init__(self, worker_id, signals):
        super().__init__()
        self.worker_id = worker_id
        self.signals = signals

    def run(self):
        time.sleep(2)
        results = self.worker_id * 10
        self.signals.result_ready.emit(results)


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

        self.thread_pool = QThreadPool()

    def start_tasks(self):
        self.button.setEnabled(False)

        signals = WorkerSignals()

        for i in range(1, 6):
            worker = Worker(i, signals)
            signals.result_ready.connect(self.collect_result)
            self.thread_pool.start(worker)
            

    def collect_result(self, result):
        current_result = self.results_label.text()
        new_result = f"Worker Result : {result}"
        self.results_label.setText(current_result + "\n" + new_result)

        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

        if self.thread_pool.activeThreadCount() == 0:
            self.button.setEnabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())