# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :6.修改文件的方式.py
@Author  :magic007
@Date    : 16:50
'''
# 修改文件的方式一：
# 1 将文件内容由硬盘全部读入内存
# 2 在内存中完成修改
# 3 将内存中修改后的结果覆盖写回硬盘
# 优点：在文件修改过程中硬盘上始终一份数据
# 缺点： 占用内存过多，不适用于大文件

# with open('文件修改.txt', mode='rt', encoding='utf-8') as f:
#     all_data = f.read()
#     print(all_data, type(all_data))
# with open('文件修改.txt', mode='wt', encoding='utf-8') as f1:
#     f1.write(all_data.replace('a', '毛主席'))

# 修改文件的方式二：
# 1. 以读的方式打开源文件，以写的方式打开一个临时文件
# 2. 从源文件中每读一样内容修改完毕后写入临时文件，直到源文件读取完毕
# 3. 删除源文件，将临时文件重命名为源文件名
# 优点：在同一时刻内存中只存在源文件的一行内容，不会过多地占用内存
# 缺点：在文件修改地过程中会出现源文件与临时文件共存，硬盘上同一时刻
# 会有两份数据，即在修改佛如过程中会过多地占用硬盘

import os

with open('文件修改2.txt', mode='rt', encoding='utf-8') as read_f, \
        open('临时文件.txt', mode='wt', encoding='utf-8') as wite_f:
    for line in read_f:
        wite_f.write(line.replace('小明', '小王'))

# 文件修改2删除
os.remove('文件修改2.txt')
# 临时文件.txt 改成 文件修改2.txt
os.rename('临时文件.txt', '文件修改2.txt')



