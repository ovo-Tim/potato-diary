#!/usr/bin/python3
import TinyMCE_on_Pyqt

import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

import tagsBar
import tags

import threading
import time

class editor(QWidget):
    def __init__(self,file_path):
        super().__init__()
        self.file_path=file_path
        self.mainLayout = QVBoxLayout()
        self.tags_bar = tagsBar.TagBar()
        self.tiny = TinyMCE_on_Pyqt.TinyMCE_on_PyQt_window()
        self.tiny.init()
        self.save_btn = QPushButton("保存")

        self.mainLayout.addWidget(self.tags_bar)
        self.mainLayout.addWidget(self.tiny)
        self.mainLayout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save)

        self.tag = tags.tags()

        self.setLayout(self.mainLayout)

        threading.Thread(target=self.open_file).start()

        

    def open_file(self):
        time.sleep(5)
        with open(self.file_path) as f:
            self.tiny.set_html(f.read())

    def save(self):
        self.tiny.save_file(self.file_path)
        for i in self.tags_bar.tags:
            self.tag.add_article(i, self.file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=editor("")
    window.show()
    sys.exit(app.exec())