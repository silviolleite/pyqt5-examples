import os
import sys

from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


BASE_DIR = os.getcwd()


class Loop(QThread):
    def run(self):
        for i in range(100000):
            print(f"{i}: Estamos no loop")


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(200, 200)
        self.button = QPushButton("Iniciar loop", self)
        self.setWindowIcon(QIcon(f"{BASE_DIR}/static/logo.png"))
        self.button.clicked.connect(self.start_loop)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def start_loop(self):
        self.thread_loop = Loop()
        self.thread_loop.start()


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Window()
    app.show()
    sys.exit(root.exec_())
