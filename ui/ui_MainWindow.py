# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUoEbCA.ui'
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
    QListWidgetItem, QSizePolicy, QSplitter, QStackedWidget,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(854, 658)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.function_selection = QListWidget(self.splitter)
        self.function_selection.setObjectName(u"function_selection")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.function_selection.sizePolicy().hasHeightForWidth())
        self.function_selection.setSizePolicy(sizePolicy)
        self.function_selection.setMinimumSize(QSize(0, 5))
        self.splitter.addWidget(self.function_selection)
        self.treeWidget = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.treeWidget)
        self.splitter_2.addWidget(self.splitter)
        self.stackedWidget = QStackedWidget(self.splitter_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setSizeIncrement(QSize(0, 0))
        self.stackedWidget.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.browse = QWidget()
        self.browse.setObjectName(u"browse")
        self.browse.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.addWidget(self.browse)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.stackedWidget.addWidget(self.edit)
        self.splitter_2.addWidget(self.stackedWidget)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u571f\u8c46\u65e5\u8bb0", None))
    # retranslateUi

