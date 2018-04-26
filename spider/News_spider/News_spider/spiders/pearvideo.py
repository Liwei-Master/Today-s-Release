# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 11:16
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : pearvideo.py(梨视频)
import json
import re

import scrapy
from scrapy import Spider


class Video_V1(scrapy.Spider):
    name = 'pearvideo'

    allowed_domains = ['www.pearvideo.com']

    # redis_key = 'pearvideo:start_urls'

    start_urls = ['http://www.pearvideo.com/']

    def parse(self, response):

        v1_dict = {
            '娱乐':'4',
            '社会': '1',
            '生活': '5',
            '音乐': '59',
            '体育': '9',
            '科技': '8',
            '动画': '17',
            '创意': '',
        }
        # reqtype 有 14 5
        cy_url  = 'http://www.pearvideo.com/category_loading.jsp?reqType=14&categoryId=&start=12'
        url = "http://www.pearvideo.com/category_loading.jsp?reqType={reqtype}&categoryId={catid}&start={offset}"
        for channel, tag_link in v1_dict.items():
            # type_link = 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=1&start=24'
            for offset in range(0, 480,12):
                if '创意' in channel:
                    type_link = url.format(reqtype=14,catid=tag_link,offset=offset)
                else:
                    type_link = url.format(reqtype=5, catid=tag_link, offset=offset)
                print('type_link >>>> ',channel,type_link)
                yield scrapy.Request(url=type_link, callback=self.get_main_link, meta={'channel': channel},dont_filter=True)


    def get_main_link(self, response):
        node_list = response.xpath("//*[@class='vervideo-bd']")
        for node in node_list:
            a_link = node.xpath("./a/@href").extract_first()
            a_link = response.urljoin(a_link)
            title = node.xpath("./a/div[@class='vervideo-title']/text()").extract_first()
            duration = node.xpath("./a/div[@class='vervideo-img']/div[@class='cm-duration']/text()").extract_first()
            cut_url = node.xpath("./a/div[@class='vervideo-img']/div[@class='verimg-view']/div[@class='img']/@style").extract_first()
            cut_url = re.findall(r'url\((.*?)\);',cut_url)[0]
            authorname = node.xpath("./div[@class='actcont-auto']/a/text()").extract_first()
            print(title,authorname,duration,cut_url)
            if a_link and title:
                yield scrapy.Request(url=a_link,callback=self.parse_detail)

    def parse_detail(self,response):
        print('parse_detail >>>>>  ',response)
        release_time  = response.xpath("//*[@class='brief-box']/div[@class='date']/text()").extract_first()
        print(release_time)
        mp4_source = re.findall(r'srcUrl="(.*?)"',response.body.decode("utf-8"),re.S)[0]
        print(mp4_source)

