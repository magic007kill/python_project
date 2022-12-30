# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :装饰器.py
@Author  :magic007
@Date    : 16:50
'''
# 装饰器就是一个特殊的闭包函数
# 只不过这个函数不是给自己使用的，是给其他函数添加功能的
# 装饰器指的就是为被装饰的对函数对象添加额外功能
# 2.为什么要使用装饰器
#   软件的维护应该遵循开放封闭的原则：
#      软件一旦上线运行后对修改源代码是封闭的，对扩展功能是开放的
#    装饰器要遵循两大原则：
#       1.不修改修饰对象的源代码(如：人原来的性格，生活方式)
#       2.不修改被装饰对象的调用方式（如：人的原来外貌，名字）
# def run():
#     print('跑步')
#     print('健身')   改变了原来的代码
# run()

# def fitness():
#     print('健身')
#     run()  改变了原来调用的方式
# def run():
#      print('跑步')

# 装饰器
# name = '大海'
#
#
# def run(func_name):
#     print('=======')
#     print('%s' % func_name)
#     print('=======')
#
#
# # run(name)
# def decorate(func):  # func传入run
#     def new_func(new_name):  # run(name)的name
#         print('我是装饰器前面的代码')
#         func(new_name)
#         print('我是装饰器后面的代码')
#
#     return new_func
#
#
# # 1.定义了一个new_func(name)函数 2. 返回了new_func内存地址 3.传入了一个run函数名
# run = a = decorate(run)
# # print(a)
# run(name)

# 测试for循环从1加到9000000的时间
n = 9000000

# def for1(n):
#     sum1 = 0
#     for i in range(1, n + 1):
#         sum1 += i
#     print(sum1)

# for1(n)
# 导入可以拿到当前的时间的模块
from datetime import datetime


def run_time(func):  # func 是for1 这是一个用来计算程序执行时间的装饰器
    def new_for1(*args, **kwargs):
        start_time = datetime.now()
        print('开始时间%s' % start_time)
        func(*args  , **kwargs)
        stop_time = datetime.now()
        print('结束时间%s' % stop_time)
        runtime = stop_time - start_time
        print(runtime)

    return new_for1


@run_time  # for1 = decorate(for1) # 1.定义了new_for1(n)函数 2.返回了new_for1的内存地址 3. 传入了一个for1的函数名
def for1(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i
    print(sum1)


@run_time
def test_print():
    print('打印指令的耗时')


for1(n)
test_print()
