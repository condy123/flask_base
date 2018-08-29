import os
import uuid
from datetime import datetime


class Func():
    # 修改文件名称
    def change_filename(filename):
        fileinfo = os.path.splitext(filename)
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + fileinfo[-1]
        return filename