# -*- coding : utf-8 -*-
#闻到 http://wendao123.cn
#采集http://www.ruyile.com网站的山西省小学信息

import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import re
import csv
import datetime

def get_html(url):
    '''
    公共网页请求函数
    :param url: url
    :return: response.text
    '''
    try:
        ua = UserAgent()
        headers = {
            "User-Agent" : ua.random
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return get_html(url)
    except:
        return get_html(url)


def get_page(html):
    '''
    获取页面数
    :param url: 第一面html
    :return: 该市下的小学一共有多少页
    '''
    doc = pq(html)
    page =doc(".zys").text()
    return page

def get_data(link, writer,tag):
    '''
    解析并保存数据
    :param link:
    :param write:
    :param tag:
    :return:
    '''
    html = get_html(link)
    doc = pq(html)
    xx_doc = doc.items(".sk")
    for item in xx_doc:
        #school name
        school_name = item.find("h4").text()
        item = item.text()+'地址'
        # print(item)
        pattern1 = re.compile(r"电话：(.*?) 邮编",re.S)
        phone_number = re.findall(pattern1, item)
        if phone_number:
            phone_number = phone_number[0]
        else:
            phone_number = ''

        pattern2 = re.compile("邮编：(.*?) 地址")
        post = re.findall(pattern2, item)
        if post:
            post = post[0]
        else:
            post = ''
        pattern3 = re.compile("地址：(.*?)地址")
        address = re.findall(pattern3 ,item)
        if address:
            address = address[0]
        else:
            address = ''
        tag = tag

        detail = (school_name, phone_number, post, address, tag)
        writer.writerow(detail)
        print(detail)



if __name__ == "__main__":
    timestart = datetime.datetime.now()
    print("开始采集，当前时间："+timestart.strftime("%Y-%m-%d %H:%M:%S"))
    url = "http://www.ruyile.com/xuexiao/?a={a}&t=2&p={p}"
    shi_dict = {
        '太原市': 84,
        '大同市': 85,
        '阳泉市': 86,
        '长治市': 87,
        '晋城市': 88,
        '朔州市': 89,
        '晋中市': 90,
        '运城市': 91,
        '忻州市': 92,
        '临汾市': 93,
        '吕梁市': 94
    }
    with open('data3.csv', 'a+', encoding='utf-8', newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(('校名', '电话', '邮编', '地址', '所在地区'))
        for tag,a in shi_dict.items():
            html = get_html(url.format(a=a, p=1))
            page = int(get_page(html))
            for p in range(1,page+1):
                urls = url.format(a=a,p=p)
                print("正在抓取"+urls)
                html = get_data(urls, writer, tag)
    timeend = datetime.datetime.now()
    time = timeend - timestart
    print("采集完成，当前时间："+timeend.strftime("%Y-%m-%d %H:%M:%S"))
    print("此次采集共花费："+str(time)+'s')
