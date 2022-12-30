# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :3.文件操作的常用模式.py
@Author  :magic007
@Date    : 0:23
'''
'''
一 文件的打开模式
    r:只读模式（默认）
    w:只写模式
    a:只追加模式

二 控制读写文件单位的方法（必须与r\w\a连用）  
    t:文本模式(默认)，一定要指定encoding然后返回 
    优点：操作系统会将硬盘中二进制数字解码成unicode然后返回
    强调：只针对文本文件有效
    
    b:二进制模式，一定不能指定encoding参数
    优点： 
'''
# 一 rt: 只读模式（默认）

# 当文件不存在时，会报错
# 当文件存在时，文件指针指向文件的开头

# with open(r'a.txt', encoding='utf-8') as f:
    # res1 = f.read()
    # print('1>>',res1)
    # # 第一次读完了，第二次不能读到
    # res2 = f.read()
    # print('2>>', res2)
    # 判断rt模块是否可读
    # print(f.readable())
    # 判断rt模块是否可写
    # print(f.writable())
    # # 行读取
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # # 不按行输出，用列输出内容
    # L = []
    # for line in f:
    #     L.append(line)
    # print(L)
    # 用一行代码搞定
    # print(f.readlines())

# 二 wt: 只读模式
# 1. 当文件不存在时，新建一个空白文档
# with open('b.txt', mode='wt', encoding='utf-8') as f:
#     pass
# 2. 当文件存在，且由内容时，则清空原有文档，文件指针回到文件的开头
# with open('b.txt', mode='wt', encoding='utf-8') as f:
    # 清空全部
    # 下面写自己的内容
    # 写在一行
    # f.write('小明')
    # f.write('小王')
    # f.write('小美')
    # 写成三行
    # f.write('小明\n')
    # f.write('小王\n')
    # f.write('小美\n')
    # 一次性写多行
    # f.write('小明\n小王\n小美\n')
    # 把列表内容一行行写入
    # info = ['小明\n', '小王\n', '小美\n']
    # for line in info:
    #     f.write(line)
    # # 一行代码搞定
    # f.writelines(info)

# 三 at: 只追加模式
# 1.当文件不存在时，新建一个空文档，文件指针指到文件的末尾（开头）
# with open('c.txt', mode='at', encoding='utf-8') as f:
#     pass
# 2.文件存在的时候
# with open('c.txt', mode='at', encoding='utf-8') as f:
#     # 不能读
#     print(f.readable())
#     # 能写
#     print(f.writable())
#     f.write('我是嘻嘻嘻')

# w模式和a模式的区别
# wt模式在文件打开不关闭的情况下，连续写入
# a模式关闭了下次打开再写，是再文件末尾写，不会覆盖原来的内容

# t模式只能队文本文件进行操作，有局限性


# 二进制文件b模式
# with open(r'图片\m4.png', mode='rb') as f:
#     data = f.read()
#     print(type(data))
# 复制图片
# with open('1.png', mode='wb') as f1:
#     f1.write(data)

# 用b模式，也可以对文本文件操作，但是要解码
# decode 二进制解码成字符
# encode 字符编码成二进制
# 解码 读的时候转换成字符
# with open('b模式.txt', mode='rb') as f:
#     data=f.read()
#     print(data)
#     print(data.decode('utf-8'))
# 编码 写的时候把字符转换成二进制写入
# with open('wb模式.txt', mode='wb') as f:
#     f.write('毛泽东\n'.encode('utf-8'))

# 可读可写 r+t模式：
# 当文件不存在时，会报错
# 当文件存在时，文件指针指向文件的开头
with open('可读可写r+t模式.txt', mode='r+t', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    print(f.readline())
    print(f.readline())
    f.write('magic')

# 可读可写 w+t模式
# 1. 当文件不存在时，新建一个空白文档
# with open('b.txt', mode='wt', encoding='utf-8') as f:
#     pass
# 2. 当文件存在，且由内容时，则清空原有文档，文件指针回到文件的开头
# with open('可读可写w+t模式.txt', mode='w+t', encoding='utf-8') as f:
#     print(f.readable())
#     print(f.writable())
#     f.write('熊婉依小乖乖\n')
#     f.write('熊婉依小依依\n')
#     # 指针移动 seek(移动的字节数，开头开始0)
#     # 从头开始移动0
#     f.seek(9,0)
#     print(f.readline())
#     f.write('熊亦贤')

# a+t模式 不会覆盖原文件
with open('可读可写a+t模式.txt', mode='a+t', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('熊婉依小乖乖\n')
    f.write('熊婉依小依依\n')
    # 指针移动 seek(移动的字节数，开头开始0)
    # 从头开始移动0
    f.seek(9,0)
    print(f.readline())
    f.write('熊亦贤\n')
# 视频和图片用不上
# r+b w+b a+b 和r+t w+t a+t 规律一样




