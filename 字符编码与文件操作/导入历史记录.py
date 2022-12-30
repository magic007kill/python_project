# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :导入历史记录.py
@Author  :magic007
@Date    : 16:21
'''
import time

# at
with open('历史.txt', mode='at', encoding='utf-8') as f:

    f.write('%s 小明转账给小王1个亿\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
