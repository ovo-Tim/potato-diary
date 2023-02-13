#!/usr/bin/python3
import os
import sys

if __name__ == "__main__":
    DIR = "."
    sys.path.append("../")
else:
    DIR = "./ui"

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

import ui_browse
import edit

from tags import tags

class browse(QWidget,ui_browse.Ui_Form):
	def __init__(self):
		super(browse, self).__init__()
		self.setupUi(self)

		self.tags = tags()

		self.comboBox.addItems(self.tags.data["tags"])
		self.comboBox.currentIndexChanged.connect(self.change_list)
		self.change_list()


	def change_list(self):
		self.listWidget_2.clear()
		if self.comboBox.currentText() != "":
			self.listWidget_2.addItems(self.tags.data["tags-article"][os.path.normpath(self.comboBox.currentText())])