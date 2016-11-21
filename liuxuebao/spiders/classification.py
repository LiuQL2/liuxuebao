# -*- coding: utf-8 -*-

import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.http import FormRequest
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from liuxuebao.items import ClassificationItem
import urllib

class MySpider(Spider):
    name = 'classification'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://liuxuebao.com/cn/ajax/Country.ashx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           # 'liuxuebao.pipelines.CourseInfoPipeline': 300,
            # 'liuxuebao.pipelines.CourseInfoImagePipeline':800,
        },
        # 'IMAGES_STORE' : '/Users/Qianlong/Downloads'
        'IMAGES_STORE' : '/Volumes/LiuQL/liuxuebao/images'
    }

    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36",
            }

    def make_requests_from_url(self, url):
        return Request(url = url,headers =self.headers)

    def parse(self, response):
        sel = Selector(response)
        print response.url
        data = json.loads(response.body)
        print data
        # data = get_data
        # country_switch = sel.xpath('//div[@class="country-switch"]/a[@id="J_country_trigger"]/@href').extract()[0]
        # print country_switch
        # yield Request(url = country_switch, method='POST', callback=self.l_get_data, headers=self.headers)
        # print Request(url = country_switch, method='POST', headers=self.headers,)
        formdata = {
            "action":"Bind",
            "region1":"4268",
            "region2":"0",
            "region4":"0",
            "degree":"0",
            "page":"1",
        }
        yield FormRequest.from_response(response, formdata=formdata, method='POST',callback=self.get_ajax)
        # yield Request(url=response.url, method='POST', callback=self.get_ajax, body=urllib.urlencode(formdata))


    def get_ajax(self,response):
        data = json.loads(response.body)
        sel = Selector(response)
        print response.body
        # country_name = sel.xpath('//div[@class="country-switch"]/span[@id="region1Name"]/text()').extract()[0]
        # print 'county_name',country_name,
        # print response['region1List']



