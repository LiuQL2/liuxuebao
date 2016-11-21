# -*- coding: utf-8 -*-
#用来抓取expert的信息,同时expert与circle的信息也利用这个爬虫获取。
#发现如果两个放在一起抓取,可能无法抓取全部信息,如果只是抓取医生的信息,基本上可以全部抓取
import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from liuxuebao.items import LogoImageItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'logo_image'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           # 'liuxuebao.pipelines.LogoImagesPipeline': 300
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
        return Request(url = url, headers =self.headers)

    #获得所有含有学校连接的页面
    def parse(self,response):
        sel = Selector(response)
        for index in range(1, 68,1):
            page_url = 'http://www.liuxuebao.com/cn/search/List.aspx?page=' + str(index)
            print 'page_url',page_url
            yield Request(url=page_url, callback=self.get_school_logo, headers=self.headers)

    #获得所有学校的logo链接
    def get_school_logo(self,response):
        # print '****'
        sel = Selector(response)
        logo_src_content = sel.xpath('//div[@class="school-logo"]/img/@src').extract()
        school_name_content = sel.xpath('//div[@class="list-item-wrap"]//div[@class="school-name"]/a[1]/strong/text()').extract()
        school_course_url_content = sel.xpath('//div[@class="list-item-wrap"]/div/a/@href').extract()#获取每一个学校课程的页面
        item = LogoImageItem()
        item['image_urls'] = []
        item['image_names'] = []
        index = 0
        for logo_url in logo_src_content:
            # school_url = 'http://www.liuxuebao.com/cn/search/'
            logo_url = logo_url.replace('../../', 'http://liuxuebao.com/')
            # print 'logo_url', logo_url
            item['image_urls'].append(logo_url)
            item['image_names'].append(school_name_content[index])
            print 'http://liuxuebao.com/cn/search/' + school_course_url_content[index]
            index = index + 1

        return item