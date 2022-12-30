# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :如何避免乱码.py
@Author  :magic007
@Date    : 22:03
'''
# 天生我材必有用

# 日语
with open('text1.txt', mode='w', encoding='shift_jis') as f1:
    f1.write('あもーがざいひつよーよー')
# 可以正常读
with open('text1.txt', mode='r', encoding='shift_jis') as f1:
    print(f1.read())
# 乱码
with open('text1.txt', mode='r', encoding='GBK') as f1:
    print(f1.read())
# 报错
# with open('text1.txt', mode='r', encoding='utf-8') as f1:
    print(f1.read())

print('===============')
# 英文
with open('text2.txt', mode='w', encoding='GBK') as f2:
    f2.write('I belive')

with open('text2.txt', mode='r', encoding='utf-8') as f2:
    print(f2.read())

print('===============')
with open('text2.txt', mode='w', encoding='shift_jis') as f2:
    f2.write('I belive')

with open('text2.txt', mode='r', encoding='utf-8') as f2:
    print(f2.read())

print('===============')
with open('text2.txt', mode='w', encoding='ASCII') as f2:
    f2.write('I belive')

with open('text2.txt', mode='r', encoding='utf-8') as f2:
    print(f2.read())

#  总结：
# 1.保证不乱码的核心法则就是字符按照什么标准编码的
#   就要按照什么标准解码，此处的标准指的就是字符编码
# 2.在内存中写的所有字符，一视同仁，都是unicode
#   比如我们打开编辑器，输入一个’你‘，我们并不能说’你‘就是一个汉字，此时它仅仅是个符号
#   只有在我们往硬盘保存或者基于网络传输时，才能确定’你‘到底是一个汉字，还是一个日本字，这就是unicode转换成其他编码格式的过程
