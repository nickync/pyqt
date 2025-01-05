import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtNetwork import QTcpServer, QHostAddress

class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Server')

        self.label = QLabel(self)

        self.setGeometry( 350, 350, 600, 350)

        self.server = QTcpServer(self)
        self.server.newConnection.connect(self.new_connection)
        self.server.listen(QHostAddress('127.0.0.1'), 8888)

    def new_connection(self):
        client_socket = self.server.nextPendingConnection()
        client_socket.readyRead.connect(self.receive_message)

    def receive_message(self):
        client_socket = self.sender()
        message = client_socket.readAll().data().decode()
        self.label.setText(f'Received: {message}')

app = QApplication(sys.argv)
window = ServerWindow()
window.show()
sys.exit(app.exec())