# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class SchoolImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    sch_name = scrapy.Field()

class LogoImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    image_names = scrapy.Field()

class CourseImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    course_names = scrapy.Field()
    school_name = scrapy.Field()

class CourseImage2Item(scrapy.Item):
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    course_names = scrapy.Field()
    school_names = scrapy.Field()

class CourseInfoItem(scrapy.Item):
    cors_id = scrapy.Field()
    cors_name = scrapy.Field()#课程中文名
    cors_fname = scrapy.Field()#课程英文名称
    sch_name = scrapy.Field()#所属学校
    image = scrapy.Field()#课程图片位置
    cors_cate_id = scrapy.Field()#课程所属分类
    cors_cate_pid = scrapy.Field()#课程所属大类
    cors_fee = scrapy.Field()#学费,美元
    edu_bkgrd = scrapy.Field()#学历
    span = scrapy.Field()#学制
    enroll_time = scrapy.Field()#入学日期
    app_prblm = scrapy.Field()#申请难度
    lan_reqir = scrapy.Field()#语言要求
    aca_reqir = scrapy.Field()#学术要求
    othr_reqir = scrapy.Field()#其他要求
    material = scrapy.Field()#申请材料清单

class SchoolInfoItem(scrapy.Item):
    sch_id = scrapy.Field()
    sch_name = scrapy.Field()#学校名称
    sch_fname = scrapy.Field()#学校英文名称
    country_id = scrapy.Field()##所属国家
    pro_id = scrapy.Field()#所属省份/区域
    city_id = scrapy.Field()#所属城市
    bache_num = scrapy.Field()#本科课程数目
    master_num = scrapy.Field()#硕士课程数目
    logo = scrapy.Field()#logo图片存储位置
    image = scrapy.Field()#详情页中的多张图片位置
    sch_intro = scrapy.Field()#院校简介
    sch_academic = scrapy.Field()#学术实力
    sch_major = scrapy.Field()#专业优势
    sch_trans = scrapy.Field()#出行交通
    sch_location = scrapy.Field()#地理位置
    sch_tips = scrapy.Field()#申请小贴士
    sch_advice = scrapy.Field()#推荐课程
    urank = scrapy.Field()#USNEWS综合排名
    arank = scrapy.Field()#世界排名


class ClassificationItem(scrapy.Item):
    country = scrapy.Field()
    type_name = scrapy.Field()
    sch_name = scrapy.Field()
    sch_id = scrapy.Field()


