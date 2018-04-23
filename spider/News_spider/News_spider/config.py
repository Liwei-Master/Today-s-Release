# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 11:55
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : config.py.py

class serviceConfig():

    @classmethod
    def test_config(self):
        mysql_list = {
            'MYSQL_HOST':'118.25.0.58',
            'MYSQL_DBNAME':'janesi-interest',
            'MYSQL_USER':'janesi_all',
            'MYSQL_PASSWD':'MyLBdwW13I83sygn',
            'MYSQL_PORT':'3306'
        }
        mongo_list = {
            'MONGO_URL':'111.231.75.58',
            'MONGO_USER':'',
            'MONGO_PWD':'',
            'MONGO_PORT':271017,
            'MONGO_HOST':'111.231.75.58',
            'MONGO_DB':'news',
            'MONGO_COLL':'article',
        }
        redis_list = {
            'REDIS_HOST':'118.25.0.190',
            'REDIS_PARAMS':"{'password': 'MyLBdwW13I83sygn'}",
        }
        cos_list = {
            'bucket_name':'matrix-dev'
        }
        es_list = {
            'es_url':'http://118.25.10.151'
        }
        j_list = {
            'mysql_list':mysql_list,
            'mongo_list':mongo_list,
            'redis_list':redis_list,
            'cos_list':cos_list,
            'es_list':es_list,
        }
        return [j_list]