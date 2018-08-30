from flask import Flask
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy


import config

#实例化flask
app = Flask(__name__)

#加载配置文件
app.config.from_object(config)

#调试模式
app.debug = True

#实例化SQLAlchemy
db = SQLAlchemy(app)

#实例化redis
cache = Cache()
cache.init_app(app)

# 此处遇到一个坑，蓝图必须在实例之后引入，不然会报错 ImportError: cannot import name 'xx'
from app.admin import admin as admin_bp

#注册蓝图
app.register_blueprint(admin_bp)



@app.errorhandler(404)
def page_not_found(error):
    """
    定义404页面 找不大路由会走此方法
    :rtype: object
    """
    return "page is error..."