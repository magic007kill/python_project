# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :匿名函数.py
@Author  :magic007
@Date    : 13:56
'''
'''
1. 匿名函数：就是没有名字的函数

2. 为何要用：用于仅仅临时使用一次的场景，没有重复使用的需求

'''

# 有名函数
# def sum1(x, y):
#     print(x, y)
#     return x + y
#
#
# print(sum1(1, 2))

# 匿名函数，除了没有名字其他都有
# 语法 lambda空格+参数+冒号+函数代码（表达式或者函数）
# 用一行代码图省事
# 匿名函数的定义

# print(lambda x, y: x + y)
# # 调用直接内存地址加括号（它虽然没有名字）+括号可以调用
# #表达式
# print((lambda x, y: x + y)(1, 2))
# #函数
# print((lambda x, y:print( x + y))(1, 2))
# # 把内存地址赋值给一个变量没有意义
# # 匿名函数的精髓就是没有名字，为其绑定名字没有意义
# f = lambda x, y: x + y
# print(f(1, 2))
# 匿名函数与内置函数结合使用
# max,min,sorted
salaries = {
    '小明': 30000,
    '小王': 10000,
    '小五': 3000
}
# 求薪资最高的那个人名：比较的时候value,但是结果是key
# 默认比较key值
# print(max(salaries))


# max(字典，key=函数名)
def func(name):
    return salaries[name]
print(max(salaries, key=func))
# 在外部不要使用func()
# 求最大值即比较的是value，但取的是key人名
# print(max(salaries,key=lambda name:salaries[name]))

# 求最小值
# print(min(salaries,key=lambda name:salaries[name]))

# sorted排序
# nums = [11,23,45,232,2]
# res = sorted(nums,reverse=True) # reverse=True为倒序，=False为正序
# print(res)
# 循环遍历薪资
# for v in salaries.values():
#     print(v)
#
# print(sorted(salaries.values()))
# 但是我们要比较薪资，返回人名
# 薪资反序
print(sorted(salaries, key=lambda name: salaries[name], reverse=True))
# 薪资正序
print(sorted(salaries, key=lambda name: salaries[name], reverse=False))