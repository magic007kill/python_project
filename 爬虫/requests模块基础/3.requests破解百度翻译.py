# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :3.requests破解百度翻译.py
@Author  :magic007
@Date    : 21:34
'''
import json

import requests

if __name__ == "__main__":
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'

    # 2.进行UA伪装
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    # 3.post请求参数处理(同get请求一致)
    word = input('enter a word: ')
    data = {
        'kw': word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应的数据:json()方法返回的是一个对象(如果确认响应数据是json类型的，才能用json)
    dic_obj = response.json()
    # 持久化存储

    # 直接将翻译结果存储在一个文档中
    # with open('./翻译文档.json', 'at', encoding='utf-8') as fp:
    #     json.dump(dic_obj, fp=fp, ensure_ascii=False)
    #     fp.write('\n')
    #     print("over!")

    # 每次翻译结果单独存储到一个文件中
    filename = word + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dic_obj, fp=fp, ensure_ascii=False)
        print("over!")
