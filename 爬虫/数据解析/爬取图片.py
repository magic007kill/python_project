# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :爬取图片.py
@Author  :magic007
@Date    : 11:24
'''
'''
# content返回的是二进制形式的图片数据
    text(字符串) content(二进制) json()(对象)
    image_data = requests.get(url=url).content

    with open('./图片.jpg', 'wb') as fp:
        fp.write(image_data)
'''
import requests
import re

# 如何爬取新浪军事图片
if __name__ == '__main__':
    # 找到图片网页的url
    url = 'http://slide.mil.news.sina.com.cn/?choice=1'
    # 伪装UA
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    # 使用通用爬虫对url对应的一整张网页进行爬取
    page = requests.get(url=url, headers=headers)
    # 进行乱码处理
    page.encoding = page.apparent_encoding
    page_text = page.text
    # with open('图片地址.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page.text)
    # 使用聚焦爬虫将页面中所有的图片进行解析
    ex = r'<div class="item">.*?;img=(.*?)" alt.*?</div>'
    obj = re.compile(ex, re.S)
    image_src_iter = re.finditer(page_text)
    for it in image_src_iter:
        print(it.group())

