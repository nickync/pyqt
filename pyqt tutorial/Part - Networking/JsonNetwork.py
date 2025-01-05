from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
import sys
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import json
from PyQt6.QtCore import QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle('Working with JSON Data')

        vbox = QVBoxLayout()
        
        self.text_edit = QTextEdit()
        self.text_edit.setMinimumHeight(300)
        vbox.addWidget(self.text_edit)

        self.button = QPushButton('Fetch JSON')
        self.button.clicked.connect(self.fetch_json)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)


    def fetch_json(self):
        url = QUrl('https://jsonplaceholder.typicode.com/posts')
        request = QNetworkRequest(url)
        self.network_manager.get(request)

    def handle_response(self, reply:QNetworkReply):
        if reply.error() != QNetworkReply.NetworkError.NoError:
            error_msg = reply.errorString()
            self.text_edit.append(f'Error occured : {error_msg}')
        else:
            data = reply.readAll().data()
            json_data = json.loads(data)
            self.text_edit.append('Received JSON Data : ')
            for item in json_data:
                self.text_edit.append(f'Title : {item['title']}')
                self.text_edit.append(f'Body : {item['body']}')
                self.text_edit.append('-------------------')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
