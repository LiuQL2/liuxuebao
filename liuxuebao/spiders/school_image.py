# -*- coding: utf-8 -*-
import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from liuxuebao.items import SchoolImageItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'school_image'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           'liuxuebao.pipelines.SchoolImagesPipeline': 300
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
            yield Request(url=page_url, callback=self.get_school_url, headers=self.headers)

    #获得所有学校的主页链接
    def get_school_url(self,response):
        print '****'
        sel = Selector(response)
        school_content = sel.xpath('//div[@class="list-item-wrap"]//div[@class="school-name"]/a[1]/@href').extract()
        for school_url in school_content:
            school_url = 'http://www.liuxuebao.com/cn/search/' + school_url
            print 'school_url', school_url
            yield Request(url=school_url, callback=self.get_school_images, headers=self.headers)

    #获得每一个学校的所有图片
    def get_school_images(self, response):
        sel = Selector(response)
        content = sel.xpath('//ul[@id="J_spec_list_panel"]/li/img/@src').extract()

        item = SchoolImageItem()
        item['image_urls'] = []
        school_name = (sel.xpath('//head/meta[4]/@content').extract()[0]).split('/')[0]
        item['sch_name'] = school_name
        for image_url in content:
            image_url = image_url.replace('../../', 'http://liuxuebao.com/')#构造照片的地址链接
            # print image_url
            item['image_urls'].append(image_url)
        print item['sch_name']
        print '####',item['image_urls']

        return item
