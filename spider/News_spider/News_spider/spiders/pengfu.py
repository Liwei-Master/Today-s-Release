# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 10:48
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : pengfu.py.py
import re

import scrapy


class PengfuSpider(scrapy.Spider):
    pass

    # name = 'pengfu'
    #
    # allowed_domains = ['www.pengfu.com']
    # # https: // www.pengfu.com / content_1815933_1.html
    # start_urls = ['http://www.pengfu.com']
    #
    # def parse(self, response):
    #     url = "https://www.pengfu.com/index_1.html"
    #     for pagesize in range(1,15):
    #         url = "https://www.pengfu.com/index_{}.html".format(str(pagesize))
    #         print('parse url ==   ',url)
    #         yield scrapy.Request(url=url,callback=self.parse_list)
    #
    # def parse_list(self,response):
    #     node_list = response.xpath("//*[@class='list-item bg1 b1 boxshadow']")
    #     for v_node in node_list:
    #         author_name = v_node.xpath("./dl[@class='clearfix dl-con']/dd/p[@class='user_name_list']/a/text()").extract_first()
    #         title = v_node.xpath("./dl[@class='clearfix dl-con']/dd/h1[@class='dp-b']/a/text()").extract_first()
    #         title_link = v_node.xpath("./dl[@class='clearfix dl-con']/dd/h1[@class='dp-b']/a/@href").extract_first()
    #         if title_link:
    #             yield scrapy.Request(url=title_link,callback=self.parse_detail)

    # def parse_detail(self,response):
    #     item = ()
    #     print('parse_detail >>>>>>  ')
    #     content = response.xpath("//*[@class='content-txt pt10']").extract_first()
    #     if 'type="video/mp4"' in content:
    #         return
    #
    #     # 替换src
    #     content = MyUtils.Util.remove_impurity(content)
    #     content = MyUtils.Util.replace_style(content)
    #
    #     image_urls = re.findall(r'src="(.*?)"', content)
    #
    #     for v_image in image_urls:
    #         t_image = Util.generate_pic_time(v_image)
    #         content = content.replace(v_image, t_image)
    #     f_content = content
    #     print('f_content  ',f_content)
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
    #         image_url_with_http = []
    #         for num, image_url in enumerate(image_urls):
    #             t_image = Util.generate_pic_time(image_url)
    #             temp_image_url = Util.generate_pic_time(t_image)
    #             image_dict = {"index": num, "url": temp_image_url, "title": ""}
    #             item['images'].append(image_dict)
    #
    #             item['image_urls'].append(response.urljoin(image))
    #             if 'http' not in image_url:
    #                 image_url_with_http.append(response.urljoin(image_url))
    #             else:
    #                 image_url_with_http.append(image_url)
    #             item['image_urls'] = image_url_with_http
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
    #     item['scan'] =  Util.random_number()
    #     item['like'] = 0
    #     item['share'] = 0
    #     item['play'] = 0
    #     item['forward'] = 0
    #     item['collect'] = 0
    #     item['upload_file_flag'] = 'true'
    #     item['platform'] = 'pengfu'
    #     if  content:
    #         check = Util.check_item(item)
    #         if check == 1:
    #             return
    #         yield item
    #     else:
    #         # print('-----------  pengfu  parse  error --------')