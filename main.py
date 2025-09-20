from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maze generator")
        self.setFixedSize(QSize(400, 300))

        self.width_label = QLabel('width')
        self.width = QLineEdit()
        self.width.textChanged.connect(self.width.setText)

        self.hight_label = QLabel('height')
        self.hight = QLineEdit()
        self.hight.textChanged.connect(self.hight.setText)
        
        self.min_lines_label = QLabel('min_lines')
        self.min_lines = QLineEdit()
        self.min_lines.textChanged.connect(self.min_lines.setText)

        self.button = QPushButton("Generate!")
        self.button.clicked.connect(self.generate_maze)

        layout = QVBoxLayout()
        layout.addWidget(self.width_label)
        layout.addWidget(self.width)
        layout.addWidget(self.hight_label)
        layout.addWidget(self.hight)
        layout.addWidget(self.min_lines_label)
        layout.addWidget(self.min_lines)
        
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        
        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def generate_maze(self):
        # your code goes here
        pass

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
