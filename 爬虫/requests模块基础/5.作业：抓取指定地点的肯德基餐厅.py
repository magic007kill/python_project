# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :5.作业：抓取指定地点的肯德基餐厅.py
@Author  :magic007
@Date    : 22:57
'''
import json

import requests

if __name__ == '__main__':
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }

    kw = input('请输入查询地点： ')
    no = input('请输入显示页数： ')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': no,
        'pageSize': '10'
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    json_data = response.json()
    print(json_data)
    filename = kw + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(json_data, fp=fp, ensure_ascii=False)
        print('over!')
