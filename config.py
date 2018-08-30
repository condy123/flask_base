import os

# 所有的配置相关的key 必须是大写

SECRET_KEY = 'usda781qsyt562wsd0okmh'
CSRF_ENABLED = True
port = 5001
DEBUG=True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = True #设置这一项是每次请求结束后都会自动提交数据库中的变动

#图片上传地址
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),'app/static/uploads/')

#redis 相关配置
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''