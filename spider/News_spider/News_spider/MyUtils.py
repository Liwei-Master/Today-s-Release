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

    @classmethod
    def replace_style(self, origin_content):

        if origin_content:
            if isinstance(origin_content, str):
                # 过滤掉style 样式
                content = re.sub(r'style="(.*?)"', '', origin_content)
                # 内容里的跳转链接不可点击
                content = re.sub(r'target="_blank"', '', content)
                content = re.sub(r'width="(.*?)"','',content)
                content = re.sub(r'height="(.*?)"','',content)
                content = re.sub(r'align="center"','',content)
                content = re.sub(r'img_height="(.*?)"','',content)
                content = re.sub(r'img_width="(.*?)"','',content)
                content = content.replace('href=', '')
                # content = re.sub('data-original', 'src', content)
                if 'sizes=' in content:
                    content = re.sub('sizes=".*"','',content)
                return content
            else:
                return None
        else:
            return None


    @classmethod
    def generate_pic_time(self, target_url, cos_type=None):
        date = datetime.date.today()
        date = str(date).replace('-', '')

        if isinstance(target_url, str):
            pic_name = target_url.split('/')[-1]
            print('pic_name == ',pic_name)
            if "."in pic_name:
                if cos_type:
                    pic_name = 'news/' + date  + '/' + str(pic_name)
                else:
                    pic_name = '//yun1.janesi.net/news/' + date  + '/' + str(pic_name)
                return pic_name
            else:
                if cos_type:
                    pic_name = 'news/' + date  + '/' + str(pic_name) + ".jpg"
                else:
                    pic_name = '//yun1.janesi.net/news/' + date  + '/' + str(pic_name) + ".jpg"
                return pic_name
        else:
            return None

    @classmethod
    def generate_pic_time_qq(self, target_url, cos_type=None):
        date = datetime.date.today()
        date = str(date).replace('-', '')
        if isinstance(target_url, str):
            pic_name = target_url.split('/')[-2]
            if cos_type:
                pic_name = 'news/' + date + '/' + str(pic_name) + ".jpg"
            else:
                pic_name = '//yun1.janesi.net/news/' + date + '/' + str(pic_name) + ".jpg"
            return pic_name
        else:
            return None

    @classmethod
    def generate_pic_time_yd(self, target_url, cos_type=None):
        date = datetime.date.today()
        date = str(date).replace('-', '')
        if isinstance(target_url, str):
            pic_name = target_url.split('/')[-1].split('=')[-1]
            if cos_type:
                pic_name = 'news/' + date + '/' + str(pic_name) + '.jpg'
            else:
                pic_name = '//yun1.janesi.net/news/' + date + '/' + str(pic_name) + '.jpg'
            return pic_name
        else:
            return None

    # 除去不必要的标签
    @classmethod
    def remove_impurity(self, content):

        cleaner = Cleaner(scripts=True, annoying_tags=True, remove_unknown_tags=True, style=True,
                          links=True, page_structure=False, safe_attrs_only=False, )
        html = cleaner.clean_html(content)
        return html


    # 作者的id
    @classmethod
    def author_id(self):
        msec_id = round(time.time() * 10000)
        return msec_id

    # 造假随机阅读数
    @classmethod
    def random_number(self):
        return random.randint(50, 500)

    @classmethod
    def check_item(self, item):
        right = 0
        loser = 1
        if isinstance(item['item_id'], str) and isinstance(item['title'], str) and isinstance(item['item_type'], str)\
            and isinstance(item['create_type'], str) and isinstance(item['source'], str) and isinstance(item['original_url'], str) and isinstance(item['body'], str) \
            and isinstance(item['name'], str) and isinstance(item['channel'], str) and isinstance(item['tag'], list) and isinstance(item['scan'], int) and isinstance(item['like'], int)\
            and isinstance(item['share'], int) and isinstance(item['play'], int) and isinstance(item['forward'], int) and isinstance(item['collect'], int)\
            and isinstance(item['release_time'], str) and isinstance(item['janesi_time'], str) and isinstance(item['images'], list) and isinstance(item['videos'], list)\
            and isinstance(item['audios'], list) and isinstance(item['copyright'], str) and isinstance(item['platform'], str) and isinstance(item['avatar'], str)\
            and isinstance(item['type'], int) and isinstance(item["category"], dict) and isinstance(item['author'], dict):

            return right
        else:
            return loser

