# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : models.py
# @Software: PyCharm

from datetime import datetime

from app import mdb


class Post(mdb.Document):
    title = mdb.StringField()
    title_url = mdb.StringField()
    url = mdb.StringField()
    content = mdb.StringField()
    create_time = mdb.DateTimeField(default=datetime.now)

# 运行此处会连接数据库建立对应的表
if __name__ == '__main__':
    pass
    # 创建表
    # db.create_all()
    # db.session.commit()