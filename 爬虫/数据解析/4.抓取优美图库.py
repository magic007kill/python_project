# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :4.抓取优美图库.py
@Author  :magic007
@Date    : 20:59
'''
# 1.拿到主页面的源代码，然后拿到子页面的链接地址——herf
# 2.通过href拿到子页面的内容，从子页面中拿到图片下载的地址
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    url = 'http://www.umeituku.com/weimeitupian/'
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }

    response = requests.get(url=url, headers=headers)
    # 处理乱码
    response.encoding = response.apparent_encoding
    # 把源代码交给bs
    main_page = BeautifulSoup(response.text, 'html.parser')
    alist = main_page.find('div', class_="TypeList").find_all('a')
    for a in alist:
        # 直接通过get就可以拿到属性的值,
        # a变量是一个class 'bs4.element.Tag'的类
        herf = a.get('href')
        # 进子页面那源代码
        child_response = requests.get(url=herf, headers=headers)
        # 处理乱码
        child_response.encoding = child_response.apparent_encoding
        # 拿到子页面的源代码
        child_page_text = child_response.text
        # 从子页面中拿到图片的下载地址
        child_page = BeautifulSoup(child_page_text, 'html.parser')
        img = child_page.find('div', class_='ImageBody').find('img')
        # 拿到图片地址
        src = img.get('src')
        # 拿到图片名字
        img_name = img.get('alt')
        # 下载图片
        img_resp = requests.get(url=src, headers=headers)
        # 拿到二进制文件
        img_bin = img_resp.content
        # 拿到url中最后一个’.‘以后的内容 —— 图片格式
        img_format = src.split('.')[-1]
        with open('img/'+img_name+'.'+img_format, 'wb') as fp:
            # 把图片内容写入文件内
            fp.write(img_bin)
        print('已经下载了%s' % img_name)
        time.sleep(1)

    print('over')



