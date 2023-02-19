#!/usr/bin/python3
import TinyMCE_on_Pyqt

import sys,os

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
        self.tiny.browser.page().loadFinished.connect(self.open_file)
        self.save_btn = QPushButton("保存")

        self.mainLayout.addWidget(self.tags_bar)
        self.mainLayout.addWidget(self.tiny)
        self.mainLayout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save)

        self.tag = tags.tags()

        self.setLayout(self.mainLayout)


        for k,v in self.tag.data["tags-article"].items():
            if file_path in v:
                self.tags_bar.tags.append(k)
        self.tags_bar.refresh()

        # self.open_file()


        

    def open_file(self):
        with open(os.path.abspath(os.path.normpath(self.file_path)), mode='r', encoding='utf-8') as f:
            f.seek(0)
            self.tiny.set_html(str(f.read()))
            print(self.tiny.get_file())

    def save(self):
        self.tiny.save_file(self.file_path)
        for i in self.tags_bar.tags:
            self.tag.add_article(i, self.file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=editor("")
    window.show()
    sys.exit(app.exec())