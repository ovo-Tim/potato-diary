#!/usr/bin/python3
import os
import sys

sys.path.append('./ui')

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qt_material import apply_stylesheet

from ui.MainWindow import MainWindow



app = QApplication(sys.argv)
window=MainWindow()
apply_stylesheet(app, theme='dark_teal.xml')
window.show()
sys.exit(app.exec())