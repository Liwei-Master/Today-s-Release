#!/bin/sh
PATH=/home/admin/anaconda3/bin:/home/admin/bin:/home/admin/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

cd /home/admin/Today-s-Release/spider/News_spider/Daily_crawler/News_data
time=`date "+%Y-%m-%d-%H:%M:%S"`
dirname="news_${time}"
mkdir $dirname
cd $dirname


scrapy crawl zaker     > /home/admin/Today-s-Release/spider/News_spider/log/crawler.log 2>&1
scrapy crawl pengfu   > /home/admin/Today-s-Release/spider/News_spider/log/crawler.log 2>&1
scrapy crawl qctt   > /home/admin/Today-s-Release/spider/News_spider/log/crawler.log 2>&1

