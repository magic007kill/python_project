# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :re模块.py
@Author  :magic007
@Date    : 12:56
'''
import re

# # findall: 匹配字符串中所有的符合正则的内容
# lst = re.findall(r'\d+', '我的电话号是:10010,我哥们的电话;10086')
# print(lst)
#
# # finditer:匹配字符串中所有的内容【返回的是迭代器】
# # 从迭代器中拿到内容需要.group()
# it = re.finditer(r'\d+', '我的电话号是:10010,我哥们的电话;10086')
# print(it)
# for pid in it :
#     print(pid.group())

# re.search()返回的结果是match对象，拿数据要.group()
# 且找到一个结果就返回
# s = re.search(r'\d+', '我的电话号是:10010,我哥们的电话;10086')
# print(s)
# print(s.group())

# match是从头开始匹配
# m = re.match(r'\d+', '10010,我哥们的电话;10086')
# print(m)
# print(m.group())

# 预加载正则表达式
# obj = re.compile(r'\d+')
# ret = obj.finditer('我的电话号是:10010,我哥们的电话;10086')
# for pid in ret:
#     print(pid.group())
#
# rfd = obj.findall('我的电话号是:10010,我哥们的电话;10086')
# for pid in rfd:
#     print(pid)

s = '''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='sylar'><span id='3'>大王</span></div>
<div class='tory'><span id='4'>秦始皇</span></div>
<div class='jolin'><span id='5'>小狗</span></div>
'''
# re.S->参数是把要查找的文本转换成单行字符串 ——也就是文本为了让"."能匹配换行符
# obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)
# res = obj.findall(s)
# for it in res:
#     print(it)
# 如果想要拿去指定的内容，则要在指定的内容上用()括起来，用findall可以直接取值
# 如果想要把他们进行分组，可以在想要的内容前加上?P<'想要的组号'>，这种方式要用finditer方法
obj = re.compile(r"<div class='(?P<en>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
# res = obj.findall(s)
# for it in res:
#     print(it)
res = obj.finditer(s)
for it in res:
    print(it.group('id'))
    print(it.group('en'))
    print(it.group('name'))

