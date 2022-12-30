# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :1.正则应用_手刃豆瓣top250.py
@Author  :magic007
@Date    : 15:47
'''
import requests
import re
import csv

if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }
    # 正则表达式
    ex = r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<div class="star">.*?property="v:average">(?P<start>.*?)</span>.*? <span>(?P<NO>.*?)评价</span>'


    for no in range(0,10):
        page_NO = 25 * no
        page_NO = str(page_NO)
        pram = {
            'start': page_NO
        }
        response = requests.get(url=url, params=pram, headers=headers)
        page_content = response.text
        # 解析数据
        obj = re.compile(ex.strip(), re.S)
        result = obj.finditer(page_content)

        # 写入text格式文件中
        # with open('./豆瓣TOP250.txt', 'at', encoding='utf-8') as fp:
        #     fp.write('电影名单：'+'\n\n')
        #     for it in result:
        #         fp.write('电影名称:' + it.group('name') + '  ')
        #         fp.write('上映年份:' + it.group('year').strip() + '  ')
        #         fp.write('评分：' + it.group('start') + '  ')
        #         fp.write('评论人数：' + it.group('NO') + '  '+'\n')
        # 写入csv格式文件,不能同事把信息存储在豆瓣TOP250.csv与TOP250.txt文件中
        # 因为使用的是findinter方法进行数据筛选，所返回的是一个迭代器对象
        # 当上一个语句把迭代器值取完后，下一个语句就取不到了
        with open('./豆瓣TOP250.csv', 'at', encoding='utf-8') as fp:
            csv_writer = csv.writer(fp)
            for it in result:
                dic = it.groupdict()
                dic['year'] = dic['year'].strip()
                csv_writer.writerow(dic.values())
    print('over')
