import base64
import time
import os
import csv
import random
# from settings import proxy_list
from settings import PROXY_LIST as proxy_list
from liuxuebao.proxyClass import ProxyClass
# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy

        # proxy_list = []
        # file = open('/Users/Qianlong/Desktop/eHealth/haodaifu/proxy_effective.csv','r')
        # reader = csv.reader(file)
        # for line in reader:
        #     proxy_list.append(line[0])
        #     print '\''+line[0]+'\','
        # file.close()

        # index = random.randint(0, len(proxy_list)-1)
        # ip = (proxy_list[index].split('//')[1]).split(':')[0]
        # ping_cmd = 'ping -c 2 -W 0.5 %s' % ip
        # ping_result = os.popen(ping_cmd).read()
        # print type(ping_result)
        # print time.time(),'ping_cmd : %s, ping_result : %r' % (ping_cmd, ping_result)
        # if '100.0% packet loss' in ping_result:
        #     print 'ping %s fail' % ip
        # else:
        #     print time.time(),'ping %s ok' % ip
        #     print proxy_list[index],type(proxy_list[index])
        #     request.meta['proxy'] = proxy_list[index]
        # print time.time(),'&&&&&&', 'http://'+(proxy_list[index]['ip_port'])
        # request.meta['proxy'] = 'http://'+(proxy_list[index]['ip_port'])

        # request.meta['proxy'] = "http://115.29.33.208:8088"
        # request.meta['proxy'] = "http://115.28.2.233:8088"
        # print random.choice(proxy_list)
        # request.meta['proxy'] = random.choice(proxy_list)

        # Use the following lines if your proxy requires authentication

        proxy = ProxyClass()
        proxy_tuple = proxy.select_proxy(table='proxy')
        proxy = random.choice(proxy_tuple)
        print proxy[3].lower() + '://' + proxy[1] + ':' + proxy[2]

        request.meta['proxy'] = proxy[3].lower() + '://' + proxy[1] + ':' + proxy[2]
        # proxy_user_pass = "USERNAME:PASSWORD"
        proxy_user_pass = "861265654@qq.com:777angel"
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

    def ping_ip(self,ip=None):
        ping_cmd = 'ping -c 2 -W 0.5 %s' % ip
        ping_result = os.popen(ping_cmd).read()
        print type(ping_result)
        print time.time(),'ping_cmd : %s, ping_result : %r' % (ping_cmd, ping_result)

        if '100.0% packet loss' in ping_result:
            print 'ping %s fail' % ip
            return False
        else:
            print time.time(),'ping %s ok' % ip
            return True
