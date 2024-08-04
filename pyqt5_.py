import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Application")
        self.setGeometry(100, 100, 400, 300)

        # Set up a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add widgets to the layout
        self.label = QLabel("Hello, PyQt5!")
        layout.addWidget(self.label)
        
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)
        
    def on_button_click(self):
        self.label.setText("Button Clicked!")

# Main part of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
