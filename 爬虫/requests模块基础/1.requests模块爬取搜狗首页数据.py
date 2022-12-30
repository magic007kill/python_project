# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :1.requests模块爬取搜狗首页数据.py
@Author  :magic007
@Date    : 14:47
'''

'''
requests模块的作用：
    模拟浏览器发出请求
如何使用：(requests模块的编码流程)
    —— 指定url
    —— 发起请求
    —— 获取响应数据
    —— 持久化存储
环境安装：
    pip install requests   
    如果下载速度太慢可以使用国内的清华源镜像资源：
    临时下载：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
        
'''
import requests

# 爬取搜狗首页
if __name__ == '__main__':
    # 1.指定url
    url = 'https://www.sogou.com/'
    # 2.发起请求
    # get方法会返回一个响应对象
    # 3.response 获取响应数据
    response = requests.get(url=url)
    # response.text方法获得响应对象的字符串数据,并打印
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')

