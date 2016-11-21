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
from liuxuebao.items import CourseImageItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'course_image'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           # 'liuxuebao.pipelines.CourseImagesPipeline': 300
           'liuxuebao.pipelines.CourseImages3Pipeline': 300
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

    #获得所有学校的课程信息页面链接
    def get_school_url(self,response):
        sel = Selector(response)
        school_course_url_content = sel.xpath('//div[@class="list-item-wrap"]/div/a/@href').extract()#获取每一个学校课程的页面
        for url in school_course_url_content:
            url = 'http://www.liuxuebao.com/cn/search/' + url
            # print '****','school_course_url', url
            yield Request(url=url, callback=self.get_course_images, headers=self.headers)

    #获得每一个学校的所有课程图片
    def get_course_images(self, response):
        sel = Selector(response)
        src_content = sel.xpath('//div[@class="item-list"]/div[@class="item-img"]/a/img/@src').extract()#所有课程的图片的src
        school_name = (sel.xpath('//div[@class="school-name"]/a/strong/text()').extract()[0])#学校的名称
        course_name_content = sel.xpath('//div[@class="item-list"]/div[@class="item-col"]/div[@class="item-name"]/a/h3[1]/text()').extract()#学校所有课程的名称

        index = 0
        # item = CourseImageItem()
        # item['image_urls'] = []
        # item['course_names'] = []
        # item['school_name'] = school_name

        # #将课程图片链接,课程名称放入item
        # for image_url in src_content:
        #     image_url = image_url.replace('../../', 'http://www.liuxuebao.com/')#构造照片的地址链接
        #     # 'http://www.liuxuebao.com/upload/course_info/%E8%8B%B1%E5%9B%BD%20(128).jpg'
        #     # print image_url
        #     item['image_urls'].append(image_url)
        #     item['course_names'].append(course_name_content[index])
        #     index = index + 1
        #
        # print len(item['image_urls']),item['image_urls']
        # # print item['course_names']
        # return item
        # print '###', len(src_content)
        index = 0
        for image_url in src_content:
            item = CourseImageItem()
            image_url = image_url.replace('../../', 'http://www.liuxuebao.com/')#构造照片的地址链接
            # 'http://www.liuxuebao.com/upload/course_info/%E8%8B%B1%E5%9B%BD%20(128).jpg'
            # print image_url
            item['image_urls']=image_url
            item['school_name'] = school_name
            item['course_names']=course_name_content[index]
            print '###', len(src_content), index, item['school_name'], item['course_names'], item['image_urls']
            yield Request(url=image_url, callback=self.return_item,meta={'item':item} ,headers=self.headers)
            index = index + 1

    def return_item(self, response):
        return response.meta['item']


