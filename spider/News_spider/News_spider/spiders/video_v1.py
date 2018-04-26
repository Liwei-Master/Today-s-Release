# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 11:26
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : video_v1.py(http://www.v1.cn/ 第一视频)
import json
import re

import scrapy
from scrapy import Spider
from scrapy_redis.spiders import RedisSpider


class Video_V1(scrapy.Spider):
    name = 'video_v1'

    allowed_domains = ['www.v1.cn']

    # redis_key = 'video_v1:start_urls'

    start_urls = ['http://www.v1.cn/']

    def parse(self, response):

        v1_dict = {
            '新闻':'xinwen',
            '娱乐':'yule',
            '搞笑': 'gaoxiao',
            '旅游': 'lvyou',
            '财经': 'caijing',
            '美食': 'meishi',
            '汽车': 'qiche',
            '社会': 'shehui',
            '原创': 'yuanchuang',
            '两性': 'liangxing', }
        for channel, tag_link in v1_dict.items():
            type_link = 'http://www.v1.cn/{}/'.format(tag_link)
            yield scrapy.Request(url=type_link, callback=self.get_main_link, meta={'channel': channel},dont_filter=True)


    def get_main_link(self, response):

        for pageindex in range(1,2):
            if int(pageindex) == 1:
                # 解析Html
                yield scrapy.Request(url=response.url,callback=self.parse_first_html,meta={'item':item},dont_filter=True)
            else:
                # # 更多的数据查找
                cid = re.findall(r'id="cid" value="(.*?)"', response.body.decode("utf-8"), re.S)[0]
                # print('cid ', cid)
                main_link = 'http://www.v1.cn/index/getList4Ajax'
                for page in range(1, 30):
                    formdata = {'cid': str(cid), 'page': str(page)}
                    yield scrapy.FormRequest(url=main_link, formdata=formdata, callback=self.get_list_res,meta={'item':item})


    def parse_first_html(self,response):
        item = response.meta['item']
        # print('parse_first_html', response)
        # 当前页面视频
        video_list = response.xpath("//*[@class='infoList']/li")
        # print('video_list  ', len(video_list))

        for video in video_list:
            duration = video.xpath("./div[@class='pic']/span[@class='tipTime']/text()").extract_first()
            # print('时长：',tip_time)
            title = video.xpath("./div[@class='tit']/a/text()").extract_first()
            _author = video.xpath("./div[@class='uploadUser']/p/text()").extract_first()
            author = '第一视频'

            if _author:
                author = _author

            scan = video.xpath("./span[@class='icoPv']/text()").extract_first()
            cut_url = video.xpath("./div[@class='pic']/a/img/@src").extract_first()

            next_link = video.xpath("./div[@class='pic']/a/@href").extract_first()
            print('时长：'+duration,'标题：',title,"作者：",author,'阅读量：',scan,'第一帧：',cut_url,'链接：',next_link)
            new_next_url = response.urljoin(next_link)





