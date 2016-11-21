# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv
import codecs
import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

#保存图片的,对应school_iamges
class SchoolImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        index = 1
        for image_url in item['image_urls']:
            # print '****', image_url
            # yield Request(image_url)
            yield Request(image_url,meta={'image_name':item['sch_name'] + '_' + str(index) + '.jpg'})#调用函数获取图片信息
            index = index + 1

    #返回item
    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        return 'school_cover/'+'%s' % (image_guid)


#保存图片的,对应logo_iamges
class LogoImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        index = 0
        for image_url in item['image_urls']:
            print '****', image_url
            # yield Request(image_url)
            yield Request(image_url,meta={'image_name':(item['image_names'])[index] + '.jpg'})#调用函数获取图片信息
            index = index + 1

    #返回item
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        return 'logo/'+'%s' % (image_guid)

#保存课程图片,对应course_image
class CourseImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        index = 0
        for image_url in item['image_urls']:
            # yield Request(image_url)
            # yield Request(image_url,meta={'school_name':item['school_name'],'image_name':item['school_name'] + '_' + (item['course_names'])[index] + '.jpg'})#调用函数获取图片信息。图片名称包含学校
            yield Request(image_url,meta={'school_name':item['school_name'],'image_name':(item['course_names'])[index] + '.jpg'})#调用函数获取图片信息,图片名称不包含学校
            index = index + 1

    #返回item
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        school_name = request.meta['school_name']
        return 'course/' + school_name + '/'+'%s' % (image_guid)



#保存课程图片,对应course_image
class CourseImages2Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        index = 0
        for image_url in item['image_urls']:
            # yield Request(image_url)
            # yield Request(image_url,meta={'school_name':item['school_name'],'image_name':item['school_name'] + '_' + (item['course_names'])[index] + '.jpg'})#调用函数获取图片信息。图片名称包含学校
            yield Request(image_url,meta={'school_name':(item['school_names'])[index],'image_name':(item['course_names'])[index] + '.jpg'})#调用函数获取图片信息,图片名称不包含学校
            index = index + 1

    #返回item
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        school_name = request.meta['school_name']
        return 'course/' + school_name + '/'+'%s' % (image_guid)


class CourseImages3Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(url=item['image_urls'],meta={'school_name':item['school_name'],'image_name':item['course_names'] + '.jpg'})#调用函数获取图片信息,图片名称不包含学校
        # index = 0
        # for image_url in item['image_urls']:
        #     # yield Request(image_url)
        #     # yield Request(image_url,meta={'school_name':item['school_name'],'image_name':item['school_name'] + '_' + (item['course_names'])[index] + '.jpg'})#调用函数获取图片信息。图片名称包含学校
        #     yield Request(image_url,meta={'school_name':item['school_name'],'image_name':(item['course_names'])[index] + '.jpg'})#调用函数获取图片信息,图片名称不包含学校
        #     index = index + 1

    #返回item
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        school_name = request.meta['school_name']
        return 'course/' + school_name + '/'+'%s' % (image_guid)


#被用在course_info里面,为了在抓取数据的时候下载图片,但是仍然不全
class CourseInfoImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(url=item['image'],meta={'school_name':item['sch_name'],'image_name':item['cors_name'] + '.jpg'})#调用函数获取图片信息,图片名称不包含学校
        item['image'] ='images/course/'+ item['sch_name'] + '/' + item['cors_name']

    #返回item
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]#用户下面判断是否获得图片
        if not image_paths:
            raise DropItem("Item contains no images")
        # print 'paths', item['image_paths']
        return item

    #给图片自定义命名
    def file_path(self, request, response=None, info=None):
        # print 'fil_path', request.meta['url']
        image_guid = request.meta['image_name']
        school_name = request.meta['school_name']
        return 'course/' + school_name + '/'+'%s' % (image_guid)

class CourseInfoPipeline(object):
    def __init__(self):
        self.file = open('/Volumes/LiuQL/liuxuebao/courseInfo.json', 'wb')
        # self.file = open('/Users/Qianlong/Desktop/typeInfo.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class SchoolInfoPipeline(object):
    def __init__(self):
        self.file = open('/Volumes/LiuQL/liuxuebao/schoolInfo.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class ClassificationPipeline(object):
    def __init__(self):
        # self.file = open('/Volumes/LiuQL/liuxuebao/typeInfo.json', 'wb')
        self.file = open('/Users/Qianlong/Desktop/typeInfo.json', 'wb')

    def process_item(self, item, spider):

        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


#对应circle,保存圈子主表的信息
class CirclePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
                host = settings['MYSQL_HOST'],
                db = settings['MYSQL_DBNAME'],
                user = settings['MYSQL_USER'],
                passwd = settings['MYSQL_PASSWD'],
                charset = 'utf8',
                cursorclass= MySQLdb.cursors.DictCursor,
                use_unicode = True,
                )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d =self.dbpool.runInteraction(self._do_upinsert, item, spider)
        return d

    def _do_upinsert(self, conn, item, spider):
        conn.execute("SET NAMES utf8")
        conn.execute("select * from circle where circle_id = '%s' " % item['circle_id'])
        ret = conn.fetchone()
        if ret:
            pass
        else :
            conn.execute("""
                    insert into circle(circle_id, circle_name, circle_intro, circle_suffer_number,
                    circle_expert_number, circle_topic_number, circle_owner_id) values(%s, %s, %s, %s, %s, %s, %s)""",
                    (item["circle_id"], item["circle_name"], item["circle_intro"], item["circle_suffer_number"],
                     item["circle_expert_number"], item["circle_topic_number"], item["circle_owner_id"]))