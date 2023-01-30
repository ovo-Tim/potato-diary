#!/usr/bin/python3
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

import ui_MainWindow
import browse

from qt_material import apply_stylesheet

if __name__ == "__main__":
    DIR = "."
else:
    DIR = "./ui"

class MainWindow(QWidget,ui_MainWindow.Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 设置function_selection
        with open(DIR + "/qss/QListWidget.qss") as QListWidget_qss:
            self.function_selection.setStyleSheet(QListWidget_qss.read())
        self.function_selection.addItem("浏览")
        self.function_selection.addItem("新建")
        self.function_selection.addItem("统计")

        # 测试翻页
        # l1=QHBoxLayout()
        # l2=QHBoxLayout()
        # label1 = QLabel()
        # label1.setText("Page1")
        # label2 = QLabel()
        # label2.setText("Page2")
        # l1.addWidget(label1)
        # l2.addWidget(label2)
        # self.page.setLayout(l1)
        # self.page_2.setLayout(l2)

        self.browse_layout = QGridLayout()
        self.browse_layout.addWidget(browse.browse())
        self.browse.setLayout(self.browse_layout)

        self.function_selection.currentRowChanged.connect(self.set_page)
    def set_page(self,i):
        self.stackedWidget.setCurrentIndex(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec())