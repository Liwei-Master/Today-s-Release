#! /bin/sh

cd /home/admin/Today-s-Release/spider/News_spider/log
now_time=`date "+%Y-%m-%d-%H:%M:%S"`
echo $now_time>>run_time.txt
time -a -o run_time.txt /home/admin/Today-s-Release/spider/News_spider/Daily_crawler/news_crawl.sh

