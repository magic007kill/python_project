# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :3.bs4基本使用.py
@Author  :magic007
@Date    : 9:53
'''
# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据
import re
import requests
from bs4 import BeautifulSoup
import json
import csv

if __name__ == '__main__':
    # 抓取新发地蔬菜价格数据（re抓取）
    # url = 'http://www.xinfadi.com.cn/getPriceData.html'
    # headers = {
    #     'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    # }
    # ex = r'\"prodName\":\"(?P<name>.*?)\".*?prodCat\":\"(?P<group>.*?)\".*?"lowPrice\":\"(?P<low_price>.*?)\",\"highPrice\":\"(?P<high_price>.*?)\",\"avgPrice\":\"(?P<avg_price>.*?)\"'
    # obj = re.compile(ex, re.S)
    # # 抓取前9页的菜价数据(试下数据)
    # for i in range(1, 10):
    #     data = {
    #         'limit': 100,
    #         'current': i,
    #         'pubDateStartTime': '',
    #         'pubDateEndTime': '',
    #         'prodPcatid': 1186,
    #         'prodCatid': '',
    #         'prodName': ''
    #     }
    #     response = requests.post(url=url, data=data, headers=headers)
    #     result = obj.finditer(response.text)
    #     for it in result:
    #         with open('./菜价.csv', 'at', encoding='utf-8') as fp:
    #             fp.write('菜名：%s  ' % it.group('name'))
    #             fp.write('种类：%s  ' % it.group('group'))
    #             fp.write('最低价格：%s  ' % it.group('low_price'))
    #             fp.write('最高价格：%s  ' % it.group('high_price'))
    #             fp.write('平均价格：%s  ' % it.group('avg_price'))
    #             fp.write('\n')
    #
    # print("over!")

    # 抓取今日菜价数据（bs4抓取）
    url = 'http://zhongdapeng.com/shucaijiage/1187.html'
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    f = open('今日菜价.csv', 'w', encoding='utf-8')
    csvwriter = csv.writer(f)
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding

    # 解析数据
    # 1.把页面源代码交给BeautifuSoup进行处理，生成bs对象
    # BeautifulSoup中的'html.parser'参数是声明传入的是html源代码
    page = BeautifulSoup(response.text, 'html.parser')
    # 2.从bs对象中查找数据
    # find(标签，属性=值) ——找到第一个相关数据返回
    # find_all(标签，属性=值) ——找到所有相关数据返回
    # 如果需要添加属性筛选如：'class_='h1'实际上是'class='h1',避免关键字冲突
    # 如：table = page.find('table'，class_='h1')
    # 也可以写为：table = page.find('table'，attrs={'class':'h1'})
    table = page.find('table')
    trs = table.find_all('tr')[1:]
    for tr in trs:  # 每一行
        tds = tr.find_all('td')
        name = tds[1].text  # .text 表示拿到被标签标记的内容
        price = tds[2].text
        print(name, price)
        csvwriter.writerow([name, price])
    f.close()
    print('over')
