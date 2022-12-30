# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :2.正则应用_屠戮电影天堂.py
@Author  :magic007
@Date    : 20:37
'''

# 任务要求：
# 1.定位到2022必看片
# 2.从2022必看片中提取到子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的下载地址

import requests
import re

if __name__ == '__main__':
    # 获取主页面url
    url_main = 'https://www.dy2018.com/'
    # 伪装浏览器
    # 若不用伪装，可以在requests参数中令verify=False —— 不做安全验证，一般不建议这样做
    # 如：requests.get(url=url_main, verify=False)
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    # 取到网页源代码
    response = requests.get(url=url_main, headers=headers)
    # 发现源代码有汉字乱码，对乱码进行处理
    # 第一种: 自动匹配字符集 —— 建议用这个
    response.encoding = response.apparent_encoding
    # 第二种：手动把代码进行从新指定字符集，与网页源代码一致
    # response.encoding = 'gb2312'
    ex1 = r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>'
    obj1 = re.compile(ex1, re.S)
    result1 = obj1.finditer(response.text)
    # 定位到2022必看片
    ul1 = result1.__next__().group('ul').strip()
    # 第一件事完成
    print('↑' * 20 + '定位到2022必看片' + '↑' * 20)

    ex2 = r"<li><a href='(?P<ul>.*?)'"
    # 提取子页面
    obj2 = re.compile(ex2, re.S)
    result2 = obj2.finditer(ul1)
    child_href_list = []
    for it in result2:
        ul2 = it.group('ul')
        # 拼接子页面url地址：域名+子页面地址
        child_href = url_main + ul2.strip('/')
        child_href_list.append(child_href)
    print('↑' * 20 + '从2022必看片中提取到子页面的链接地址' + '↑' * 20)

    # 提取子页面的内容
    ex3 = r'◎译　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">'
    obj3 = re.compile(ex3, re.S)
    for href in child_href_list:
        child_responce = requests.get(url=href, headers=headers)
        child_responce.encoding = child_responce.apparent_encoding
        result3 = obj3.finditer(child_responce.text)
        for it in result3:
            print(it.group('name'))
            print(it.group('download'))
    print('↑' * 20 + '拿到我们想要的下载地址' + '↑' * 20)
    print('over')
