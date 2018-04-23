# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 10:48
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : pengfu.py.py

import scrapy

from News_spider.MyUtils import Util
from News_spider.items import NewsItem


class PengfuSpider(scrapy.Spider):

    name = 'pengfu'

    allowed_domains = ['www.pengfu.com']
    start_urls = ['http://www.pengfu.com']

    def parse(self, response):
        for pagesize in range(1,50):
            url = "https://www.pengfu.com/index_{}.html".format(str(pagesize))
            yield scrapy.Request(url=url,callback=self.parse_list)

    def parse_list(self,response):
        item = NewsItem()
        node_list = response.xpath("//*[@class='list-item bg1 b1 boxshadow']")
        for v_node in node_list:
            author_name = v_node.xpath("./dl[@class='clearfix dl-con']/dd/p[@class='user_name_list']/a/text()").extract_first()
            title = v_node.xpath("./dl[@class='clearfix dl-con']/dd/h1[@class='dp-b']/a/text()").extract_first()
            title_link = v_node.xpath("./dl[@class='clearfix dl-con']/dd/h1[@class='dp-b']/a/@href").extract_first()
            if title and author_name and title_link:
                item['item_id'] = Util.to_md5(title)
                item['item_title'] = title
                item['item_type'] = "ARTICLE"
                item['item_title'] = title
                item['category'] = "搞笑"
                item['title_link'] = title_link
                item['item_source'] = '捧腹网'
                item['collect_time'] = Util.local_time()
                item['release_time'] = Util.local_time()
                item['author'] = author_name
                yield item




"""
item_id = scrapy.Field()
item_title = scrapy.Field()
item_type = scrapy.Field()
category = scrapy.Field()
title_link = scrapy.Field()
cut_url = scrapy.Field()
collect_time = scrapy.Field()
item_source = scrapy.Field()
release_time = scrapy.Field()
author = scrapy.Field()
"""