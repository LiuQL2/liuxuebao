# -*- coding: utf-8 -*-
#用户将学校的数据进行入库操作,分别写了三个函数进行地区的国家、省份、城市的入库,不过其中两个国家
#会出现问题,分别是瑞士、爱尔兰,因为该国家中学校的国家、省份都一样,所以需要手动修改。
#然后写了一个函数进行写入学校的信息,因为有些学校没有arank排名,所以第一次先写入有arank的学校,不过会有数据库出错提示,
#然后第二步去掉arank属性,写入其他的数据。
import MySQLdb
import sys
import json
import test
from twisted.enterprise import adbapi

reload(sys)
sys.setdefaultencoding('utf-8')

database_info = dict(
    host='localhost',
    user='root',
    passwd='962182',
    db='oversea',
    port=3306,
    charset='utf8'
)

#构建与数据库的链接
def build_connector(database_info):
    try:
        conn = MySQLdb.connect(host=database_info['host'],
                               user=database_info['user'],
                               passwd=database_info['passwd'],
                               db=database_info['db'],
                               port=database_info['port'],
                               charset=database_info['charset'])
        return conn
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return "Mysql Error %d: %s" % (e.args[0], e.args[1])

#写入地区中的国家级别
def write_country(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    school_csv_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    for line in school_csv_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print row['country_id']
        try:
            cursor.execute('select * from os_region where region_name = %s', [row['country_id']])
            if cursor.fetchone():
                pass
            else:
                sql = 'insert into os_region (region_name, parent_id, region_path) values(%s, %s, %s)'
                cursor.execute(sql, (row['country_id'], 0, 1))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    school_csv_file.close()
    cursor.close()
    conn.close()

#写入地区中的省份级别
def write_province(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    school_csv_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    for line in school_csv_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print row['pro_id']
        try:
            cursor.execute('select * from os_region where region_name = %s', [row['country_id']])#找出该省份对应的国家ID
            country_id = (cursor.fetchone())[0]
            cursor.execute('select * from os_region where region_name = %s and parent_id = %s', [row['pro_id'],country_id])
            if cursor.fetchone():
                pass
            else:
                sql = 'insert into os_region (region_name, parent_id, region_path) values(%s, %s, %s)'
                cursor.execute(sql, (row['pro_id'], country_id, 2))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    school_csv_file.close()
    cursor.close()
    conn.close()

#写入地区中的城市级别
def write_city(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    school_csv_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    for line in school_csv_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print row['pro_id']
        try:
            cursor.execute('select * from os_region where region_name = %s', [row['country_id']])#找出该城市对应的国家ID
            country_id = (cursor.fetchone())[0]
            cursor.execute('select * from os_region where region_name = %s', [row['pro_id']])#找出该城市对应的省份ID
            province_id = (cursor.fetchone())[0]

            cursor.execute('select * from os_region where region_name = %s and parent_id = %s', [row['city_id'],province_id])
            if cursor.fetchone():
                pass
            else:
                sql = 'insert into os_region (region_name, parent_id, region_path) values(%s, %s, %s)'
                cursor.execute(sql, (row['city_id'], province_id, 3))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    school_csv_file.close()
    cursor.close()
    conn.close()


#写入学校信息
def write_school(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    school_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    index = 0
    for line in school_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print index
        index = index + 1

        try:
            cursor.execute('select * from os_region where region_name = %s', [row['country_id']])#找出该城市对应的国家ID
            country_id = (cursor.fetchone())[0]
            # cursor.execute('select * from os_region where region_name = %s and parent_id = %s', [row['pro_id'],country_id])
            cursor.execute('select * from os_region where region_name = %s and parent_id = %s', [row['pro_id'],country_id])#找出该城市对应的省份ID
            province_id = (cursor.fetchone())[0]
            cursor.execute('select * from os_region where region_name = %s and parent_id = %s', [row['city_id'],province_id])
            city_id = (cursor.fetchone())[0]
            scate_name = find_school_scate(row['sch_id'])
            if scate_name == None:
                scate_id = ''
            else:
                cursor.execute('select * from os_scate where scate_name = %s', [scate_name])
                scate_id = (cursor.fetchone())[0]

            cursor.execute('select * from os_school where sch_name = %s and sch_fname = %s', [row['sch_name'],row['sch_fname']])
            if cursor.fetchone():
                pass
            else:
                print row['sch_name']
                sql = 'insert into os_school (sch_name, sch_fname, country_id, pro_id, city_id, scate_id,' \
                      'bache_num, master_num, sch_logo, sch_intro, sch_academic, sch_major, sch_trans, ' \
                      'sch_location, sch_tips, urank, arank) ' \
                      'values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql, (row['sch_name'], row['sch_fname'], country_id, province_id, city_id, scate_id,
                                     row['bache_num'], row['master_num'], row['logo'], row['sch_intro'], row['sch_academic'], row['sch_major'], row['sch_trans'],
                                     row['sch_location'], row['sch_tips'], row['urank'], row['arank'] ))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    school_file.close()
    cursor.close()
    conn.close()

#写入学校图片信息
def write_school_gallery(path):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    fileList = test.printPath(1,path)
    index = 0
    for file in fileList:
        img_url = 'images/school_cover/' + file
        sch_name = file.split('_')[0]
        index = index + 1
        try:
            cursor.execute('select * from os_school where sch_name = %s', [sch_name])#找出该图片对应的学校ID
            sch_id = (cursor.fetchone())[0]
            cursor.execute('select * from os_school_gallery where sch_id = %s and img_url = %s', [sch_id, img_url])
            if cursor.fetchone():
                pass
            else:
                print sch_name, sch_id,img_url
                sql = 'insert into os_school_gallery (sch_id, img_url) values( %s, %s)'
                cursor.execute(sql, (sch_id, img_url ))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    cursor.close()
    conn.close()

#写入课程中的大类信息
def write_course_cate1(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    course_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    for line in course_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print row['cors_cate_pid']
        try:
            cursor.execute('select * from os_ccate where ccate_name = %s', [row['cors_cate_pid']])
            if cursor.fetchone():
                pass
            else:
                sql = 'insert into os_ccate (ccate_name, parent_id, cors_path) values(%s, %s, %s)'
                cursor.execute(sql, (row['cors_cate_pid'], 0, 1))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    course_file.close()
    cursor.close()
    conn.close()


#写入课程中的大类信息
def write_course_cate2(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    course_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')
    for line in course_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print row['cors_cate_id']
        try:
            cursor.execute('select * from os_ccate where ccate_name = %s', [row['cors_cate_pid']])
            cate1_id = cursor.fetchone()[0]
            cursor.execute('select * from os_ccate where ccate_name = %s', [row['cors_cate_id']])
            if cursor.fetchone():
                pass
            else:
                sql = 'insert into os_ccate (ccate_name, parent_id, cors_path) values(%s, %s, %s)'
                cursor.execute(sql, (row['cors_cate_id'], cate1_id, 2))
                conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    course_file.close()
    cursor.close()
    conn.close()

#写入课程信息
def write_course(fileName):
    conn = build_connector(database_info)
    cursor = conn.cursor()
    course_file = open('/Users/Qianlong/Desktop/liuxuebao/' + fileName, 'r')

    school_file = open('/Users/Qianlong/Desktop/liuxuebao/schoolInfo.json','r')
    school_list = []
    for line in school_file:
        row = unicode_to_utf8(json.loads(line))
        school = {}
        school['sch_name'] = row['sch_name']
        school['sch_advice'] = row['sch_advice']
        school_list.append(school)
    school_file.close()

    no_school_list = []

    index = 0
    for line in course_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        print index
        index = index + 1
        try:
            cursor.execute('select * from os_school where sch_name = %s', [row['sch_name']])#找出该课程对应的学校ID
            list_temp = (cursor.fetchone())
            if list_temp == None:#是否有这个学校
                no_school_list.append(row['sch_name'])
                print '***************************************************************',row['sch_name']
            else:
                sch_id = list_temp[0]
                cursor.execute('select * from os_course where sch_id = %s and cors_name = %s', [sch_id,row['cors_name']])
                if cursor.fetchone():
                    pass
                else:
                    if (row['cors_fee'].split(' ')[0]).isalpha():
                        cors_fee = 0
                    else:
                        cors_fee = change_crash_unit(number=float(row['cors_fee'].split(' ')[0]), unit = row['cors_fee'].split(' ')[1])
                    span = row['span'].split('年')[0]
                    # is_intro = wether_advice(row['cors_name'], row['sch_name'])
                    is_intro = wether_advice2(row['cors_name'], row['sch_name'],school_list)
                    cursor.execute('select * from os_ccate where ccate_name = %s', [row['cors_cate_id']])
                    ccate_id = (cursor.fetchone())[0]
                    print row['sch_name'], sch_id, row['cors_name']
                    sql = 'insert into os_course (cors_name, cors_fname, sch_id, cors_img, ccate_id, cors_fee,' \
                      'edu_bkgrd, span, enroll_time, app_prblm, lan_reqir, aca_reqir, othr_reqir, ' \
                      'material, is_intro) ' \
                      'values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql, (row['cors_name'], row['cors_fname'], sch_id, row['image'], ccate_id, cors_fee,
                                     row['edu_bkgrd'], span, row['enroll_time'], row['app_prblm'], row['lan_reqir'], row['aca_reqir'], row['othr_reqir'],
                                     row['material'], is_intro))
                    conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    for school in no_school_list:
        print school
    print len(no_school_list)
    course_file.close()
    cursor.close()
    conn.close()


# 把unicode编码的字典转化为utf-8的编码形式
def unicode_to_utf8(dict):
    result = {}
    for key in dict.keys():
        result[key.encode('utf-8')] = dict[key].encode('utf-8')
    return result

#根据学校网址,查找学校类型
def find_school_scate(school_id):
    school_type_file = open('/Users/Qianlong/Desktop/liuxuebao/typeInfo.json', 'r')
    type_id = None
    for line in school_type_file:
        row = unicode_to_utf8(json.loads(line))  # 提取json形式
        if row['sch_id'] == school_id:
            type_id = row['type_name']
            break
    school_type_file.close()
    return type_id

#根据课程所属的学校,查找学校是否为建议课程,1为建议,0为不建议
def wether_advice(course_name, sch_name):
    school_file = open('/Users/Qianlong/Desktop/liuxuebao/schoolInfo.json', 'r')
    advice = 0
    for line in school_file:
        row = unicode_to_utf8(json.loads(line))
        if row['sch_name'] == sch_name and (course_name in row['sch_advice']):
            advice = 1
            break
    school_file.close()
    return advice

def wether_advice2(course_name, sch_name, sch_list):
    advice = 0
    for row in sch_list:
        if row['sch_name'] == sch_name and (course_name in row['sch_advice']):
            advice = 1
            break
    return advice

#变换货币单位
def change_crash_unit(number, unit):
    unit_list = ['美元','英镑','澳元','加币','欧元','新币','纽元','港币','瑞士法郎']
    rate_list = [ 1,   1.337, 0.766, 0.7756, 1.129,0.7411,0.7419,0.1289, 1.0312]
    new_number = rate_list[unit_list.index(unit)] * number
    return int(round(new_number))

# write_country('schoolInfo.json')
# write_province('schoolInfo.json')
# write_city('schoolInfo.json')
# write_school('schoolInfo.json')
# write_school_gallery('/Volumes/LiuQL/liuxuebao/images/school_cover')
# write_course_cate2('courseInfo.json')
# change_crash_unit(26,'英镑')
write_course('courseInfo.json')
print database_info
