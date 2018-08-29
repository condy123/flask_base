import os

SECRET_KEY = 'usda781qsyt562wsd0okmh'
CSRF_ENABLED = True
port = 5001
debug=True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = True #设置这一项是每次请求结束后都会自动提交数据库中的变动
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),'app/static/uploads/')