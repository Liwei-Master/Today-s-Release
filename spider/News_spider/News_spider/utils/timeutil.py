# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 10:45
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : timeutil.py(时间工具类)
import datetime
import hashlib
import time


class TimeUtil():
    """
    :return md5
    """
    @classmethod
    def to_md5(self, target):
        if isinstance(target, str):
            local_time = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
            target_md5 = hashlib.md5((target + local_time).encode(encoding='UTF-8')).hexdigest()
            return str(target_md5)
        else:
            return None
    """
    :return local time
    """
    @classmethod
    def local_time(self):
        format_time = "%Y-%m-%d %H:%M:%S"
        cur_time = datetime.datetime.now().strftime(format_time)
        data_time = datetime.datetime.strptime(cur_time, format_time)
        return str(data_time)
