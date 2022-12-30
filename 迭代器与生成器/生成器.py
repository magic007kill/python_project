# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :生成器.py
@Author  :magic007
@Date    : 18:55
'''
# 大前提：生成器就是一种自定义的迭代器，本质就是迭代器
# 但凡函数内包含yield关键字，调用函数不会执行函数体代码
# 会得到一个返回值，该返回值就是生成器对象
#
# def func():
#     print('======1')
#     yield 1
#     print('======2')
#     yield 2
#     print('======3')
#     yield 3
#
#
# g = func()
# print(g)
# print(g is g.__iter__())
# # g.__next__()
# res1 = next(g)
# # 会触发函数执行，直到碰到一个yield停下来，
# # 并且将yield后的值当做本次next的结果返回
# print(res1)
# res2 = next(g)
# print(res2)
# res3 = next(g)
# print(res3)
#
# print('=====================')
# # 生成器一般与for循环连用
# for i in g:
#     print(i)

# 总结yield：只能在函数内使用
# 1. yield提供了一种自定义迭代器的解决方案
# 2. yield可以保存函数的暂停状态
# 3. yield对比return
#         ① 相同点：都可以返回值，值得类型和个数没有限制
#         ② 不同点：yield可以返回多次值，而return只能返回一次值，函数就结束了

'''
定义一个生成器，这个生成器可以生成10位斐波拉契数列
数列中每个值等于前两个数的和，前两个数是1,1 —— 如：[1,1,2,3,5,8.......]
'''


# def run(n):
# # 参数说明：
# # n是数列的个数
# # i是计算循环，a是第一个数，b是第二个数
#     i, a, b = [0, 1, 1]
#     while i < n:
#         yield a  # 每次都返回一个数
#         a, b = b ,a +b
#         i += 1
#
# my_run = run(10)
# print(my_run)
# for i in my_run:
#     print(i)
def js(n):
    i = 1
    a = 1
    sum = 1
    while i <= n:
        yield sum
        i += 1
        a = a * i
        sum = a + sum


my_js = js(4)
print(list(my_js))
for i in my_js:
    print(my_js)  # 上句已经通过list函数去完，for循环无法取出值
                  # 迭代器只能取一次，而可迭代对象可以反复取
