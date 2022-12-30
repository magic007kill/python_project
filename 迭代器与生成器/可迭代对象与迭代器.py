# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :可迭代对象与迭代器.py
@Author  :magic007
@Date    : 20:21
'''
'''
1.什么是迭代器
    迭代就是更新换代
    1.1 迭代器指的就是迭代取值的工具
    1.2 迭代是一重复的过程，每一次重复都是基于上一次的结果
2.为何要用迭代器
    迭代器提供了一种通用的且不依赖于索引的迭代取值方式的功能
3.如何用迭代器        
'''
# 单纯的重复不是迭代
# i = 0
# while True:
#     print(i)

# 哪些数据类型需要这样迭代取值
# 字符串 列表 元组 字典 文件等
# l = ['a', 'b', 'c']
# a = 'abc'
# b = ('a', 'b', 'c')
# dic = {'name': '小明', 'age': 10}
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# 可迭代对象
# 每个取值都加了_iter_方法
# a = 1
# a.iter 没有
# b = 1.1
# b.iter没有
# c = 'hello'
# c.__iter__()
# print(c.__iter__())
# d = ['a', 'b']
# d.__iter__()
# print(d.__iter__())
# e = {'x':1}
# e.__iter__()
# print(e.__iter__())
# f = {1,2,3}
# f.__iter__()
# print(f.__iter__())
# g = open('b.txt', 'w')
# # g是迭代器对象，文件类特殊
# # g._iter_()会生成迭代器
# print(g.__iter__())

# 迭代器
# 执行可迭代对象下的_iter_方法，返回值就是一个迭代器对象

# dic = {'x':1, 'y':2, 'z':3}
# # 把迭代器对象变成迭代器
# iter_dic = dic.__iter__()
# print(iter_dic.__next__())
# print(iter_dic.__next__())
# print(iter_dic.__next__())
# # StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(iter_dic.__next__())

# 列表不依赖索引取值
# l =[1, 2, 3]
# iter_l = l.__iter__()
# print(iter_l.__next__(),end=' ')
# print(iter_l.__next__(),end=' ')
# print(iter_l.__next__(),end=' ')

# 误区,下面两个print输出的都是列表的第一个值
#
# 基于老的迭代器对象取值，才能取完整
# iter_l = l.__iter__()
# print(iter_l.__next__(),end=' ')
# print(iter_l.__next__(),end=' ')
# print(iter_l.__next__(),end=' ')

# 可迭代对象与迭代器
# 可迭代对象，只有_iter()_方法，没有__next__（）方法
# 除了文件，其他的容器都是可迭代对象

# 迭代器
# 1.既有内置的next方法的对象，执行迭代器__next__方法可以不依赖索引取值
# 2.又内置__iter__方法的对象，执行迭代器__iter__方法得到的仍然是迭代器本身
# 3.迭代器一定是可迭代的对象，而可迭代的对象却不一定是迭代器对象
# 可迭代对象只需要有__iter()__方法
# 迭代器对象既有__iter()__方法也有__next()__方法
# 文件对象本身就是一个迭代器对象

# l = [1,2,3]
# iter_l = l.__iter__()
# # 调用可迭代的对象__iter__()得到的是迭代器
# # 执行迭代器__iter__方法得到的仍然是迭代器本身,那么有什么用
# # 这样是为了for循环
# print(iter_l.__iter__().__iter__().__iter__())

# dic = {'x':1,'y':2,'z':3}
#
# iter_dic = iter(dic) # 等同于dic.__iter__()
#
# print(iter_dic)
# print(dic.__iter__())
# # 底层 print(dict.__iter__())
# # next与iter一样
# print(next(iter_dic))
# print(iter_dic.__next__())
# 底层 print(dict.__next__())

# 解决迭代器报错

# 异常捕获
# while True:
#     try:
#         print(next(iter_dic))
#     except StopIteration:
#         break
# print('======================')
# # 同一个迭代器只能完整地取完一次值
# while True:
#     try:
#         print(next(iter_dic))
#     except StopIteration:
#         break

# 找一个可迭代对象变成迭代器对象
# 能够自己获取迭代器对象的NEXT的值，且不报错  ————就是for循环
# for本质应该称之为迭代器循环
# 底层工作原理
# 1. 先调用in后面的那个对象的iter方法，将其变成一个迭代器对象
# 2. 调用next(迭代器)，将得到的返回值赋值给变量名
# 3. 循环往复直到next(迭代器)抛出异常，for会自动捕获异常StopIteration然后结束循环

# 可迭代对象包含迭代器对象
# 文件对象是迭代器，那么for循环也会自动调用__iter__，那么还是一个迭代器
# 那么for循环的机制就可以通用，这就是为什么迭代器对象里面也有一个__iter__方法的原因
# dic = {'x':1,'y':2,'z':3}
# for k in dic:
#     print(k)
# # 为什么下一次又可以使用迭代器，因为语句执行完后，有回收了跌代器，下面又执行for循环时
# # 又生成新额dic迭代器
# for k in dic:
#     print(k)

# 迭代器总结
# 优点:
#       1. 提供一种通用的且不依赖于索引的迭代取值方式
#       2. 同一时刻在内存中只存在一个值，更节省内存

# 缺点：
#       1. 取值不如按照索引的方式灵活 ——不能取指定的某一个值，而且只能往后取
#       2. 无法预测迭代器的长度

# 若for....in....'in'后面跟着的是迭代器，则循环从迭代器已迭代到额位置开始；
# 如果后面跟着的可迭代对象，还没有生成迭代器，则重头开始
# 如：
# object = range(1,10)
# iter_object = object.__iter__()
# print(iter_object.__next__())
# print(iter_object.__next__())
# print(iter_object.__next__())
# print('====================')
# for i in iter_object:
#     print(i)
# print('====================')
# for i in object:
#     print(i)













