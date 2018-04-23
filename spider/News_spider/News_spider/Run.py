# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 13:57
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : Run.py.py(scrapy 启动程序)
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.join(os.getcwd()))

targetLine = 'qctt'
# targetLine = 'pengfu'
# targetLine = 'zaker'
execute(['scrapy', 'crawl', targetLine])