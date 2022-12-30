# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :6.requests药监局化妆品相关备案记录的爬取.py
@Author  :magic007
@Date    : 9:05
'''
import requests
import json

if __name__ == '__main__':
    url = 'https://hzpba.nmpa.gov.cn/gccx/'
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    json_obj = requests.get(url=url, headers=headers).text

    with open('./化妆品.json', 'w', encoding='utf-8') as fp:
        json.dump(json_obj, fp=fp, ensure_ascii=False)
        print('over!')
