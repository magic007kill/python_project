# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :4.指针移动.py
@Author  :magic007
@Date    : 14:49
'''
# f.seek
# 文件内指针移动，只有t模式下的read(n),n代表的字符的个数
# b模式文件内指针的移动都是以字节为单位
# with open('指针移动.txt', mode='rt', encoding='utf-8') as f:
#     print(f.read(1))
#     print(f.read(1))
#     print(f.read(1))

# with open('指针移动.txt', mode='rb') as f:
#    # 读取一个字节，英文没问题
#    print(f.read(1).decode())
#    # 只读到了1个字节，而每个汉字有三个字节存储，所以下属报错
#    print(f.read(1).decode())

# 指针操作
# f.seek(offset,whence)两个参数：
# offset: 代表控制指针移动的字节数
# ————注意中英文混杂时，字节的位置英文占一个字节，汉字占3个字节
# whence: 代表参照什么位置进行移动
# whence = 0: 参照文件开头（默认的），可以在t和b模式下使用
# whence = 1: 参照当前所在的位置，必须在b模式下用
# whence = 2: 参照文件末尾，必须在b模式下用
# t模式下操作
# with open('seek.txt', mode='rt', encoding='utf-8') as f:
#     f.seek(4, 0)
#     print(f.read(3))

# b模式下操作
# with open('seek.txt', mode='rb') as f:
#     f.seek(0, 0)
#     print(f.read(10).decode('utf-8'))

# whence = 1
with open('seek.txt', mode='rb') as f:
    msg = f.read(4)
    # 显示当前的光标所在的字节数
    print(f.tell())
    f.seek(3, 1)
    print(f.read(15).decode('utf-8'))

# whence = 2
with open('seek.txt', mode='rb') as f:
    msg = f.read(4)
    # 显示当前的光标所在的字节数
    f.seek(-3, 2)
    print(f.tell())
    print(f.read(15).decode('utf-8'))

