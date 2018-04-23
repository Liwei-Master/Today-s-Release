# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 14:08
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : zaker.py(http://www.myzaker.com  zaker 新闻)
import re

import scrapy



class CarTouTiaoSpider(scrapy.Spider):
    pass
    #
    # name = 'qctt'
    #
    # allowed_domains = ['www.qctt.cn']
    #
    # start_urls = ['https://www.qctt.cn/home/video']
    #
    # def parse(self, response):
    #     item = NewsItem()
    #     print('response ',response)
    #     video_infos = response.xpath("//*[@class='article clearfix']")
    #     for v_video in video_infos:
    #         detail_link = v_video.xpath("./div[@class='img']/a/@href").extract_first()
    #         cut_url = v_video.xpath("./div[@class='img']/a/img/@src").extract_first()
    #         duration = v_video.xpath("./div[@class='img']/p[@class='time']/span/text()").extract_first()
    #         title = v_video.xpath("./div[@class='words']/div[@class='part1 clearfix']/div[@class='words_title']/a/text()").extract_first()
    #         author = v_video.xpath("./div[@class='words']/div[@class='words_1']/span[1]/text()").extract_first()
    #         release_time = v_video.xpath("./div[@class='words']/div[@class='words_1']/span[2]/text()").extract_first()
    #         print('duration:  ' , duration, 'author ',author,'release_' ,release_time,'title  ',title, 'cut_url :',cut_url,)
    #         if detail_link:
    #             yield scrapy.Request(url=detail_link,callback=self.parse_detail,meta={'item':item})
    #
    # def parse_detail(self,response):
    #     item = response.meta['item']
    #     mp4_source = response.xpath("//*[@class='video']/video[@id='video']/@src").extract_first()
    #     print('mp4_source ',mp4_source)