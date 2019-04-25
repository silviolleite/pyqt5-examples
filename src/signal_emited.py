import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QApplication, QFileDialog, QWidget

BASE_DIR = os.getcwd()


class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.w = parent
        self.setMouseTracking(True)

    def mousePressEvent(self, e):
        img, re = QFileDialog.getOpenFileName(self.w, "Selecionar Arquivo",
                                              filter="All(*.png *.jpg)")

        if re:
            self.setPixmap(QPixmap(img).scaled(250, 150, Qt.KeepAspectRatio))

    def mouseMoveEvent(self, e):
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self, e):
        QApplication.setOverrideCursor(Qt.ArrowCursor)


class HandlerWindow(QWidget):
    def __init__(self, parent=None):
        super(HandlerWindow, self).__init__(parent)
        self.resize(300, 350)
        self.label = CustomLabel(self)
        self.setWindowIcon(QIcon(f"{BASE_DIR}/static/logo.png"))
        self.label.setPixmap(QPixmap(f"{BASE_DIR}/static/logo.png").scaled(250, 150, Qt.KeepAspectRatio))


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = HandlerWindow()
    app.show()
    sys.exit(root.exec_())
