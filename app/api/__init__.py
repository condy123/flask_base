from flask import Blueprint

#创建admin对象
api = Blueprint('api',__name__)


import app.api.views