# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 10:00
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : qncye.py(青年创业网)
import re

import scrapy


class QingNianCYeSpider(scrapy.Spider):
    pass
    #
    # name = 'qncye'
    #
    # allowed_domains = ['www.qncye.com']
    # # https: // www.pengfu.com / content_1815933_1.html
    # start_urls = ['http://www.qncye.com/data/sitemap.html']
    #
    # def parse(self, response):
    #     site_link = response.xpath("//*[@class='linkbox']")
    #     print(site_link)
    #     per_link = 'http://www.qncye.com/baodao/keji/'
    #     if per_link:
    #         yield scrapy.Request(url=per_link, callback=self.parse_list)
    #     # for link in site_link:
    #     #     ul_links = link.xpath("./ul[@class='f6']/li")
    #     #     for u_link in ul_links:
    #     #         per_link = response.urljoin(u_link.xpath("./a/@href").extract_first())
    #     #         channel = u_link.xpath("./a/text()").extract_first()
    #     #         print('link ==== ',response.urljoin(per_link),channel)
    #     #         if per_link:
    #     #             yield scrapy.Request(url=per_link,callback=self.parse_list)
    #
    # def parse_list(self,response):
    #     print('parse_list ',response)
    #     link = 'http://www.qncye.com/zhishiku/renli/021032045.html'
    #     yield scrapy.Request(url=link, callback=self.parse_detail)
    #     # article_list = response.xpath("//*[@class='ptb25']")
    #     # for article in article_list:
    #     #     link = article.xpath("./div[@class='clearfix']/div/h3[@class='fz18 YaHei fbold']/a/@href").extract_first()
    #     #     title = article.xpath("./div[@class='clearfix']/div/h3[@class='fz18 YaHei fbold']/a/@title").extract_first()
    #     #     time = article.xpath("./div[@class='clearfix']/div/div[@class='txtBox']/div[@class='txt']/p/span/text()").extract_first()
    #     #     link = response.urljoin(link)
    #     #     link = 'http://www.qncye.com/baodao/lingxiu/041633080.html'
    #     #     if title and link:
    #     #         print('link ',link,'title ',title,time)
    #     #         yield scrapy.Request(url=link,callback=self.parse_detail)
    #
    # def parse_detail(self,response):
    #     print('parse_detail ',response)
    #     item = NewsItem()
    #     content = response.xpath("//*[@id='ctrlfscont']").extract_first()
    #     content = Util.remove_impurity(content)
    #     content = Util.replace_style(content)
    #
    #     image_urls = re.findall(r'src="(.*?)"', content)
    #
    #     for v_image in image_urls:
    #         t_image = Util.generate_pic_time(v_image)
    #         content = content.replace(v_image, t_image)
    #     item['body'] = content
    #     try:
    #         item['images'] = []
    #         item['image_urls'] = []
    #         for num, image_url in enumerate(image_urls):
    #             t_image = Util.generate_pic_time(image_url)
    #             temp_image_url = Util.generate_pic_time(t_image)
    #             image_dict = {"index": num, "url": temp_image_url, "title": ""}
    #             item['images'].append(image_dict)
    #             item['image_urls'].append(response.urljoin(image_url))
    #
    #     except:
    #         item["image_urls"] = []
    #         item['images'] = []
    #
    #     item_id = Util.to_md5(title)
    #     item['item_id'] = item_id
    #     item['item_type'] = 'ARTICLE'
    #     # 原创还是转载，
    #     item['create_type'] = ''
    #     item['source'] = '捧腹网'
    #     item['original_url'] = response.url
    #     janesi_time = Util.local_time()
    #     item['avatar'] = ''
    #     item['type'] = 0
    #     item['fans_count'] = ''
    #     item['scan_count'] = ''
    #     item['collect_count'] = ''
    #     item['is_delete'] = '0'
    #     item['gmt_create'] = janesi_time
    #     item['gmt_modified'] = janesi_time
    #     item['author'] = {'name': name, 'avatar': '', 'platform': 'jiemian', 'type': '0', 'fans_count': '',
    #                       'scan_count': '', 'collect_count': '', 'is_delete': '0', 'gmt_create': janesi_time,
    #                       'gmt_modified': janesi_time}
    #
    #     item['category'] = {"channel": '搞笑', "child_channel": '', "topic": [], "tag": ['搞笑'], "keyword": [],
    #                         "region": ''}
    #
    #     item['tag'] = ['搞笑']
    #     item['channel'] = '搞笑'
    #     item['child_channel'] = ''
    #     item['topic'] = []
    #     item['keyword'] = []
    #     item['region'] = ''
    #
    #     item["videos"] = []
    #     item["audios"] = []
    #     item['videos'] = []
    #     item['audios'] = []
    #     item['copyright'] = ''
    #     item['release_time'] = janesi_time
    #     item['janesi_time'] = janesi_time
    #     item['scan'] = Util.random_number()
    #     item['like'] = 0
    #     item['share'] = 0
    #     item['play'] = 0
    #     item['forward'] = 0
    #     item['collect'] = 0
    #     item['upload_file_flag'] = 'true'
    #     item['platform'] = 'pengfu'
    #     if content:
    #         check = Util.check_item(item)
    #         if check == 1:
    #             return
    #         yield item
    #     else:
    #         print('-----------  pengfu  parse  error --------')
