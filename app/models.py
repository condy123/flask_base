# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : models.py
# @Software: PyCharm

from datetime import datetime

from app import db

class User(db.Model):
    __tablename__ = 'user'
    id       = db.Column(db.Integer,    primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    logo = db.Column(db.String(255), unique=True)  # 封面

    def __repr__(self):
        return '<User %r>' % self.username

    # 验证密码
    def check_password(self,password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password,password)


class Artcle(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64),nullable=False)
    content = db.Column(db.TEXT,nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

# 运行此处会连接数据库建立对应的表
if __name__ == '__main__':
    # 创建表
    db.create_all()
    db.session.commit()