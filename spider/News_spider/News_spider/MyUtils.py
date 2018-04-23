# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 9:54
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : MyUtils.py(工具类信息)
import datetime
import hashlib
import random
import re

import time

from lxml.html.clean import Cleaner



class Util():

    @classmethod
    def to_md5(self, target):
        if isinstance(target, str):
            jiansi_time = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
            target_md5 = hashlib.md5((target + jiansi_time).encode(encoding='UTF-8')).hexdigest()
            return str(target_md5)
        else:
            return None

    @classmethod
    def local_time(self):
        format_time = "%Y-%m-%d %H:%M:%S"
        cur_time = datetime.datetime.now().strftime(format_time)
        data_time = datetime.datetime.strptime(cur_time, format_time)
        return str(data_time)





