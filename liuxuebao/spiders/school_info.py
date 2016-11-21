# -*- coding: utf-8 -*-
import re
import math
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from liuxuebao.items import SchoolInfoItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ExpertSpider(Spider):
    name = 'school_info'
    allowed_domains = ['liuxuebao.com']
    start_urls = ['http://www.liuxuebao.com/cn/search/List.aspx']
    custom_settings = {
        'ITEM_PIPELINES' : {
           # 'liuxuebao.pipelines.SchoolInfoPipeline': 300
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
        school_city_content = sel.xpath('//div[@class="list-item-wrap"]//div[@class="school-name"]/a[2]/text()[2]').extract()
        print len(school_city_content),school_city_content
        index = 0
        school_url_list = ['http://liuxuebao.com/cn/search/detail-school.aspx?id=1564',
                           'http://www.liuxuebao.com/cn/search/detail-school.aspx?id=1636',
                           'http://www.liuxuebao.com/cn/search/detail-school.aspx?id=1637',
                           'http://www.liuxuebao.com/cn/search/detail-school.aspx?id=1578']

        for school_url in school_content:
            school_url = 'http://www.liuxuebao.com/cn/search/' + school_url
            school_city = (school_city_content[index]).replace('\r\n                                        ','#')
            print school_city
            school_city = school_city.split('#')[1].replace('  ','')
            print 'school_url', school_url, school_city
            yield Request(url=school_url, meta={'school_city':school_city,'url':school_url},callback=self.get_school_images, headers=self.headers)
            index = index + 1


    #获得每一个学校的所有图片
    def get_school_images(self, response):
        sel = Selector(response)
        mode = re.compile(r'\d+')#构造提取数字的正则表达式
        image_src_content = sel.xpath('//ul[@id="J_spec_list_panel"]/li/img/@src').extract()

        item = SchoolInfoItem()
        item['sch_id'] = response.meta['url']
        item['sch_name'] = sel.xpath('//div[@class="school-info"]/h3/text()').extract()[0]
        item['sch_fname'] = sel.xpath('//div[@class="school-info"]/h4/text()').extract()[0]
        # print sel.xpath('//div[@class="school-info"]/p/text()').extract()[0]
        item['country_id'] = (sel.xpath('//div[@class="school-info"]/p/text()').extract()[0]).split(' ')[0]
        item['pro_id'] = sel.xpath('//div[@class="school-info"]/p/text()').extract()[0].split(' ')[1]
        item['city_id'] = response.meta['school_city']
        item['bache_num'] = mode.findall(sel.xpath('//ul[@class="info-row2 clearfix"]/li[1]/text()').extract()[0])[0]
        item['master_num'] = mode.findall(sel.xpath('//ul[@class="info-row2 clearfix"]/li[2]/text()').extract()[0])[0]
        item['logo'] = 'images/logo/' + item['sch_name']+'.jpg'
        item['image'] = 'images/shcool_cover/'

        if len(sel.xpath('//div[@class="ds-about-article"][1]/p/text()').extract())==0:
            sch_intro_content = sel.xpath('//div[@class="ds-about-article"][1]/text()').extract()
            # print sch_intro_content
            item['sch_intro'] = ''
            for intro in sch_intro_content:
                item['sch_intro'] = item['sch_intro'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'
        else:
            item['sch_intro'] = sel.xpath('//div[@class="ds-about-article"][1]/p/text()').extract()[0]


        sch_academic_content = sel.xpath('//div[@class="ds-about-article"][2]/text()').extract()
        item['sch_academic'] = ''
        for intro in sch_academic_content:
            item['sch_academic'] = item['sch_academic'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        sch_major_content = sel.xpath('//div[@class="ds-about-article"][3]/text()').extract()
        item['sch_major'] = ''
        for intro in sch_major_content:
            item['sch_major'] = item['sch_major'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        sch_trans_content = sel.xpath('//div[@class="ds-about-article"][4]/text()').extract()
        item['sch_trans'] = ''
        for intro in sch_trans_content:
            item['sch_trans'] = item['sch_trans'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        sch_location_content = sel.xpath('//div[@class="ds-about-article"][5]/text()').extract()
        item['sch_location'] = ''
        for intro in sch_location_content:
            item['sch_location'] = item['sch_location'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        sch_tips_content = sel.xpath('//div[@class="ds-about-article"][4]/text()').extract()
        item['sch_tips'] = ''
        for intro in sch_tips_content:
            item['sch_tips'] = item['sch_tips'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        sch_advice_content = sel.xpath('//div[@class="ds-recommend"]/ul/li/a/text()').extract()
        item['sch_advice'] = ''
        for intro in sch_advice_content:
            item['sch_advice'] = item['sch_advice'] + (intro.replace('\r\n\t\t\t\t\t\t    ','')).replace('\r\n\t\t\t\t\t    ','') + '##'

        # item['sch_advice'] = sel.xpath('//div[@class="ds-recommend"]/ul/li/a/@href').extract()#存网址

        item['urank'] = sel.xpath('//ul[@class="ds-preview-flag"]/li[1]/span/text()').extract()[0]

        arank = sel.xpath('//ul[@class="ds-preview-flag"]/li[2]/span/text()').extract()
        if len(arank) == 0:
            item['arank'] = ''
        else:
            item['arank'] = arank[0]
        # item['image_urls'] = []
        # for image_url in image_src_content:
        #     image_url = image_url.replace('../../', 'http://liuxuebao.com/')#构造照片的地址链接
        #     # print image_url
        #     item['image_urls'].append(image_url)
        print item['sch_id']
        print item['sch_name']
        print item['sch_fname']
        print item['country_id']
        print item['pro_id']
        print item['city_id']
        print item['bache_num']
        print item['master_num']
        print item['sch_intro']
        print item['sch_academic']
        print item['sch_major']
        print item['sch_trans']
        print item['sch_location']
        print item['sch_tips']
        print item['sch_advice']
        print item['urank']
        print item['arank']
        # print item['sch_tips']
        return item
