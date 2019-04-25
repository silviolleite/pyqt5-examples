import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton, QSystemTrayIcon,
                             QFileDialog, QFormLayout, QApplication, QMessageBox)
from PyQt5.QtCore import QThread, QRegExp
import requests
import sys

BASE_DIR = os.getcwd()


class DownloaderMusic(QThread):
    def __init__(self, name, url, path):
        super(DownloaderMusic, self).__init__()
        self.path = path
        self.url = url
        self.name = name

    def run(self):
        mescl = self.path+"/"+self.name
        with open(mescl+'.mp3', 'wb') as f:
            f.write(requests.get(self.url).content)


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.path = None
        self.settings()
        self.create_widgets()
        self.create_layout()

    def settings(self):
        self.resize(300, 120)
        self.setWindowTitle("Mp3 Downloader")
        self.setWindowIcon(QIcon(f"{BASE_DIR}/static/logo.png"))

    def create_widgets(self):
        self.edit_url = QLineEdit()
        self.edit_name = QLineEdit()
        self.btn_select_path = QPushButton("Select path", self)
        self.btn_select_path.clicked.connect(self.select_path)
        self.btn_down = QPushButton("Download mp3", self)
        self.btn_down.clicked.connect(self.download)

    def create_layout(self):
        self.layout = QFormLayout()
        self.layout.addRow("Nome:", self.edit_name)
        self.layout.addRow("Url:", self.edit_url)
        self.layout.addRow("Selecionar destino:", self.btn_select_path)
        self.layout.addRow(self.btn_down)
        self.setLayout(self.layout)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")

    def download(self):
        if self.verify_fields():
            self.manage_interface(False)
            self.thread_qt()

    def verify_fields(self):
        if self.path is None:
            return False
        else:
            strings = [self.edit_url.text(), self.edit_name.text(), self.path]
            regex_validate = QRegExp("*.mp3")
            regex_validate.setPatternSyntax(QRegExp.Wildcard)
            emptys = 0
            for string in strings:
                if len(string.split()) == 0:
                    emptys += 1
            if emptys == 0 and regex_validate.exactMatch(self.edit_url.text()):
                return True

    def thread_qt(self):
        url = self.edit_url.text()
        name = self.edit_name.text()
        path = self.path
        self.thre = DownloaderMusic(name, url, path)
        self.thre.finished.connect(self.downfin)
        self.thre.start()

    def manage_interface(self, state):
        self.btn_down.setEnabled(state)
        self.edit_name.setEnabled(state)
        self.edit_url.setEnabled(state)
        self.btn_select_path.setEnabled(state)

    def downfin(self):
        text = """Download Finalizado O download da sua música foi realizado com sucesso."""
        QMessageBox.information(self, "Exemplo 1",
                                text)
        self.manage_interface(True)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Main()
    app.show()
    sys.exit(root.exec_())