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
    item_source = scrapy.Field()
    # 原新闻发布时间
    release_time = scrapy.Field()
    # 新闻发布作者，若无则填写平台
    author = scrapy.Field()

    # 正文内容（此处只要文本）
    # content = scrapy.Field()
    # 文本主题
    # tags = scrapy.Field()
    #
    # item_id = scrapy.Field()
    # title = scrapy.Field()
    # item_type = scrapy.Field()
    # create_type = scrapy.Field()          # 是原创还是转发
    # source = scrapy.Field()
    # original_url = scrapy.Field()
    # author = scrapy.Field()
    # category = scrapy.Field()              # 类型image_url
    # body = scrapy.Field()
    # images = scrapy.Field()
    # videos = scrapy.Field()
    # audios = scrapy.Field()
    # copyright = scrapy.Field()  # 版权
    # release_time = scrapy.Field()
    # janesi_time = scrapy.Field()
    # scan = scrapy.Field()  # 阅读数
    # like = scrapy.Field()  # 喜欢
    # share = scrapy.Field()  # 分享
    # play = scrapy.Field()  # 播放次数
    # forward = scrapy.Field()  # 转发次数
    # collect = scrapy.Field()  # 收藏数
    # image_urls = scrapy.Field()
    # cut_url = scrapy.Field()
    # duration = scrapy.Field()
    # size = scrapy.Field()
    # # 上传至cos的flag
    # images_success = scrapy.Field()
    #
    # tag = scrapy.Field()
    # channel = scrapy.Field()
    # child_channel = scrapy.Field()
    # topic = scrapy.Field()
    # keyword = scrapy.Field()
    # region = scrapy.Field()
    #
    #
    # name = scrapy.Field()
    # avatar = scrapy.Field()
    # type = scrapy.Field()
    # fans_count = scrapy.Field()
    # scan_count = scrapy.Field()
    # collect_count = scrapy.Field()
    # is_delete = scrapy.Field()
    # gmt_create =scrapy.Field()
    # gmt_modified = scrapy.Field()
    # platform = scrapy.Field()
    # upload_file_flag = scrapy.Field()

