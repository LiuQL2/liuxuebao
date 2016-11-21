# -*- coding: utf-8 -*-

'不断运行检验代理是否可行，不可信的删除，可行的保留在effective表中'

import MySQLdb
import os
import sys
import MySQLdb.cursors
import traceback
import urllib2
import time
from twisted.enterprise import adbapi
from liuxuebao.settings import database_info
reload(sys)
sys.setdefaultencoding('utf-8')


class ProxyClass(object):
    #构建与数据库的链接
    def __init__(self):
        self._all_to_effective_process = None
        self._maintain_effective_process = None
        try:
            conn = MySQLdb.connect(host=database_info['host'],
                               user=database_info['user'],
                               passwd=database_info['passwd'],
                               db=database_info['db'],
                               port=database_info['port'],
                               charset=database_info['charset'])
            self._connector = conn
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def colse_connect(self):
        return self._connector.close()

    #从代理总表中验证，如果代理可用就放倒有效表中，不可用直接删除
    def all_to_effective(self):
        try:
            self._all_to_effective_process = 'processing'
            proxy_tuple = self.select_proxy(table='proxy_all')
            for proxy in proxy_tuple:
                if self.ping_ip(proxy) and self.verify_ip_hdf(proxy):
                    self.insert_proxy(table='proxy_effective',proxy=proxy)
                else:
                    self.delete_proxy(table='proxy_effective',proxy=proxy)
                    self.delete_proxy(table='proxy_all',proxy=proxy)
            self._all_to_effective_process = 'over'
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    #维护有效表，如果一个代理仍旧有效则仍然放在有效表中
    def maintain_effective(self):
        try:
            self._maintain_effective_process = 'processing'
            proxy_tuple = self.select_proxy(table = 'proxy_effective')
            for proxy in proxy_tuple:
                if self.ping_ip(proxy) and self.verify_ip_hdf(proxy):
                    pass
                else:
                    self.delete_proxy(table='proxy_effective', proxy=proxy)
                    self.delete_proxy(table='proxy_all', proxy=proxy)
            self._maintain_effective_process = 'over'
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    #从表中读取proxy，根据是否传入参数proxy判断是读取所有数据，还是读取一个proxy
    def select_proxy(self, table = None, proxy=None):
        try:
            cursor = self._connector.cursor()
            if proxy == None:
                cursor.execute('select * from '+ table)
                proxy_tuple = cursor.fetchall()
            else:
                cursor.execute('select * from '+ table +' where proxy_ip = %s and proxy_port = %s', [proxy[1], proxy[2]])
                proxy_tuple = cursor.fetchall()
            cursor.close()
            return proxy_tuple
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            return tuple()

    #从表table中删除proxy
    def delete_proxy(self, table = None, proxy=None):
        try:
            proxy_temp = self.select_proxy(table=table,proxy = proxy)
            if len(proxy_temp) == 0:
                print '表' + table + '不存在：', proxy[1],':',proxy[2]
                pass
            else:
                cursor = self._connector.cursor()
                cursor.execute('delete from ' + table + ' where proxy_ip = %s and proxy_port = %s', [proxy[1], proxy[2]])
                self._connector.commit()
                cursor.close()
                print '从'+ table +'表中删除：',proxy[1],':', proxy[2]
        except MySQLdb.Error, e:
            print 'Mysql Error %d: %s' % (e.args[0], e.args[1])


    #在表table 中插入proxy
    def insert_proxy(self,table = None, proxy = None):
        try:
            proxy_temp = self.select_proxy(table = table, proxy = proxy)
            if len(proxy_temp) != 0:
                print '表'+table+'已经存在：', proxy[1],':',proxy[2]
                pass
            else:
                cursor = self._connector.cursor()
                sql = 'insert into '+ table + ' (proxy_type, proxy_ip, proxy_port, proxy_location, proxy_speed) values(%s, %s, %s, %s, %s)'
                cursor.execute(sql, (proxy[0],proxy[1],proxy[2],proxy[3],proxy[4]))
                self._connector.commit()
                cursor.close()
                print '在'+ table + '表中插入：',proxy[1],':', proxy[2]
        except MySQLdb.Error, e:
            print 'Mysql Error %d: %s' % (e.args[0], e.args[1])


    #ping功能，验证代理ip是否可用
    def ping_ip(self,proxy=None):
        ip = proxy[1]
        ping_cmd = 'ping -c 5 -W 0.005 %s' % ip
        ping_result = os.popen(ping_cmd).read()
        # print 'ping_cmd : %s, ping_result : %r' % (ping_cmd, ping_result)
        if 'received, 0.0% packet loss' in ping_result:
            # print 'ping %s ok' % ip
            return True
        else:
            # print 'ping %s fail' % ip
            return False

    #验证一个代理是否能够访问好大夫
    def verify_ip_hdf(self, proxy=None):
        proxy_temp = urllib2.ProxyHandler({proxy[0].lower(): proxy[1] + proxy[2]})
        opener = urllib2.build_opener(proxy_temp)
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen('http://www.haodf.com',timeout = 50)
            sel = response.read()
            if '<title>250 Forbidden</title>' not in sel:
                return True
            else:
                return False
        except Exception,e:
            return False


if __name__ == '__main__':
    proxy = ProxyClass()
    proxy.maintain_effective()
    proxy.all_to_effective()
    proxy.colse_connect()