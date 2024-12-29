import sys
from PyQt6.QtCore import Qt, QObject, QEvent, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class CustomEvent(QEvent):
    Type = QEvent.registerEventType()
    def __init__(self, message):
        super().__init__(CustomEvent.Type)
        self.message = message

class CustomEventEmitter(QObject):
    custom_event = pyqtSignal(CustomEvent)

    def emit_custom_event(self, message):
        event = CustomEvent(message)
        self.custom_event.emit(event)
        
