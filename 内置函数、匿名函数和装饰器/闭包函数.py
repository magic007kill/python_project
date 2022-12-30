# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :testplay
@File    :闭包函数.py
@Author  :magic007
@Date    : 16:12
'''


# 闭包函数
# 闭包指的是该函数是一个内部函数
# 包指的是该内部的函数名字在外部被引用


def outer():
    # 1.只检测函数体outer的语法，不执行函数体代码
    print('外函数正在运行')

    def inner():
        print('里面的函数正在运行')

    return inner  # 3.返回inner的内存地址


inner = outer()  # 2.定义了inner函数
# 4.inner函数可以读取原outer函数的命令，加inner加装的命令
inner()


# 为函数体传值的方式一：参数
def func(x, y):
    print(x + y)


func(1, 2)


# 为函数体传值的方式二：闭包
def outer(x, y):
    def func():
        print(x + y)

    return func


print('=====')
func = outer(1, 2)  # 接收的是def func()的地址
func()  # 执行def func()函数
print('=====')
# 给第二个值
# 之后调用func2()可以
func2 = outer(2, 2)
func2()
