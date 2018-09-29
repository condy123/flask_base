# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : views.py
# @Software: PyCharm


from app.https.spider import Google
from app.https.spider_test import my_background_task
from . import api


@api.route('/py')
def py():
    # dict = {'title': '1234', 'title_url': "1234", 'url': "1234", 'content': "1234"}
    my_background_task.delay(str = 'led+display+screen')
    # posts = service.insert(dict)
    # posts = service.getPost()
    # print(posts)
    return '12'



@api.route('/test')
def test():
    my_background_task('led+display+screen')


@api.route('/test1')
def test1():
    return '12312312'