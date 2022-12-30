# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :购物车.py
@Author  :magic007
@Date    : 22:30
'''
# 业务逻辑
# 购物车
# 个人信息
# 字典
# 导入time模块
import time

user_dic = {
    'name': '小明',
    'password': '123',
    'locked': False,
    'account': 50000,
    'shopping_cart': {}
}


# 登录
def login():
    '''
    登录函数，密码输入错误3次锁定5秒，用户名输入错误可以一直输入
    :return:
    '''
    print('请登录')
    count = 0  # 初始化count
    while True:
        # 'locked':False,初始为非锁定
        if user_dic['locked']:
            print('你已经输入错误3次,系统锁定5秒，请等待5秒后再登录')
            time.sleep(5)
            user_dic['locked'] = False
            count = 0
        name = input('请输入用户名：').strip()  # 去掉空格的输入
        if name == user_dic['name']:
            pwd = input('请输入密码：')
            if user_dic['password'] == pwd and user_dic['locked'] == False:
                print('登录成功')
                break
            else:
                print('密码错误')
                count += 1
        else:
            print('用户名不存在')
        if count >= 3:
            user_dic['locked'] = True


# login()
def login_inter(func):
    # shopping
    def wrapper():
        login()
        func()

    return wrapper


# 先登录再购物
@login_inter # 等同于shopping = login_inter(shopping)
def shopping():
    print('购物')
    goods_list = [
        ['coffee', 30],
        ['chicken', 20],
        ['iphone', 10000],
        ['car', 100000],
        ['house', 200000]
    ]
    account_old = user_dic['account']
    shopping_cart = {}
    cost_money = 0
    total_price = 0
    while True:
        # print(goods_list)
        # enumerate 枚举
        for i, item in enumerate(goods_list):
            print(i, item)
            # i就是列表的索引
            # item就是列表的元素

        # 输入时候 输入名字
        # 输入商品对应得编号
        choice = input('输入产品对应的编号,结账请按“t”：').strip()
        # input输入的是数字吗，字符串的数字
        if choice.isdigit():
            # 判断字符串是否是数字
            # 进入了这个里面，字符串的数字
            choice = int(choice)
            if choice < 0 or choice >= len(goods_list):
                # 判断数字对应列表的索引没在索引范围内
                print('请选择正确的序号')
                continue
            goods_name = goods_list[choice][0]
            goods_price = goods_list[choice][1]
            print('你选的商品：%s' % goods_name)
            print('你选的商品价格：%d' % goods_price)
            if user_dic['account'] >= goods_price:
                # 用户账上的钱要大于商品的价格
                # 提示用户这次新加入的商品
                print('新的购物商品：%s ' % goods_name)
                # 判断所选商品是否存在于购物车中，若有则该商品数量加1
                if goods_name in shopping_cart:
                    shopping_cart[goods_name]['count'] += 1
                    user_dic['account'] = user_dic['account'] - goods_price
                else:
                    shopping_cart[goods_name] = {'price': goods_price, 'count': 1}
                    user_dic['account'] = user_dic['account'] - goods_price
            else:
                print('你的余额：%d,不足以支付%s:%d，请重新选择' % (
                    user_dic['account'], goods_list[choice][0], goods_list[choice][1]))
                continue


            # # 账户金额
            # user_dic['account'] -= goods_price
            # # 花费的金额
            # cost_money += goods_price
            # 花费的总金额
            for dit in shopping_cart:
                # 展示购物车商品
                print('商品名:%s\t  单价:%d\t  数量:%d\t\n=====================================' %
                      (dit, shopping_cart[dit]['price'], shopping_cart[dit]['count']))
                total_price = total_price + shopping_cart[dit]['price']
            print("已花费:%d" % total_price)
        elif choice == 't':
            rechoose = True
            while rechoose:
                pay = input('请确定是否支付（Y/N):').strip()
                if pay == 'Y':
                    if total_price == 0:
                        print('你什么也没买！')
                    print('你的余额：%d' % user_dic['account'])
                    break
                elif pay == 'N':
                    print('退出购物')
                    shopping_cart = {}
                    user_dic['account'] = account_old
                    break
                else:
                    rechoose = True
            break


        else:
            print('非法输入')


# 先登录再购物
# @login_inter
# def shopping():
#     print('===')




shopping()
