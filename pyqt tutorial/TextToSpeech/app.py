from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QComboBox, QLabel
from PyQt6.QtTextToSpeech import QTextToSpeech
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text to Speech')

        self.setGeometry(600,0, 800, 600)

        self.text = QLineEdit()

        self.button = QPushButton('Say')
        self.button.clicked.connect(self.say)

        hbox = QHBoxLayout()
        hbox.addWidget(self.text)
        hbox.addWidget(self.button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('Voice'))
        self.comboBox = QComboBox()
        hbox2.addWidget(self.comboBox)

        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.engine = None
        engines = QTextToSpeech.availableEngines()

        if len(engines) > 0:
            engineName = engines[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)

            self.voices = []
            
            for voice in self.engine.availableVoices():
                self.voices.append(voice)
                self.comboBox.addItem(voice.name())
        else:
            self.button.setEnabled(False)

    def stateChanged(self, state):
        if (state == QTextToSpeech.State.Ready):
            self.button.setEnabled(True)

    def say(self):
        self.button.setEnabled(False)
        self.engine.setVoice(self.voices[self.comboBox.currentIndex()])
        #self.engine.setVoice(float(self.ui.horizontalSlier).value()/100)
        self.engine.say(self.text.text())



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())