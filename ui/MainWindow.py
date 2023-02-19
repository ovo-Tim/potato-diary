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

import ui_MainWindow
import browse
import edit

from qt_material import apply_stylesheet

import tags
import shutil



def get_parents(parents_list):
    if parents_list[0].parent() != None:
        parents_list.insert(0,parents_list[0].parent())
        return get_parents(parents_list)
    else:
        return parents_list


class MainWindow(QWidget,ui_MainWindow.Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 设置function_selection
        with open(DIR + "/qss/QListWidget.qss") as QListWidget_qss:
            self.function_selection.setStyleSheet(QListWidget_qss.read())
        self.function_selection.addItem("浏览")
        self.function_selection.addItem("统计")
        self.function_selection.setMinimumHeight(18)

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
        self.browse_cla = browse.browse()
        self.browse_layout.addWidget(self.browse_cla)
        self.browse.setLayout(self.browse_layout)

        self.function_selection.currentRowChanged.connect(self.set_page)

        self.article_path = "./data/article"
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0,"article")
        self.CreateTree(os.listdir(self.article_path), root, self.article_path)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.tree_menu)

        self.browse_cla.listWidget_2.itemClicked.connect(lambda: self.openfile(self.browse_cla.listWidget_2.selectedItems()[0].text()))

    def openfile(self ,article):
        self.edit_page = edit.editor(article)
        self.edit_layout = QGridLayout()
        self.edit_layout.addWidget(self.edit_page)
        self.edit.setLayout(self.edit_layout)
        self.stackedWidget.setCurrentIndex(2)
        

    def tree_menu(self,pos):
        self.Selected_item = self.treeWidget.currentItem()
        item1 = self.treeWidget.itemAt(pos)

        if self.Selected_item!=None and item1!=None:
            if self.Selected_item.text(0)[-5:] == ".html": #判断是不是文件夹
                Menu = QMenu()
                Menu.addAction(QAction(u'删除', self))
                Menu.addAction(QAction(u'打开', self))
                Menu.triggered[QAction].connect(self.file_func)
                Menu.exec_(QCursor.pos())
            else:
                Menu = QMenu()
                Menu.addAction(QAction(u'新建', self))
                Menu.addAction(QAction(u'新建文件夹', self))
                Menu.addAction(QAction(u'删除', self))
                Menu.triggered[QAction].connect(self.file_func)
                Menu.exec_(QCursor.pos())

    def file_func(self,q):
        if q.text() == "新建文件夹":
            # print(get_parents([self.Selected_item]))
            path = "./data/"
            for i in get_parents([self.Selected_item]):
                path += i.text(0)
                path += "/"
            folder_name = QInputDialog.getText(self, "新建文件夹", "输入文件名")
            os.makedirs(path+folder_name[0])
            # print(path)
        elif q.text() == "删除":
            path = "./data/"
            for i in get_parents([self.Selected_item]):
                path += "/"
                path += i.text(0)
                
            try:
                shutil.rmtree(path)
            except:
                os.unlink(path)
        elif q.text() == "新建":
            path = "./data/"
            for i in get_parents([self.Selected_item]):
                path += "/"
                path += i.text(0)
            file_name = QInputDialog.getText(self, "新建文件", "输入文件名")[0]
            with open(path+"/"+file_name,'w') as f:
                f.write("")
            path = path+"/"+file_name
            self.openfile(path)
        elif q.text() == "打开":
            path = "./data/"
            for i in get_parents([self.Selected_item]):
                path += "/"
                path += i.text(0)
            self.openfile(path)


        # 完成后刷新
        self.treeWidget.clear()
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0,"article")
        self.CreateTree(os.listdir(self.article_path), root, self.article_path)
    
    def set_page(self,i):
        self.stackedWidget.setCurrentIndex(i)

    def CreateTree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '/' + i
            if os.path.isdir(path_new):
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0,i)
                child.setIcon(0,QIcon(icon))
                dirs_new = os.listdir(path_new)
                self.CreateTree(dirs_new, child, path_new)
            else:
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0,i)
                child.setIcon(0,QIcon(icon))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec())