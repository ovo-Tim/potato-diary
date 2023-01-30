#!/usr/bin/python3
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

import ui_browse


class browse(QWidget,ui_browse.Ui_Form):
	def __init__(self):
		super(browse, self).__init__()
		self.setupUi(self)