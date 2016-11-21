# -*- coding: utf-8 -*-
#用来抓取课程的信息,里面可以同时下载照片,看看哪一种方法比较完整
import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from liuxuebao.items import CourseInfoItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'course_info'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           'liuxuebao.pipelines.CourseInfoPipeline': 300,
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
            yield Request(url=url, callback=self.get_course_url, headers=self.headers)

    #获得课程的主页链接
    def get_course_url(self,response):
        sel = Selector(response)
        course_url_content = sel.xpath('//div[@class="item-list"]/div[@class="item-col"]/div[@class="item-name"]/a/@href').extract()
        for url in course_url_content:
            course_url = 'http://liuxuebao.com/cn/search/' + url
            yield Request(url=course_url, meta={'course_url':course_url},callback=self.get_course_info, headers=self.headers)

    def get_course_info(self, response):
        sel = Selector(response)
        item = CourseInfoItem()
        item['cors_id'] = response.meta['course_url']
        item['cors_name'] = sel.xpath('//div[@class="dc-info-name"]/h2/text()').extract()[0]
        item['cors_fname'] = sel.xpath('//div[@class="dc-info-name"]/h3/text()').extract()[0]
        item['sch_name'] = sel.xpath('//div[@class="dc-info-name"]/a/p/text()').extract()[0]
        item['image'] = 'images/course/'+ item['sch_name'] + '/' + item['cors_name']
        # item['image'] = sel.xpath('//div[@class="dc-preview"]/img/@src').extract()[0].replace('../../','http://liuxuebao.com/')
        cate_id = sel.xpath('//ul[@class="dc-course-info clearfix"]/li[3]/text()').extract()[0]
        cate_id = cate_id.split('：')[1]
        item['cors_cate_id'] = cate_id.split(' ')[1]
        item['cors_cate_pid'] = cate_id.split(' ')[0]
        item['cors_fee'] = (sel.xpath('//ul[@class="dc-course-info clearfix"]/li[7]/text()').extract()[0]).split('：')[1].split('/')[0]
        item['edu_bkgrd'] = (sel.xpath('//ul[@class="dc-course-info clearfix"]/li[4]/text()').extract()[0]).split('：')[1]
        item['span'] = (sel.xpath('//ul[@class="dc-course-info clearfix"]/li[5]/text()').extract()[0]).split('：')[1]
        item['enroll_time'] = (sel.xpath('//ul[@class="dc-course-info clearfix"]/li[6]/text()').extract()[0]).split('：')[1]
        item['app_prblm'] = (sel.xpath('//ul[@class="dc-course-info clearfix"]/li[8]/span/@class').extract()[0])[-1]
        item['lan_reqir'] = sel.xpath('//div[@id="J_floor_request"]/div[@class="ds-main-panel-inner"]/div[1]/text()').extract()[0].replace('\r\n\t\t\t\t\t\t\t\t\t','').replace('\r\n\t\t\t\t\t\t\t\t','')
        item['aca_reqir'] = sel.xpath('//div[@id="J_floor_request"]/div[@class="ds-main-panel-inner"]/div[2]/text()').extract()[0].replace('\r\n\t\t\t\t\t\t\t\t\t','').replace('\r\n\t\t\t\t\t\t\t\t','')
        item['othr_reqir'] = sel.xpath('//div[@id="J_floor_request"]/div[@class="ds-main-panel-inner"]/div[3]/text()').extract()[0].replace('\r\n\t\t\t\t\t\t\t\t\t','').replace('\r\n\t\t\t\t\t\t\t\t','')
        material_content= sel.xpath('//div[@id="J_floor_materials"]/div[@class="ds-main-panel-inner"]/div/text()').extract()
        item['material']=''
        for material in material_content:
            item['material'] = item['material'] + '##' + material.replace('\r\n                                ', '').replace('\r\n\t\t\t\t\t\t\t\t','')


        print '***********'
        print item['cors_id']
        print item['cors_name']
        print item['cors_fname']
        print item['sch_name']
        print item['image']
        print item['cors_cate_id']
        print item['cors_cate_pid']
        print item['cors_fee']
        print item['edu_bkgrd']
        print item['span']
        print item['enroll_time']
        print item['app_prblm']
        print 'lan_reqir',item['lan_reqir']
        print 'aca_reqir',item['aca_reqir']
        print 'othr_reqir',item['othr_reqir']
        print item['material']
        return item






