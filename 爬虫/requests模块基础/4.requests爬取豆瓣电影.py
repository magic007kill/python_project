# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :4.requests爬取豆瓣电影.py
@Author  :magic007
@Date    : 22:21
'''
import requests
import json

if __name__ == "__main__":
    get_url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 表示从库中的第几部电影去取
        'limit': '20'  # 表示一次取出的个数
    }
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    response = requests.get(url=get_url, params=param, headers=headers)
    list_data = response.json()

    with open('./豆瓣.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)
        print('over!')
