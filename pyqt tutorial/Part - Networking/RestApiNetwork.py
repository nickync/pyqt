import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtCore import QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Rest API')

        self.setGeometry( 350, 350, 600, 350)

        vbox = QVBoxLayout()

        url_label = QLabel('URL : ')
        self.input = QLineEdit()
        self.input.setText('https://jsonplaceholder.typicode.com/posts')
        send_button = QPushButton('Send Request')
        send_button.clicked.connect(self.send_request)

        response_label = QLabel('Response : ')
        self.reponse_text = QTextEdit()
        self.reponse_text.setReadOnly(True)

        vbox.addWidget(url_label)
        vbox.addWidget(self.input)
        vbox.addWidget(send_button)

        vbox.addWidget(response_label)
        vbox.addWidget(self.reponse_text)

        self.setLayout(vbox)

        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)


    def send_request(self):
        url = self.input.text()
        request = QNetworkRequest(QUrl(url))
        self.network_manager.get(request)

    def handle_response(self, reply):
        error = reply.error()

        if error == QNetworkReply.NetworkError.NoError:
            response = reply.readAll().data().decode('utf-8')
            self.reponse_text.setPlainText(response)
        else:
            error_message = reply.errorString()
            self.reponse_text.setPlainText(f'Error : {error_message}')

    def closeEvent(self, event):
        self.network_manager.deleteLater()
        super().closeEvent(event)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())