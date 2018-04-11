# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

""""
category：
财经
科技
体育
军事
娱乐
汽车
时尚
旅游
游戏
健康
美食
星座

"""
class NewsItem(scrapy.Item):
    # 新闻id
    item_id = scrapy.Field()
    # 新闻标题
    item_title = scrapy.Field()
    # 新闻类型（图文，视频，图集）
    item_type = scrapy.Field()
    # 新闻类别（图文（娱乐，科技，军事，财经等））
    category = scrapy.Field()
    # 新闻详情链接
    title_link = scrapy.Field()
    # 新闻列表页截图
    cut_url = scrapy.Field()
    # 新闻爬取时间（这里为入库时间）
    collect_time = scrapy.Field()
    # 新闻来源（来自哪个网站）
    source = scrapy.Field()
    # 原新闻发布时间
    release_time = scrapy.Field()
    # 新闻发布作者，若无则填写平台
    author = scrapy.Field()

