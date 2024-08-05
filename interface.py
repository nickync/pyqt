from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget

class MyInterface(QWidget):
    def __init__(self):
        super().__init__()

        # Create a frame
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)

        # Create layouts
        grid_layout = QGridLayout()
        vbox_layout = QVBoxLayout()
        hbox_layout = QHBoxLayout()

        # Create widgets
        label = QLabel("Label", self)
        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)

        # Add widgets to layouts
        hbox_layout.addWidget(button1)
        hbox_layout.addWidget(button2)
        
        vbox_layout.addWidget(label)
        vbox_layout.addLayout(hbox_layout)
        
        # Add vertical layout to grid layout
        grid_layout.addLayout(vbox_layout, 0, 0)

        # Set layout to the frame
        frame.setLayout(grid_layout)

        # Set the frame as the main layout of the interface
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

# Main application
app = QApplication([])
window = MyInterface()
window.show()
app.exec_()
