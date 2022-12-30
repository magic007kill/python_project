# ！  C:\Users\熊健熹\AppData\Local\Programs\Python\Python310
# _*_ coding: UTF-8 _*_
'''
@Project :python高级
@File    :正则练习.py
@Author  :magic007
@Date    : 11:01
'''
import re

# ex = re.compile(r'<div class="item">.*?;img=(.*?)" alt.*?</div>')
# page_text ='<div class="item"><div class="bg"></div><div class="hd"><a target="_blank" href="http://slide.mil.news.sina.com.cn/h/slide_8_203_139554.html"><img src="//z0.sinaimg.cn/auto/resize?size=235_156&amp;img=http://n.sinaimg.cn/front/200/w600h400/20221222/6b66-cb76abe0feb255f6c60c42cdc70f64e4.jpg" alt="中俄海上联合军演开幕"></a></div><div class="bd"><h3><a href="http://slide.mil.news.sina.com.cn/h/slide_8_203_139554.html" title="中俄“海上联合—2022”联合军事演习举行开幕式">中俄海上联合军演开幕</a></h3><p>12月21日下午4时，中俄“海上联合—2022”军事演习开幕式在东海某海域举行。中方在指挥舰济南舰上举...</p></div><div class="ft"><span class="time"><i></i>12/22 15:45</span><a node-type="smallCmnt" action-data="jc_slidenews-album-203-139554" title="评论" href="http://slide.mil.news.sina.com.cn/h/slide_8_203_139554.html#J_Comment_Wrap" class="comment"><i></i>3</a><span node-type="smallLike" action-data="jc_slidenews-album-203-139554" title="喜欢" class="like"><i></i>0</span></div></div>>'
# mo = ex.search(page_text)
# print(mo.group(1))
ex = r"<div class=\"item\">.*?<img src=.*?;img=\"(.*?) alt="
with open('图片地址.html', 'r', encoding='utf-8') as fp:
    page_text = fp.read()
image_src_list = re.findall(ex, page_text, re.S)
print(image_src_list)
