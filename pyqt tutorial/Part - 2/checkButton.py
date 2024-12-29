from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMenu, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt6 check box')
        self.setGeometry(200, 200, 400, 400)

        self.setStyleSheet('background-color:gray')

        hbox = QHBoxLayout()

        self.label = QLabel('Title choice', self)

        self.check1 = QCheckBox('Python')
        self.check1.stateChanged.connect(self.item_selected)
        self.check2 = QCheckBox('Java')
        self.check2.stateChanged.connect(self.item_selected)
        self.check3 = QCheckBox('C++')
        self.check3.stateChanged.connect(self.item_selected)

        hbox.addWidget(self.check1)
        hbox.addWidget(self.check2)
        hbox.addWidget(self.check3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_selected(self):
        value = ''
        if self.check1.isChecked():
            value = self.check1.text()
        elif self.check2.isChecked():
            value = self.check2.text()
        elif self.check3.isChecked():
            value = self.check3.text()

        self.label.setText(value)

    def on_clicked(self):
        btn = self.sender()
        if btn.isChecked():
            self.label.setText(btn.text())


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())