# -*- coding: utf-8 -*-

import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.http import FormRequest
from liuxuebao.items import ClassificationItem
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Classification(Spider):
    name = 'classification2'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=4267&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=4268&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=4269&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=5530&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=5531&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=5937&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=5988&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=',
                  'http://www.liuxuebao.com/cn/search/List.aspx?&CountryId=5989&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&Keyword=&type=0&SchoolTypeId=0&SchoolSortId=0&schoolId=0&IsSchool=0&SchoolName=']
    custom_settings = {
        'ITEM_PIPELINES' : {
           'liuxuebao.pipelines.ClassificationPipeline': 300,
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
        return Request(url = url, headers =self.headers)

    #获得所有含有学校连接的页面
    def parse(self,response):
        sel = Selector(response)
        type_url_list = sel.xpath('//div[@id="SearchPanel11_divSchoolType"]//ul[@class="trigger-list clearfix"]/li/a/@href').extract()
        type_name_list = sel.xpath('//div[@id="SearchPanel11_divSchoolType"]//ul[@class="trigger-list clearfix"]/li/a/text()').extract()
        country = sel.xpath('//div[@class=""]//ul[@class="trigger-list clearfix"]/li[@class="current"]/a/text()').extract()[0]
        index = 0
        for type_url in type_url_list:
            url = 'http://www.liuxuebao.com' + type_url
            print 'country:', country, 'type:', type_name_list[index], url
            yield Request(url=url, meta={'country':country,'type':type_name_list[index]},callback=self.get_page_url, headers=self.headers)
            index = index + 1

    def get_page_url(self, response):
        sel = Selector(response)
        page_number_content = sel.xpath('//div[@id="AspNetPager1"]/a/@href').extract()

        if len(page_number_content) >= 1:
            page_number = int(page_number_content[len(page_number_content) - 1].split('&page=')[1])

        else:
            page_number = 1
        country = response.meta['country']
        type = response.meta['type']
        print country, type, page_number
        for index in range(1, page_number + 1, 1):
            page_url = response.url + '&page=' + str(index)
            print country, type, index, page_url
            yield Request(url = page_url, meta={'country':country, 'type':type},callback=self.get_school, headers=self.headers)

    def get_school(self,response):
        sel = Selector(response)
        school_url_list = sel.xpath('//div[@class="list-item-wrap"]//div[@class="school-name"]/a[1]/@href').extract()
        school_name_list = sel.xpath('//div[@class="list-item-wrap"]//div[@class="school-name"]/a[1]/strong/text()').extract()
        #http://www.liuxuebao.com/cn/
        index = 0
        for url in school_url_list:
            item = ClassificationItem()
            url = 'http://www.liuxuebao.com/cn/search/' + url
            name = school_name_list[index]
            index = index + 1
            item['country'] = response.meta['country'].split('(')[0]
            item['type_name'] = response.meta['type'].split('(')[0]
            item['sch_name'] = name
            item['sch_id'] = url
            print '#############'
            print item['country']
            print item['type_name']
            print item['sch_name']
            print item['sch_id']
            yield  Request(url = url, meta={'item':item}, callback=self.return_item, headers=self.headers)
            print '$$$$$'

    def return_item(self,response):#无法进入该函数
        item = response.meta['item']
        print '*********', item['sch_name']
        return item

