# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :内置函数介绍.py
@Author  :magic007
@Date    : 12:48
'''

print(all([]))

# ASCII代码转换函数
print(ord('a'))
print(chr(85))

# 拉链函数 zip
t1 = [1, 2, 3, 4, 5] # 5没有配对，将被抛弃
t2 = ['a', 'b', 'c', 'd']

print(list(zip(t1, t2)))
# 下面常用--转化为字典
print(dict(zip(t1, t2)))

# 介绍 exec函数，可以执行字符串里的代码
# 支持python语法
exec ('print("1")')

exec('''for i in range(0,10):
            print(i)
    ''')



