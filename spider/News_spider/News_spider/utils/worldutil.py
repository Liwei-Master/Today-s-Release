# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 14:26
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : worldutil.py.py(对文本内容tag主题抽取的工具类)
import random
import re
import jieba.analyse
import jieba
from gensim import corpora, models, similarities

class worldutil():
    """
    类变量
    """
    stop_list = []

    contents = []

    def __init__(self):
        stop_list = []
        # loading stop words
        with open('stop_words.txt') as f:
            for line in f:
                stop_list.append(f)
        self.stop_list = set(stop_list)



    @classmethod
    def anay_content(self,content):
        """
        目标文本通过结巴分词等工具，分析出对应的主题（list类型的tag）
        :param content: 
        :return: 
        """
        if content:
            print('*****************  starting  ************   ')
            path = 'E:\\MyWorksWithLiWEI\\Today-s-Release\\spider\\News_spider\\News_spider\\utils\\stop_words.txt'
            jieba.analyse.set_stop_words(path)
            keywords = jieba.analyse.extract_tags(self.filter_tags(content), topK=random.randint(3,5))
            return keywords
        else:
            print('error content =========>>> ')
            return














































    @classmethod
    def replaceCharEntity(self,htmlstr):
        CHAR_ENTITIES = {'nbsp': ' ', '160': ' ', 'lt': '<', '60': '<', 'gt': '>', '62': '>', 'amp': '&', '38': '&',
                         'quot': '"', '34': '"', }

        re_charEntity = re.compile(r'&#?(?P<name>\w+);')
        sz = re_charEntity.search(htmlstr)
        while sz:
            entity = sz.group()
            key = sz.group('name')
            try:
                htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
            except KeyError:

                htmlstr = re_charEntity.sub('', htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
        return htmlstr


    @classmethod
    def filter_tags(self,content):
        """fileter HTML tag and http link"""
        re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)
        re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
        re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
        re_br = re.compile('<br\s*?/?>')
        re_h = re.compile('</?\w+[^>]*>')
        re_comment = re.compile('<!--[^>]*-->')
        s = re_cdata.sub('', content)
        s = re_script.sub('', s)
        s = re_style.sub('', s)
        s = re_br.sub('\n', s)
        s = re_h.sub('', s)
        s = re_comment.sub('', s)
        blank_line = re.compile('\n+')
        s = blank_line.sub('\n', s)
        s = self.replaceCharEntity(s)
        return s
