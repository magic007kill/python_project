# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :2..requests模块实现简易的网页采集器.py
@Author  :magic007
@Date    : 18:43
'''
# UA：User-Agent(请求载体的身份标识)
# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识
# 为某一款浏览器，说明该请求是一个正常的请求，但是，如果检测到请求的载体身份标识不是基于一款浏览器，则标识该
# 请求为不正常的请求（爬虫），则服务器端就很可能拒绝该次的请求。

# UA伪装:让爬虫对应的请求载体身份标识伪装成某一款浏览器


import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带额的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param,headers=headers)
    page_text = response.text
    filename = kw + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename, '保存成功！')

