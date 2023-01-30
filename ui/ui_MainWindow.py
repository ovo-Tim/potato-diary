# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUYWcEK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSplitter,
    QStackedWidget, QTreeView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(854, 658)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.function_selection = QListWidget(self.widget)
        self.function_selection.setObjectName(u"function_selection")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.function_selection.sizePolicy().hasHeightForWidth())
        self.function_selection.setSizePolicy(sizePolicy)
        self.function_selection.setMinimumSize(QSize(0, 5))

        self.verticalLayout.addWidget(self.function_selection)

        self.treeView = QTreeView(self.widget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.treeView)

        self.set_btn = QPushButton(self.widget)
        self.set_btn.setObjectName(u"set_btn")

        self.verticalLayout.addWidget(self.set_btn)

        self.splitter.addWidget(self.widget)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.browse = QWidget()
        self.browse.setObjectName(u"browse")
        self.browse.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.addWidget(self.browse)
        self.new_file = QWidget()
        self.new_file.setObjectName(u"new_file")
        self.stackedWidget.addWidget(self.new_file)
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.stackedWidget.addWidget(self.statistics)
        self.splitter.addWidget(self.stackedWidget)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u571f\u8c46\u65e5\u8bb0", None))
        self.set_btn.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

