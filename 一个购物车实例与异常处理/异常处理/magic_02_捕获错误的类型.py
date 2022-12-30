try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用8除以用户输入的整数并输出
    result = 8/num

    print(result)
except ValueError:
    print("输入值不是整数")
except ZeroDivisionError:
    print("除零错误")

