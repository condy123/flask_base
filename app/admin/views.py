# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : views.py
# @Software: PyCharm
import os
from functools import wraps

from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from app.models import User, Artcle
from app.util.func import Func
from . import admin
from flask import render_template, request, redirect, url_for, flash, session, g
from app.admin.forms import LoginForm, RegForm
from app import db, app, cache


@admin.route('/index')
def index():
    """
    首页
    :return:
    """
    if 'username' in session.keys():
        username = session['username']
    else:
        username = ''
    return render_template('admin/index.html',username=username)


# methods 可以访问的方式
@admin.route('/login', methods=['GET','POST'])
def login():
    """
    登陆
    :return:
    """
    form = LoginForm()
    if request.method == 'POST':
        # 验证方式 一
        # form = LoginForm(request.form)
        # value = form.validate() 验证通过返回true
        # 验证方式 二
        form = LoginForm()
        if form.validate_on_submit():
            data = form.data
            user = User.query.filter_by(username=data['username']).first()
            if not user.check_password(data['password']):
                flash('账号不存在、或密码错误','error')
            # 查表进行相关判断
            else:
                session['username'] = user.username
                session['userid'] = user.id
                g.username = user.username
                g.userid=user.id
                return redirect(url_for('admin.index'))
    # 传递form是为了提交表单自动验证
    return render_template('admin/login.html', form=form)



@admin.route('/reg', methods=['GET','POST'])
def reg():
    """
    注册页面
    :return:
    """
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.data
            file_logo = secure_filename(form.logo.data.filename)
            if not os.path.exists(app.config['UP_DIR']):
                os.makedirs(app.config['UP_DIR'])
                os.chmod(app.config['UP_DIR'], 777)
            logo = Func.change_filename(file_logo)
            form.logo.data.save(app.config['UP_DIR'] + logo)
            # 已经在RegForm里面查询用户名是否存在
            user = User(
                username=data['username'],
                password=generate_password_hash(data['password']),
                logo=logo
            )
            db.session.add(user)
            db.session.commit()
            flash('注册成功', 'OK')
            return redirect(url_for('admin.login'))
    # 传递form是为了提交表单自动验证
    return render_template('admin/reg.html', form=form)

@admin.route('/logout')
def logout():
    """
    退出登录
    :return:
    """
    session.pop('username', None)
    session.pop('userid', None)
    return redirect(url_for('admin.index'))

# 登录装饰器 (装饰器必须在调用函数前面)
def is_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function

@admin.route('/article')
@is_login
@cache.cached(timeout=60*2) #使用reids缓存 但是不建议这么用，还是使用第三方的reidis  set get方便
def article():
    articles = Artcle.query.all()
    return render_template('admin/article.html', username = session['username'], article = articles)

@admin.route('/logo')
@is_login
def logo():
    user = User.query.filter_by(id=session['userid']).first()
    return render_template('admin/logo.html', logo=user.logo)


