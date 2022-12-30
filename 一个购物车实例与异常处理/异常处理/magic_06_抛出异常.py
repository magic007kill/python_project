def input_password():
    # 1.提示用户输入密码
    pwd = input("输入密码：")
    # 2.判断密码长度>=8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.如果<8主动抛出异常
    print("抛出异常")
    # 1>创建异常对象,可以使用错误字符串作为参数
    ex = Exception("密码长度不够")
    # 2>主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)

