# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 14:08
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : zaker.py(http://www.myzaker.com  zaker 新闻)
import re

import scrapy

from News_spider.MyUtils import Util
from News_spider.items import NewsItem


class CarTouTiaoSpider(scrapy.Spider):

    name = 'qctt'

    allowed_domains = ['www.qctt.cn']

    start_urls = ['https://www.qctt.cn/home/video']

    def parse(self, response):
        item = NewsItem()
        video_infos = response.xpath("//*[@class='article clearfix']")
        for v_video in video_infos:
            title_link = v_video.xpath("./div[@class='img']/a/@href").extract_first()
            title = v_video.xpath("./div[@class='words']/div[@class='part1 clearfix']/div[@class='words_title']/a/text()").extract_first()
            author = v_video.xpath("./div[@class='words']/div[@class='words_1']/span[1]/text()").extract_first()
            release_time = v_video.xpath("./div[@class='words']/div[@class='words_1']/span[2]/text()").extract_first()
            if title and author and title_link:
                item['item_id'] = Util.to_md5(title)
                item['item_title'] = title
                item['item_type'] = "ARTICLE"
                item['item_title'] = title
                item['category'] = "汽车"
                item['item_source'] = '汽车头条'
                item['title_link'] = title_link
                item['collect_time'] = Util.local_time()
                item['release_time'] = release_time
                item['author'] = author
                yield item
