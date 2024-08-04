import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt  # Import Qt for alignment constants

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QFrame Example")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Set up a layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QFrame
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(2)
        frame.setMidLineWidth(1)
        
        # Add a label inside the frame
        label = QLabel("This is a QFrame")
        label.setAlignment(Qt.AlignCenter)
        
        # Set up a frame layout and add the label
        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(label)
        
        # Add the frame to the main layout
        layout.addWidget(frame)

# Main part of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
