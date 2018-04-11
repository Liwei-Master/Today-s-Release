# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 14:08
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : zaker.py(http://www.myzaker.com  zaker 新闻)
import re

import scrapy

from News_spider.items import NewsItem
from News_spider.utils.timeutil import TimeUtil


class ZakerSpider(scrapy.Spider):

    name = 'zaker'

    allowed_domains = ['www.myzaker.com']

    start_urls = ['http://www.myzaker.com']

    def parse(self, response):
        base_url = 'http://www.myzaker.com/channel/4'

        v1_dict = {
            '财经':'4',
            '科技':'13',
            '体育': '8',
            '军事': '3',
            '娱乐': '9',
            '汽车': '7',
            '时尚': '12',
            '旅游': '981',
            '游戏': '10376',
            '健康': '10802',
            '美食': '10386',
            '星座': '1014',
        }

        for channel, tag_link in v1_dict.items():
            type_link ='http://www.myzaker.com/channel/{}'.format(tag_link)
            # print('link: ',channel,type_link)
            yield scrapy.Request(url=type_link,callback=self.get_main_link,meta={'channel':channel},dont_filter=True)

    def get_main_link(self,response):

        channel = response.meta['channel']

        article_list = response.xpath("//*[@class='figure flex-block']")
        # print('article_list ',article_list)
        for article in article_list:
            a_link = article.xpath("./a[@class='img']/@href").extract_first()
            if a_link:
                item_link = response.urljoin(a_link)
                # item_link = 'http://www.myzaker.com/article/5aaf31637f780b1438015351'
                # item_link = 'http://www.myzaker.com/article/5ab1e62d77ac6472e55e3f92/'
                # item_link = 'http://www.myzaker.com/article/5ab1bd639490cbcb3100003f/'
                yield scrapy.Request(url=item_link,callback=self.parse_detail,meta={'channel':channel})

    def parse_detail(self,response):
        item=NewsItem()
        channel = response.meta['channel']
        article_title = response.xpath("//*[@class='article_header']/h1/text()").extract_first()
        _article_author = response.xpath("//*[@class='article_tips']/a/span[@class='auther']/text()").extract_first()
        article_author = 'ZAKER'
        if _article_author:
            article_author = _article_author
        article_time = response.xpath("//*[@class='article_tips']/a/span[@class='time']/text()").extract_first()

        item['item_title']=article_title
        item_id=TimeUtil.to_md5(article_title)
        item['item_id']=item_id
        item['item_type'] = 'ARTICLE'
        item['source']='ZAKER'
        item['title_link']=response.url
        item['cut_url'] = ''
        item['collect_time'] = TimeUtil.local_time()
        item['release_time'] = article_time
        item['author'] = article_author
        item['category'] = channel
        print('item ',item)
        yield item



""""
    item_id = scrapy.Field()
    item_title = scrapy.Field()
    item_type = scrapy.Field()
    category = scrapy.Field()
    title_link = scrapy.Field()
    cut_url = scrapy.Field()
    collect_time = scrapy.Field()
    source = scrapy.Field()
    release_time = scrapy.Field()
    author = scrapy.Field()
"""