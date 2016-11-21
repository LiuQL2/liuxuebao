#coding:utf-8
import re
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import math
import random
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DoctorZixunSpider(Spider):

    name = 'recipe'
    allowed_domains = ["haodf.com"]
    start_urls=['http://wxinhua.haodf.com/zixun/list.htm',
                'http://doctorhaosuzhou.haodf.com/zixun/list.htm',
                'http://postone.haodf.com/zixun/list.htm']
    custom_settings = {
        'ITEM_PIPELINES' : {
            # 'yuanyuan.pipelines.RecipePipeline': 300
        }
    }
    # start_urls = []
    # doctor_url_file = open('/Users/Qianlong/Desktop/eHealth/haodaifu/doctorUrl.csv', 'r')
    # reader = csv.reader(doctor_url_file)
    # for url in reader:
    #     print '\''+ url[0] + '\','
    #     start_urls.append(url[0])
    # doctor_url_file.close()

    def make_requests_from_url(self, url):
        return Request(url = url)

    def parse(self, response):
        sel = Selector(response)
        page_number_content = sel.xpath('//div[@class="page_turn"]/a[@rel="true"][2]/text()').extract()
        if len(page_number_content) == 1:
            mode = re.compile(r'\d+')
            page_number = int(mode.findall(page_number_content[0])[0]) + 1
        else:
            page_number = 2

        # url_format = sel.xpath('//ul[@class="clearfix f16"]/li[1]/a/@href').extract()[0] + 'zixun/list.htm?type=&p='
        url_format = sel.xpath('//a[@class="choiced"]/@href').extract()[0] + '?type=&p='
        for index in range(1, page_number,1):
            url = url_format + str(index)
            print '*****',url