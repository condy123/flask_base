# -*- coding:utf-8 -*-

# @Author  : tang
# @Contact : 373162947@qq.com
# @Time    : 2018/8/28 17:55
# @File    : func.py
# @Software: PyCharm

# 主要用于定义一些常用功能
import os
import uuid
from datetime import datetime


class Func():
    # 修改文件名称
    def change_filename(filename):
        fileinfo = os.path.splitext(filename)
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + fileinfo[-1]
        return filename