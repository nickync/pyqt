from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication([])

engine = QQmlApplicationEngine()

engine.load('QtQuick/window.qml')

sys.exit(app.exec())