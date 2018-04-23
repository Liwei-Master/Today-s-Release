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
    """
    MYSQL_HOST
    MYSQL_DBNAME
    MYSQL_USER
    MYSQL_PASSWD
    """

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host=settings.MYSQL_HOST, port=3306, db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWD, charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""insert into display_item (item_id, item_title, item_type ,item_source,title_link, cut_url,collect_time ,category,author)
                value (%s, %s, %s, %s, %s,%s, %s,%s,%s)""",
                (item['item_id'], item['item_title'], item['item_type'], item['item_source'],item['title_link'], item['cut_url'], item['collect_time'],item['category'],item['author']))
            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print('db insert error  ', error)
        return item
