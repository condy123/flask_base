from flask import Blueprint

#创建admin对象
admin = Blueprint('admin',__name__)
# 导入views,这个必须放在这！！！
import app.admin.views