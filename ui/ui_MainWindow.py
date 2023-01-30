# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(854, 658)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.function_selection = QListWidget(Form)
        self.function_selection.setObjectName(u"function_selection")

        self.verticalLayout_2.addWidget(self.function_selection)

        self.set_btn = QPushButton(Form)
        self.set_btn.setObjectName(u"set_btn")

        self.verticalLayout_2.addWidget(self.set_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.stackedWidget = QStackedWidget(Form)
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

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u571f\u8c46\u65e5\u8bb0", None))
        self.set_btn.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

