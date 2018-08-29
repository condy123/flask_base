from flask import Flask
from flask_sqlalchemy import SQLAlchemy



import config


app = Flask(__name__)
app.config.from_object(config)
app.debug = True
db = SQLAlchemy(app)
# 此处遇到一个坑，蓝图必须在db实例之后引入，不然会报错 ImportError: cannot import name 'db'
from app.admin import admin as admin_bp
app.register_blueprint(admin_bp)


@app.errorhandler(404)
def page_not_found(error):
    return "page is error..."