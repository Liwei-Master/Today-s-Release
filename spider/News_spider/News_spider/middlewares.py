# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from News_spider.settings import USER_AGENT_LIST as user_list

class UserAgentMiddleware(object):

    def process_request(self, request, spider):
        """给每一个请求换一个user_agent"""
        user_agent = random.choice(user_list)
        request.headers["User_Agent"] = user_agent
