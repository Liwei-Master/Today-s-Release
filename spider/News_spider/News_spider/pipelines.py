# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql

from News_spider import settings


class NewsSpiderPipeline(object):
    def open_spider(self, spider):
        self.filename = open('newsdata.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + "\n"
        self.filename.write(content.encode('utf-8').decode('unicode-escape'))
        return item

    def close_spider(self, spider):
        self.filename.close()


class DBPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host=settings.MYSQL_HOST, port=3306, db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWD, charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute("""select * from doubanmovie where img_url = %s""", item['img_url'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass

            else:
                # 插入数据
                self.cursor.execute("""insert into doubanmovie(name, info, rating, num ,quote, img_url)
                    value (%s, %s, %s, %s, %s, %s)""",
                    (item['name'], item['info'], item['rating'], item['num'], item['quote'], item['img_url']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print('db insert error  ', error)
        return item
