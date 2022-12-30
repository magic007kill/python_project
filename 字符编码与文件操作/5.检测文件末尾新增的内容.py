# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :5.检测文件末尾新增的内容.py
@Author  :magic007
@Date    : 15:57
'''
with open('历史.txt', mode='rb') as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        # 如果是0个bytes意味着光标在最后
        # 没有关闭这个文件操作
        if len(line) != 0:
            print(line.decode('utf-8'), end='')

