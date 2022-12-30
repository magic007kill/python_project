# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :2.文件操作.py
@Author  :magic007
@Date    : 11:31
'''
'''
1. 什么是文件
    文件是操作系统为用户/应用程序提供的一种操作硬盘的抽象单位
2. 为何要用文件
    用户/应用程序对文件的读写操作会由操作系统转换成具体的硬盘操作
    所以用户/应用程序可以通过简单的读/写文件来间接地控制复杂地硬盘地读取操作
    实现将内存中地数据永久保存到硬盘中
    user=input('>>>>:') #user='大海'
3. 如何用文件
    文件操作地基本步骤：
        f=open(...) #打开文件，拿到一个文件对象f,f就相当于一个遥控器，可以向操作系统发送指令
        f.read() # 读写文件，向操作系统发送读写文件指令
        f.close() # 关闭文件，回收操作系统的资源
    上下文管理：
        with open(...) as f:
            pass            
'''
# 绝对路径
# f = open(r'/E:\codes\testplay\a.txt', encoding='utf-8')
# print(f.read())
# f.close()
# 相对路径
# 读取当前文件
# f = open(r'a.txt', encoding='utf-8') # 因为在当前目录下，也可以写为f = open('a.txt', encoding='utf-8')
# ../相对路径
# f = open(r'bbb\ccc\a.txt', encoding='utf-8')  # 因为在其他子目录下，所以必须要用r'去读取元素字符串，而不会被转义
# print(f.read())
# 打开后，一定在程序执行完后关闭打开的文件
# f.close()
# 若未关闭，则下式无法读取，因为f.read()只能被执行一次
# print(f.read())

# 上下文管理,常用with open() as f:这种方式读取文件
with open(r'a.txt', encoding='utf-8') as f:
    print(f.read())

