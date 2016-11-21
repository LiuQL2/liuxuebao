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
from liuxuebao.items import CourseImage2Item
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'course_image2'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/index.aspx?CountryId=0&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&keyword=&type=1&schoolId=0&IsSchool=0&SchoolName=&SchoolTypeId=0&SchoolSortId=0&page=1']
    custom_settings = {
        'ITEM_PIPELINES' : {
           'liuxuebao.pipelines.CourseImages2Pipeline': 300
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
        for index in range(1, 6970,1):
            page_url = 'http://www.liuxuebao.com/cn/search/index.aspx?CountryId=0&AreaId=0&DegreeId=0&FacultyTypeId=0&FacultyId=0&HotAreaId=0&keyword=&type=1&schoolId=0&IsSchool=0&SchoolName=&SchoolTypeId=0&SchoolSortId=0&page=' + str(index)
            # print 'page_url',page_url
            yield Request(url=page_url, callback=self.get_course_image, headers=self.headers)

    def get_course_image(self, response):
        print '#####'
        sel = Selector(response)
        src_content = sel.xpath('//div[@class="container"]/div[@class="clearfix"]/div/div[@class="item-img"]/a/img/@src').extract()
        school_name_content = sel.xpath('//div[@class="container"]/div[@class="clearfix"]/div/div[@class="item-ft"]/p/text()').extract()
        course_name_content = sel.xpath('//div[@class="container"]/div[@class="clearfix"]/div/div[@class="item-ft"]/a/p/text()').extract()

        index = 0
        item = CourseImage2Item()
        item['image_urls'] = []
        item['school_names'] = []
        item['course_names'] = []
        for src in src_content:
            image_src = src.replace('../../', 'http://www.liuxuebao.com/')#构造照片的地址链接
            item['image_urls'].append(image_src)
            item['school_names'].append(school_name_content[index])
            item['course_names'].append(course_name_content[index])
        return item


