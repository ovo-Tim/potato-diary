#!/usr/bin/python3
import os

input("警告：将清理所有数据，仅供调试！按回车继续")

with open("./data/tags.json","w") as file:
    file.write('''{"tags": [], "tags-article": {}}''')

try:
    os.removedirs("./data/article/")
except:
    print("删除文章文件夹失败")