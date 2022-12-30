# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :job_spider.py
@Author  :magic007
@Date    : 8:52
'''
import json
import re

'''
什么是爬虫：
    通过编写程序，模拟浏览器上网，然后去让其抓取数据的过程
    
爬虫在使用场景的分类 
    —— 通用爬虫：
        搜索引擎抓取系统重要组成部分。抓取的是一整张页面数据。
    —— 聚焦爬虫：
        是建立在通用爬虫的基础之上。抓取的是页面中特定的局部内容。
    —— 增量式爬虫：
        检测网站中数据更新的情况。只会抓取网站中最新出来的数据。
robots.txt协议：
    —— 规定了网站中哪些数据可以被爬虫爬取，哪些数据不能被爬取                    
http协议
    —— 概念：就是服务器与客户端进行数据交互的一种形式
常用的请求头信息
    —— User_Agent:请求载体（浏览器）的身份标识   
    —— Connection:请求完毕后，是断开连接还是保持连接 
常用响应头信息    
    —— Content-Type:服务器响应回客户端的数据类型
           
https协议:
    —— 安全的http协议
加密方式
    —— 对称密钥加密
    —— 非对称密钥加密
    —— 证书密钥加密（http使用）
'''
# 导入http网络请求库
import requests
from bs4 import BeautifulSoup  # 导入bs4网页选择器的BeautifulSoup模块

headers = {
   ' User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}


def get_html(url):
    '''
    两个参数：用户代理
            访问的网站链接
    :param url:
    :return:
    '''
    # text方法：将网页源代码通过文本的形式返回
    response = requests.get(url, headers=headers).text
    return response

def search_job(job_name):
    for index in range(1,2):
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(job_name,index)
        # "{} {}".format("hello", "world")  不设置指定位置，按默认顺序
        # 输出效果： 'hello world'
        print('正在访问：第%s页' % index)
        html = get_html(url)
        lst = re.findall('{"top_ads".*?</script>',html)
        re_scrip = re.compile('</scrip>',re.I)
        res = re_scrip.sub('',str(lst))
        formats = eval(res)
        s = json.loads(formats[0])
        data = s.get('engine_search_result')
        job_info = []
        for info in data:
            item = {
                'name':info.get('job_name'),
                'company':info.get('company_name')

            }
    print(item)



if __name__ == '__main__':
    # url = 'https://www.chinahr.com/'
    # html = get_html(url)
    # print(get_html(url))
    search_job('')
