#! /usr/bin/env python3
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout)
from PyQt5.QtGui import QIcon
import sys

BASE_DIR = os.getcwd()


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("My Program")
        # self.resize(680, 480)

        # buttom and line edit

        self.button = QPushButton('Show message')
        self.button.clicked.connect(self.exibir)
        self.line_edit = QLineEdit()

        # group box of widgets
        self.groupbox = QGroupBox("Dialog options")

        # options
        self.option_information = QRadioButton("Information")
        self.option_information.setChecked(True)
        self.option_warning = QRadioButton('Warning')
        self.option_critical = QRadioButton('Critical')

        # layout of items of group box
        self.layout_options = QVBoxLayout()
        self.layout_options.addWidget(self.option_information)
        self.layout_options.addWidget(self.option_warning)
        self.layout_options.addWidget(self.option_critical)
        self.groupbox.setLayout(self.layout_options)

        self.layout_first_widgets = QHBoxLayout()
        self.layout_first_widgets.addWidget(self.line_edit)
        self.layout_first_widgets.addWidget(self.button)

        # main layout

        self.layout_master = QVBoxLayout()
        self.layout_master.addLayout(self.layout_first_widgets)
        self.layout_master.addWidget(self.groupbox)

        self.setLayout(self.layout_master)
        self.setWindowIcon(QIcon(f"{BASE_DIR}/static/logo.png"))

    def exibir(self):
        text = self.line_edit.text()
        if self.option_information.isChecked():
            self.messsage_box = QMessageBox.information(self, "Exemplo 1",
                                                        text)
        elif self.option_warning.isChecked():
            self.messsage_box = QMessageBox.warning(self, "Exemplo 1",
                                                    text)
        else:
            self.messsage_box = QMessageBox.critical(self, "Exemplo 1",
                                                     text)

    def closeEvent(self, e):
        e.ignore()
        question_close = QMessageBox.question(self, "Close Slide",
                                              "Do you want to close this window?",
                                              QMessageBox.Yes, QMessageBox.No)
        if question_close == QMessageBox.Yes:
            exit(0)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = Window()
    app.show()
    sys.exit(root.exec_())