# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : config.py
# @Software: PyCharm

import os

# 所有的配置相关的key 必须是大写

#提交表单要使用 SECRET_KEY，且在视图文件中使用对应的  {{ form.csrf_token }}
SECRET_KEY = 'usda781qsyt562wsd0okmh'
CSRF_ENABLED = True
port = 5001
DEBUG=True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wobugaosuni@localhost:3306/spider'
SQLALCHEMY_TRACK_MODIFICATIONS = True #设置这一项是每次请求结束后都会自动提交数据库中的变动

#图片上传地址
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),'app/static/uploads/')
# mongo
MONGODB_SETTINGS = {'db': 'post', 'host': 'localhost', 'port': 27017}