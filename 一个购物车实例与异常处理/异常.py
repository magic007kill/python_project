# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :异常.py
@Author  :magic007
@Date    : 9:43
'''
'''
1. 异常
    异常是错误发生的信号，一旦程序出错就会产生一个异常，如果该异常
    没有被应用程序处理，那么该异常就会抛出来，程序的执行也随之终结
异常包含三个部分：
    1.异常的追踪信息 —— File "E:\codes\testplay\一个小实例与异常处理\异常.py"
    2.异常的类型    —— NameError
    3.异常的信息    —— name 'a' is not defined
错误分为两大类：
    1.语法上的错误：在程序运行前就应该修正，这个容易避免，有提示
    2.逻辑上的错误：比如：字典没有key，你非要取key，列表没有索引，变量没有名字，这些不容易避免

2.为何要异常处理
    避免程序因为异常而崩溃，所以在应用程序中应该对异常进行处理，从而增强程序的健壮性

3.如何处理异常
try:
    代码1
    代码2
    代码3
    ....
except NameError:
    当抛出的异常是NameError时执行的子代码
except ......:
    pass
else:
    pass
finally:
    pass                  
'''
# 异常处理的单分支
# try:
#     a
# except NameError:
#     print('NameError')，这种是自定义错误信息
# except NameError as e:  # 用这种类型的异常处理好，能把详细信息存在变量e中。
#     # 且同一种异常，处理只能处理一次，谁在最上面先处理异常代码
#     print(e)
# else:
#     print('代码正确')  # 没有异常执行这一段
# finally:
#     # 不管有错没错，都要执行这段语句
#     pass
# print('++++++++++++++++++++')
# 常见异常
# print(1+'a') # TypeError
# print(1+) # SyntaxError
# d = {'x':1,'y':2} # KeyError
# d['z']
# l= [1,2] # IndexError
# l[3]


# 异常处理的多分支
# try:                 # 在处理多分支异常时，哪类异常先触发，则先处理哪类异常，后面的异常不会再报
#     a
#     print('========')
#     print('========')
#     print('========')
#     l = [1, 2]
#     l[3]
# except NameError as e:  # 用这种类型的异常处理好，能把详细信息存在变量e中。
#     # 且同一种异常，处理只能处理一次，谁在最上面先处理异常代码
#     print(e)
# except IndexError as e2:
#     print(e2)
# except (NameError,IndexError,keyword) as e:  # 合并多 异常
#     print(e)
#
# else:
#     print('代码正确')  # 没有异常执行这一段
# finally:
#     # 不管有错没错，都要执行这段语句
#     pass

# 万能捕获  ——没有针对某种异常时，常用万能捕获
# try:
#     # d = {'x': 1, 'y': 2}  # KeyError
#     # d['z']
#     l = [1, 2]
#     l[3]
#
# except Exception as e:
#     print('随便什么异常都可以捕获')
#     print(e)
# else:
#     print('代码正确')  # 没有异常执行这一段
# finally:
#     # 不管有错没错，都要执行这段语句
#     print('已完成了异常捕获')

# 判断文件是否存在，如果没有则创建
# try:
#     f = open('text1.txt')
# except:
#     print('没有找到你的文件')
#     f = open('text1.txt', 'w', encoding='utf-8')
#     f.write('我的新建文件')
# else:
#     print('找到了你的文件')
#     print(f.read())
# finally:
#     f.close()
# 了解
# # 断言
# print('=========111')
# # 自定义异常
# l = [1, 2, 3, 4]
# # if len(l) != 5:
# #     raise TypeError('列表的长度必须为5，这是我定的规则')
# # 直接断言一个异常，终止程序执行
# assert  len(l) == 5
# print('=========222')
