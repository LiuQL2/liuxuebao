# -*- coding: utf-8 -*-

# Scrapy settings for liuxuebao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'liuxuebao'

SPIDER_MODULES = ['liuxuebao.spiders']
NEWSPIDER_MODULE = 'liuxuebao.spiders'

#mysql configuration
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'xunyiwenyao'
MYSQL_USER = 'root'
MYSQL_PASSWD = '962182'
LOG_LEVEL = 'INFO'



database_info = dict(
    host='localhost',
    user='root',
    passwd='962182',
    db='hdf',
    port=3306,
    charset='utf8',
    # cursorclass= MySQLdb.cursors.DictCursor,
    use_unicode = True,
)

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'liuxuebao.middlewares.ProxyMiddleware': 100,
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'liuxuebao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'liuxuebao.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'liuxuebao.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'liuxuebao.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

PROXY_LIST = [
{'ip_port': '122.193.202.148:6969', 'user_pass': ''} ,
{'ip_port': '60.194.100.51:80', 'user_pass': ''} ,
{'ip_port': '124.88.67.20:80', 'user_pass': ''} ,
{'ip_port': '122.5.243.116:8888', 'user_pass': ''} ,
{'ip_port': '218.30.99.209:81', 'user_pass': ''} ,
{'ip_port': '112.81.100.102:8888', 'user_pass': ''} ,
{'ip_port': '110.181.181.164:8888', 'user_pass': ''} ,
{'ip_port': '183.129.178.14:8080', 'user_pass': ''} ,
{'ip_port': '113.121.134.8:8888', 'user_pass': ''} ,
{'ip_port': '120.76.243.40:80', 'user_pass': ''} ,
{'ip_port': '115.28.2.233:8088', 'user_pass': ''} ,
]

proxy_list = [
# {'ip_port': '60.194.100.51:80', 'user_pass': ''} ,
# {'ip_port': '124.88.67.20:80', 'user_pass': ''} ,
# {'ip_port': '112.228.38.33:8888', 'user_pass': ''} ,
# {'ip_port': '122.5.243.116:8888', 'user_pass': ''} ,
# {'ip_port': '117.15.134.66:8888', 'user_pass': ''} ,
# {'ip_port': '218.30.99.209:81', 'user_pass': ''} ,
# {'ip_port': '112.81.100.102:8888', 'user_pass': ''} ,
# {'ip_port': '110.181.181.164:8888', 'user_pass': ''} ,
# {'ip_port': '122.193.202.148:6969', 'user_pass': ''} ,
# {'ip_port': '27.205.6.188:81', 'user_pass': ''} ,
# {'ip_port': '183.129.178.14:8080', 'user_pass': ''} ,
# {'ip_port': '113.121.134.8:8888', 'user_pass': ''} ,
# {'ip_port': '120.76.243.40:80', 'user_pass': ''} ,
# {'ip_port': '39.89.182.37:8888', 'user_pass': ''} ,
# {'ip_port': '115.28.2.233:8088', 'user_pass': ''} ,
# {'ip_port': '113.195.84.230:8888', 'user_pass': ''} ,
{'ip_port': '115.29.33.208:8088', 'user_pass': ''} ,
{'ip_port': '61.143.158.238:808', 'user_pass': ''} ,
{'ip_port': '222.45.233.2:3128', 'user_pass': ''} ,
{'ip_port': '116.204.64.97:8080', 'user_pass': ''} ,
{'ip_port': '119.53.124.84:8118', 'user_pass': ''} ,
{'ip_port': '39.1.46.23:8080', 'user_pass': ''} ,
{'ip_port': '121.31.48.197:8123', 'user_pass': ''} ,
{'ip_port': '110.73.8.74:8123', 'user_pass': ''} ,
{'ip_port': '39.1.43.127:8080', 'user_pass': ''} ,
{'ip_port': '118.233.194.25:8090', 'user_pass': ''} ,
{'ip_port': '60.169.78.218:808', 'user_pass': ''} ,
{'ip_port': '175.5.140.244:81', 'user_pass': ''} ,
{'ip_port': '39.1.47.184:8080', 'user_pass': ''} ,
{'ip_port': '122.195.181.46:8888', 'user_pass': ''} ,
{'ip_port': '39.1.36.88:8080', 'user_pass': ''} ,
{'ip_port': '39.1.36.34:8080', 'user_pass': ''} ,
{'ip_port': '119.1.170.3:80', 'user_pass': ''} ,
{'ip_port': '39.1.42.93:8080', 'user_pass': ''} ,
{'ip_port': '113.122.83.166:8888', 'user_pass': ''} ,
{'ip_port': '171.38.242.59:8123', 'user_pass': ''} ,
{'ip_port': '218.241.153.211:81', 'user_pass': ''} ,
{'ip_port': '39.1.43.211:8080', 'user_pass': ''} ,
{'ip_port': '39.1.36.125:8080', 'user_pass': ''} ,
{'ip_port': '39.1.42.56:8080', 'user_pass': ''} ,
{'ip_port': '60.209.167.130:8888', 'user_pass': ''} ,
{'ip_port': '123.168.211.215:808', 'user_pass': ''} ,
{'ip_port': '39.1.42.153:8080', 'user_pass': ''} ,
{'ip_port': '59.148.118.3:80', 'user_pass': ''} ,
{'ip_port': '124.88.67.17:82', 'user_pass': ''} ,
{'ip_port': '39.1.42.133:8080', 'user_pass': ''} ,
{'ip_port': '39.1.46.108:8080', 'user_pass': ''} ,
{'ip_port': '183.141.127.71:3128', 'user_pass': ''} ,
{'ip_port': '39.1.43.144:8080', 'user_pass': ''} ,
{'ip_port': '39.1.42.61:8080', 'user_pass': ''} ,
{'ip_port': '39.1.43.213:8080', 'user_pass': ''} ,
{'ip_port': '39.1.43.245:8080', 'user_pass': ''} ,
{'ip_port': '111.155.124.71:8123', 'user_pass': ''} ,
{'ip_port': '221.238.140.210:81', 'user_pass': ''} ,
{'ip_port': '221.195.55.182:8080', 'user_pass': ''} ,
{'ip_port': '110.73.50.221:8123', 'user_pass': ''} ,
{'ip_port': '134.196.87.170:8080', 'user_pass': ''} ,
{'ip_port': '39.1.47.62:8080', 'user_pass': ''} ,
{'ip_port': '39.1.46.152:8080', 'user_pass': ''} ,
{'ip_port': '39.1.41.94:8080', 'user_pass': ''} ,
{'ip_port': '121.31.78.202:8123', 'user_pass': ''} ,
{'ip_port': '39.1.37.72:8080', 'user_pass': ''} ,
{'ip_port': '110.73.41.179:8123', 'user_pass': ''} ,
{'ip_port': '110.72.17.130:8123', 'user_pass': ''} ,
{'ip_port': '110.73.5.210:8123', 'user_pass': ''} ,
{'ip_port': '39.1.46.38:8080', 'user_pass': ''} ,
{'ip_port': '111.155.116.211:8123', 'user_pass': ''} ,
{'ip_port': '222.170.17.74:2226', 'user_pass': ''} ,
{'ip_port': '39.1.42.124:8080', 'user_pass': ''} ,
{'ip_port': '123.56.182.111:82', 'user_pass': ''} ,
{'ip_port': '123.57.190.51:7777', 'user_pass': ''} ,
{'ip_port': '120.76.102.156:808', 'user_pass': ''} ,
{'ip_port': '124.88.67.24:80', 'user_pass': ''} ,
{'ip_port': '61.228.45.238:8998', 'user_pass': ''} ,
{'ip_port': '110.72.39.50:8123', 'user_pass': ''} ,
{'ip_port': '39.1.42.134:8080', 'user_pass': ''} ,
{'ip_port': '110.73.38.56:8123', 'user_pass': ''} ,
{'ip_port': '110.73.28.41:8123', 'user_pass': ''} ,
{'ip_port': '171.38.157.176:8123', 'user_pass': ''} ,
{'ip_port': '39.1.47.171:8080', 'user_pass': ''} ,
{'ip_port': '110.73.49.43:8123', 'user_pass': ''} ,
{'ip_port': '123.132.199.68:81', 'user_pass': ''} ,
{'ip_port': '110.73.4.10:8123', 'user_pass': ''} ,
{'ip_port': '171.39.69.249:8123', 'user_pass': ''} ,
{'ip_port': '101.200.87.201:808', 'user_pass': ''} ,
{'ip_port': '182.88.179.161:8123', 'user_pass': ''} ,
{'ip_port': '121.31.151.26:8123', 'user_pass': ''} ,
{'ip_port': '121.31.73.158:8123', 'user_pass': ''} ,
{'ip_port': '202.207.210.22:808', 'user_pass': ''} ,
{'ip_port': '39.1.47.118:8080', 'user_pass': ''} ,
{'ip_port': '182.92.190.64:8888', 'user_pass': ''} ,
{'ip_port': '110.72.40.18:8123', 'user_pass': ''} ,
{'ip_port': '110.73.14.76:8123', 'user_pass': ''} ,
{'ip_port': '121.31.101.11:8123', 'user_pass': ''} ,
{'ip_port': '61.153.18.179:8888', 'user_pass': ''} ,
{'ip_port': '110.72.44.216:8123', 'user_pass': ''} ,
{'ip_port': '171.38.241.87:8123', 'user_pass': ''} ,
{'ip_port': '60.185.129.199:3128', 'user_pass': ''} ,
{'ip_port': '171.39.34.159:8123', 'user_pass': ''} ,
{'ip_port': '110.72.39.98:8123', 'user_pass': ''} ,
{'ip_port': '180.153.87.22:18080', 'user_pass': ''} ,
{'ip_port': '39.1.46.253:8080', 'user_pass': ''} ,
{'ip_port': '115.159.64.193:80', 'user_pass': ''} ,
{'ip_port': '42.96.167.99:8088', 'user_pass': ''} ,
{'ip_port': '39.1.46.144:8080', 'user_pass': ''} ,
{'ip_port': '182.88.30.50:8123', 'user_pass': ''} ,
{'ip_port': '121.31.101.63:8123', 'user_pass': ''} ,
{'ip_port': '182.88.30.182:8123', 'user_pass': ''} ,
{'ip_port': '120.32.189.148:8118', 'user_pass': ''} ,
{'ip_port': '110.73.31.224:8123', 'user_pass': ''} ,
{'ip_port': '171.38.202.135:8123', 'user_pass': ''} ,
{'ip_port': '182.89.10.192:8123', 'user_pass': ''} ,
{'ip_port': '171.38.176.46:8123', 'user_pass': ''} ,
{'ip_port': '121.31.150.8:8123', 'user_pass': ''} ,
{'ip_port': '171.38.163.225:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.171:8123', 'user_pass': ''} ,
{'ip_port': '171.38.171.47:8123', 'user_pass': ''} ,
{'ip_port': '39.1.43.48:8080', 'user_pass': ''} ,
{'ip_port': '119.188.94.145:80', 'user_pass': ''} ,
{'ip_port': '124.240.187.84:83', 'user_pass': ''} ,
{'ip_port': '110.73.10.35:8123', 'user_pass': ''} ,
{'ip_port': '123.207.96.189:80', 'user_pass': ''} ,
{'ip_port': '110.73.14.152:8123', 'user_pass': ''} ,
{'ip_port': '61.178.63.90:63000', 'user_pass': ''} ,
{'ip_port': '182.90.78.31:8123', 'user_pass': ''} ,
{'ip_port': '171.37.135.51:8123', 'user_pass': ''} ,
{'ip_port': '171.38.179.125:8123', 'user_pass': ''} ,
{'ip_port': '202.201.125.51:8080', 'user_pass': ''} ,
{'ip_port': '182.88.207.72:8123', 'user_pass': ''} ,
{'ip_port': '110.72.28.229:8123', 'user_pass': ''} ,
{'ip_port': '171.38.170.22:8123', 'user_pass': ''} ,
{'ip_port': '106.75.129.29:80', 'user_pass': ''} ,
{'ip_port': '110.72.39.241:8123', 'user_pass': ''} ,
{'ip_port': '182.88.28.245:8123', 'user_pass': ''} ,
{'ip_port': '39.1.47.65:8080', 'user_pass': ''} ,
{'ip_port': '110.73.15.58:8123', 'user_pass': ''} ,
{'ip_port': '110.73.51.27:8123', 'user_pass': ''} ,
{'ip_port': '171.37.164.239:8123', 'user_pass': ''} ,
{'ip_port': '39.1.46.137:8080', 'user_pass': ''} ,
{'ip_port': '171.38.163.228:8123', 'user_pass': ''} ,
{'ip_port': '171.38.205.122:8123', 'user_pass': ''} ,
{'ip_port': '182.89.7.120:8123', 'user_pass': ''} ,
{'ip_port': '110.73.8.223:8123', 'user_pass': ''} ,
{'ip_port': '110.73.11.77:8123', 'user_pass': ''} ,
{'ip_port': '110.73.37.187:8123', 'user_pass': ''} ,
{'ip_port': '171.36.255.127:8123', 'user_pass': ''} ,
{'ip_port': '39.1.43.122:8080', 'user_pass': ''} ,
{'ip_port': '171.38.198.217:8123', 'user_pass': ''} ,
{'ip_port': '116.227.26.221:37380', 'user_pass': ''} ,
{'ip_port': '39.1.36.99:8080', 'user_pass': ''} ,
{'ip_port': '171.36.60.129:8123', 'user_pass': ''} ,
{'ip_port': '171.38.209.102:8123', 'user_pass': ''} ,
{'ip_port': '182.88.207.198:8123', 'user_pass': ''} ,
{'ip_port': '110.73.34.193:8123', 'user_pass': ''} ,
{'ip_port': '171.38.209.23:8123', 'user_pass': ''} ,
{'ip_port': '121.31.101.197:8123', 'user_pass': ''} ,
{'ip_port': '221.204.177.57:1920', 'user_pass': ''} ,
{'ip_port': '1.161.158.124:8080', 'user_pass': ''} ,
{'ip_port': '222.206.90.52:8998', 'user_pass': ''} ,
{'ip_port': '110.72.38.142:8123', 'user_pass': ''} ,
{'ip_port': '110.73.49.223:8123', 'user_pass': ''} ,
{'ip_port': '110.73.49.40:8123', 'user_pass': ''} ,
{'ip_port': '110.72.45.91:8123', 'user_pass': ''} ,
{'ip_port': '123.57.52.171:80', 'user_pass': ''} ,
{'ip_port': '110.73.0.145:8123', 'user_pass': ''} ,
{'ip_port': '1.164.151.83:8080', 'user_pass': ''} ,
{'ip_port': '110.73.28.73:8123', 'user_pass': ''} ,
{'ip_port': '121.31.144.215:8123', 'user_pass': ''} ,
{'ip_port': '222.75.36.194:808', 'user_pass': ''} ,
{'ip_port': '171.38.161.231:8123', 'user_pass': ''} ,
{'ip_port': '58.154.190.134:808', 'user_pass': ''} ,
{'ip_port': '36.7.172.18:82', 'user_pass': ''} ,
{'ip_port': '218.244.149.184:8888', 'user_pass': ''} ,
{'ip_port': '39.1.40.36:8080', 'user_pass': ''} ,
{'ip_port': '110.73.4.143:8888', 'user_pass': ''} ,
{'ip_port': '116.255.246.109:8080', 'user_pass': ''} ,
{'ip_port': '171.36.255.161:8123', 'user_pass': ''} ,
{'ip_port': '123.207.166.149:8888', 'user_pass': ''} ,
{'ip_port': '121.31.49.69:8123', 'user_pass': ''} ,
{'ip_port': '123.206.8.225:8888', 'user_pass': ''} ,
{'ip_port': '39.1.46.138:8080', 'user_pass': ''} ,
{'ip_port': '222.29.45.143:808', 'user_pass': ''} ,
{'ip_port': '110.73.53.69:8123', 'user_pass': ''} ,
{'ip_port': '182.89.5.74:8123', 'user_pass': ''} ,
{'ip_port': '171.37.132.167:8123', 'user_pass': ''} ,
{'ip_port': '61.62.147.237:8080', 'user_pass': ''} ,
{'ip_port': '110.73.11.36:8123', 'user_pass': ''} ,
{'ip_port': '110.72.38.212:8123', 'user_pass': ''} ,
{'ip_port': '171.38.177.76:8123', 'user_pass': ''} ,
{'ip_port': '39.1.43.42:8080', 'user_pass': ''} ,
{'ip_port': '123.206.89.198:8888', 'user_pass': ''} ,
{'ip_port': '110.73.35.60:8123', 'user_pass': ''} ,
{'ip_port': '125.39.68.70:83', 'user_pass': ''} ,
{'ip_port': '118.212.80.133:8118', 'user_pass': ''} ,
{'ip_port': '171.39.2.211:8123', 'user_pass': ''} ,
{'ip_port': '58.221.190.50:80', 'user_pass': ''} ,
{'ip_port': '182.88.207.147:8123', 'user_pass': ''} ,
{'ip_port': '121.31.144.122:8123', 'user_pass': ''} ,
{'ip_port': '121.31.147.170:8123', 'user_pass': ''} ,
{'ip_port': '110.72.25.154:8123', 'user_pass': ''} ,
{'ip_port': '110.73.38.251:8123', 'user_pass': ''} ,
{'ip_port': '39.1.37.147:8080', 'user_pass': ''} ,
{'ip_port': '14.198.6.91:8090', 'user_pass': ''} ,
{'ip_port': '171.38.213.227:8123', 'user_pass': ''} ,
{'ip_port': '110.73.39.221:8123', 'user_pass': ''} ,
{'ip_port': '120.76.30.231:80', 'user_pass': ''} ,
{'ip_port': '110.73.11.96:8123', 'user_pass': ''} ,
{'ip_port': '183.167.250.6:9999', 'user_pass': ''} ,
{'ip_port': '171.36.253.89:8123', 'user_pass': ''} ,
{'ip_port': '115.24.189.20:8998', 'user_pass': ''} ,
{'ip_port': '171.38.208.159:8123', 'user_pass': ''} ,
{'ip_port': '121.31.88.96:8123', 'user_pass': ''} ,
{'ip_port': '171.38.188.138:8123', 'user_pass': ''} ,
{'ip_port': '218.93.114.100:8888', 'user_pass': ''} ,
{'ip_port': '39.1.37.53:8080', 'user_pass': ''} ,
{'ip_port': '110.73.13.145:8123', 'user_pass': ''} ,
{'ip_port': '123.206.195.146:80', 'user_pass': ''} ,
{'ip_port': '101.201.235.141:8000', 'user_pass': ''} ,
{'ip_port': '171.38.163.66:8123', 'user_pass': ''} ,
{'ip_port': '39.1.36.243:8080', 'user_pass': ''} ,
{'ip_port': '110.73.1.10:8123', 'user_pass': ''} ,
{'ip_port': '110.72.16.55:8123', 'user_pass': ''} ,
{'ip_port': '110.73.8.127:8123', 'user_pass': ''} ,
{'ip_port': '110.73.1.210:8123', 'user_pass': ''} ,
{'ip_port': '182.148.114.171:3128', 'user_pass': ''} ,
{'ip_port': '182.61.1.90:80', 'user_pass': ''} ,
{'ip_port': '183.139.181.206:8080', 'user_pass': ''} ,
{'ip_port': '182.90.18.197:80', 'user_pass': ''} ,
{'ip_port': '110.73.52.18:8123', 'user_pass': ''} ,
{'ip_port': '171.37.133.198:8123', 'user_pass': ''} ,
{'ip_port': '39.1.37.76:8080', 'user_pass': ''} ,
{'ip_port': '110.73.29.14:8123', 'user_pass': ''} ,
{'ip_port': '110.73.42.167:8123', 'user_pass': ''} ,
{'ip_port': '202.75.210.45:7777', 'user_pass': ''} ,
{'ip_port': '121.31.157.193:8123', 'user_pass': ''} ,
{'ip_port': '110.73.39.114:8123', 'user_pass': ''} ,
{'ip_port': '210.72.14.142:80', 'user_pass': ''} ,
{'ip_port': '39.1.37.127:8080', 'user_pass': ''} ,
{'ip_port': '110.72.27.116:8998', 'user_pass': ''} ,
{'ip_port': '39.1.40.155:8080', 'user_pass': ''} ,
{'ip_port': '171.38.177.172:8123', 'user_pass': ''} ,
{'ip_port': '124.88.67.19:80', 'user_pass': ''} ,
{'ip_port': '39.1.42.121:8080', 'user_pass': ''} ,
{'ip_port': '171.38.202.148:8123', 'user_pass': ''} ,
{'ip_port': '39.1.36.217:8080', 'user_pass': ''} ,
{'ip_port': '121.31.156.95:8123', 'user_pass': ''} ,
{'ip_port': '39.1.46.219:8080', 'user_pass': ''} ,
{'ip_port': '39.1.47.175:8080', 'user_pass': ''} ,
{'ip_port': '220.249.141.244:8118', 'user_pass': ''} ,
{'ip_port': '39.1.46.28:8080', 'user_pass': ''} ,
{'ip_port': '59.188.75.74:8080', 'user_pass': ''} ,
{'ip_port': '171.39.41.6:8123', 'user_pass': ''} ,
{'ip_port': '182.90.18.114:80', 'user_pass': ''} ,
{'ip_port': '39.1.47.202:8080', 'user_pass': ''} ,
{'ip_port': '182.90.1.243:80', 'user_pass': ''} ,
{'ip_port': '121.31.158.115:8123', 'user_pass': ''} ,
{'ip_port': '39.1.47.111:8080', 'user_pass': ''} ,
{'ip_port': '39.1.36.80:8080', 'user_pass': ''} ,
{'ip_port': '39.1.41.169:8080', 'user_pass': ''} ,
{'ip_port': '182.90.1.1:80', 'user_pass': ''} ,
{'ip_port': '39.1.37.218:8080', 'user_pass': ''} ,
{'ip_port': '39.1.36.50:8080', 'user_pass': ''} ,
{'ip_port': '39.1.37.123:8080', 'user_pass': ''} ,
{'ip_port': '123.56.100.105:8888', 'user_pass': ''} ,
{'ip_port': '111.155.116.216:8123', 'user_pass': ''} ,
{'ip_port': '110.72.17.241:8123', 'user_pass': ''} ,
{'ip_port': '39.1.47.112:8080', 'user_pass': ''} ,
{'ip_port': '113.31.82.174:8090', 'user_pass': ''} ,
{'ip_port': '39.1.36.149:8080', 'user_pass': ''} ,
{'ip_port': '110.72.30.190:8123', 'user_pass': ''} ,
{'ip_port': '110.73.8.238:8123', 'user_pass': ''} ,
{'ip_port': '110.72.24.15:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.85:8123', 'user_pass': ''} ,
{'ip_port': '182.90.61.193:80', 'user_pass': ''} ,
{'ip_port': '39.1.46.178:8080', 'user_pass': ''} ,
{'ip_port': '121.31.106.31:8123', 'user_pass': ''} ,
{'ip_port': '39.1.46.168:8080', 'user_pass': ''} ,
{'ip_port': '182.88.135.233:8123', 'user_pass': ''} ,
{'ip_port': '171.37.132.78:8123', 'user_pass': ''} ,
{'ip_port': '121.31.102.102:8123', 'user_pass': ''} ,
{'ip_port': '182.88.166.160:8123', 'user_pass': ''} ,
{'ip_port': '110.73.49.252:8123', 'user_pass': ''} ,
{'ip_port': '171.39.67.121:8123', 'user_pass': ''} ,
{'ip_port': '182.90.119.15:80', 'user_pass': ''} ,
{'ip_port': '39.1.42.132:8080', 'user_pass': ''} ,
{'ip_port': '121.31.100.20:8123', 'user_pass': ''} ,
{'ip_port': '115.46.91.177:8123', 'user_pass': ''} ,
{'ip_port': '110.73.8.226:8123', 'user_pass': ''} ,
{'ip_port': '121.31.157.94:8123', 'user_pass': ''} ,
{'ip_port': '182.48.113.11:8088', 'user_pass': ''} ,
{'ip_port': '112.74.195.28:80', 'user_pass': ''} ,
{'ip_port': '123.57.172.247:81', 'user_pass': ''} ,
{'ip_port': '182.90.35.217:80', 'user_pass': ''} ,
{'ip_port': '39.1.36.40:8080', 'user_pass': ''} ,
{'ip_port': '171.39.232.202:80', 'user_pass': ''} ,
{'ip_port': '121.31.148.244:8123', 'user_pass': ''} ,
{'ip_port': '121.31.151.197:8123', 'user_pass': ''} ,
{'ip_port': '171.39.40.197:8123', 'user_pass': ''} ,
{'ip_port': '59.45.108.215:80', 'user_pass': ''} ,
{'ip_port': '39.1.46.234:8080', 'user_pass': ''} ,
{'ip_port': '110.73.1.22:8123', 'user_pass': ''} ,
{'ip_port': '182.90.24.164:80', 'user_pass': ''} ,
{'ip_port': '39.1.46.146:8080', 'user_pass': ''} ,
{'ip_port': '182.88.229.79:8123', 'user_pass': ''} ,
{'ip_port': '171.38.198.169:8123', 'user_pass': ''} ,
{'ip_port': '110.73.31.97:8123', 'user_pass': ''} ,
{'ip_port': '182.88.40.9:8123', 'user_pass': ''} ,
{'ip_port': '110.73.11.31:8123', 'user_pass': ''} ,
{'ip_port': '182.90.43.215:80', 'user_pass': ''} ,
{'ip_port': '110.72.45.20:8123', 'user_pass': ''} ,
{'ip_port': '118.255.204.131:3128', 'user_pass': ''} ,
{'ip_port': '39.1.47.176:8080', 'user_pass': ''} ,
{'ip_port': '39.1.47.16:8080', 'user_pass': ''} ,
{'ip_port': '203.195.152.95:80', 'user_pass': ''} ,
{'ip_port': '110.73.0.69:8123', 'user_pass': ''} ,
{'ip_port': '121.31.102.220:8123', 'user_pass': ''} ,
{'ip_port': '110.73.10.144:8123', 'user_pass': ''} ,
{'ip_port': '182.90.61.157:80', 'user_pass': ''} ,
{'ip_port': '182.90.66.253:80', 'user_pass': ''} ,
{'ip_port': '182.90.80.145:8123', 'user_pass': ''} ,
{'ip_port': '121.31.153.174:8123', 'user_pass': ''} ,
{'ip_port': '180.172.41.205:59346', 'user_pass': ''} ,
{'ip_port': '111.155.116.213:8123', 'user_pass': ''} ,
{'ip_port': '123.203.21.40:8090', 'user_pass': ''} ,
{'ip_port': '171.38.167.185:8123', 'user_pass': ''} ,
{'ip_port': '110.73.48.158:8123', 'user_pass': ''} ,
{'ip_port': '182.90.78.221:80', 'user_pass': ''} ,
{'ip_port': '122.14.40.15:808', 'user_pass': ''} ,
{'ip_port': '171.39.79.216:8123', 'user_pass': ''} ,
{'ip_port': '123.207.58.245:80', 'user_pass': ''} ,
{'ip_port': '110.73.8.184:8123', 'user_pass': ''} ,
{'ip_port': '110.73.50.235:8123', 'user_pass': ''} ,
{'ip_port': '110.73.14.67:8123', 'user_pass': ''} ,
{'ip_port': '171.38.38.65:8123', 'user_pass': ''} ,
{'ip_port': '171.38.175.28:8123', 'user_pass': ''} ,
{'ip_port': '182.90.8.46:80', 'user_pass': ''} ,
{'ip_port': '121.31.147.238:8123', 'user_pass': ''} ,
{'ip_port': '171.36.255.229:8123', 'user_pass': ''} ,
{'ip_port': '182.89.6.200:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.244:8123', 'user_pass': ''} ,
{'ip_port': '106.1.185.128:8090', 'user_pass': ''} ,
{'ip_port': '115.46.90.21:8123', 'user_pass': ''} ,
{'ip_port': '110.73.50.86:8123', 'user_pass': ''} ,
{'ip_port': '110.73.49.25:8123', 'user_pass': ''} ,
{'ip_port': '182.90.62.203:80', 'user_pass': ''} ,
{'ip_port': '115.46.67.74:8123', 'user_pass': ''} ,
{'ip_port': '183.61.236.53:3128', 'user_pass': ''} ,
{'ip_port': '183.61.236.54:3128', 'user_pass': ''} ,
{'ip_port': '110.73.9.72:8123', 'user_pass': ''} ,
{'ip_port': '110.72.19.164:8123', 'user_pass': ''} ,
{'ip_port': '182.90.66.20:80', 'user_pass': ''} ,
{'ip_port': '110.73.11.98:8123', 'user_pass': ''} ,
{'ip_port': '123.96.181.158:3128', 'user_pass': ''} ,
{'ip_port': '110.73.11.100:8123', 'user_pass': ''} ,
{'ip_port': '110.73.32.206:8123', 'user_pass': ''} ,
{'ip_port': '110.73.52.225:8123', 'user_pass': ''} ,
{'ip_port': '182.90.59.86:80', 'user_pass': ''} ,
{'ip_port': '121.42.153.46:808', 'user_pass': ''} ,
{'ip_port': '121.31.199.226:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.49:8123', 'user_pass': ''} ,
{'ip_port': '171.37.29.214:8090', 'user_pass': ''} ,
{'ip_port': '110.73.2.220:8123', 'user_pass': ''} ,
{'ip_port': '171.39.39.120:8123', 'user_pass': ''} ,
{'ip_port': '110.73.32.174:8123', 'user_pass': ''} ,
{'ip_port': '121.31.103.160:8123', 'user_pass': ''} ,
{'ip_port': '110.73.10.67:8123', 'user_pass': ''} ,
{'ip_port': '110.73.34.132:8123', 'user_pass': ''} ,
{'ip_port': '110.73.14.128:8123', 'user_pass': ''} ,
{'ip_port': '115.46.66.101:8123', 'user_pass': ''} ,
{'ip_port': '121.31.102.111:8123', 'user_pass': ''} ,
{'ip_port': '110.72.4.140:8123', 'user_pass': ''} ,
{'ip_port': '182.90.8.73:80', 'user_pass': ''} ,
{'ip_port': '110.72.37.159:8123', 'user_pass': ''} ,
{'ip_port': '182.61.13.122:6666', 'user_pass': ''} ,
{'ip_port': '121.31.194.236:8123', 'user_pass': ''} ,
{'ip_port': '171.38.181.213:8123', 'user_pass': ''} ,
{'ip_port': '110.73.9.240:8123', 'user_pass': ''} ,
{'ip_port': '115.159.101.27:8080', 'user_pass': ''} ,
{'ip_port': '119.53.128.172:8118', 'user_pass': ''} ,
{'ip_port': '182.90.50.170:8123', 'user_pass': ''} ,
{'ip_port': '171.38.200.242:8123', 'user_pass': ''} ,
{'ip_port': '117.81.52.83:808', 'user_pass': ''} ,
{'ip_port': '121.31.102.148:8123', 'user_pass': ''} ,
{'ip_port': '182.89.9.210:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.93:8123', 'user_pass': ''} ,
{'ip_port': '110.72.35.148:8123', 'user_pass': ''} ,
{'ip_port': '182.90.69.69:80', 'user_pass': ''} ,
{'ip_port': '182.90.83.25:8123', 'user_pass': ''} ,
{'ip_port': '182.88.230.12:8123', 'user_pass': ''} ,
{'ip_port': '110.73.50.110:8123', 'user_pass': ''} ,
{'ip_port': '110.73.54.67:8123', 'user_pass': ''} ,
{'ip_port': '121.31.103.242:8123', 'user_pass': ''} ,
{'ip_port': '121.31.153.224:8123', 'user_pass': ''} ,
{'ip_port': '115.46.65.75:8123', 'user_pass': ''} ,
{'ip_port': '171.36.252.225:8123', 'user_pass': ''} ,
{'ip_port': '110.72.26.109:8123', 'user_pass': ''} ,
{'ip_port': '110.73.2.231:8123', 'user_pass': ''} ,
{'ip_port': '182.61.26.186:80', 'user_pass': ''} ,
{'ip_port': '110.73.9.161:8123', 'user_pass': ''} ,
{'ip_port': '182.88.185.70:8123', 'user_pass': ''} ,
{'ip_port': '110.72.30.137:8123', 'user_pass': ''} ,
{'ip_port': '110.73.55.227:8123', 'user_pass': ''} ,
{'ip_port': '110.72.22.181:8123', 'user_pass': ''} ,
{'ip_port': '171.39.34.90:8118', 'user_pass': ''} ,
{'ip_port': '182.88.205.246:8123', 'user_pass': ''} ,
{'ip_port': '171.37.133.13:8123', 'user_pass': ''} ,
{'ip_port': '180.76.160.142:6666', 'user_pass': ''} ,
{'ip_port': '110.73.13.52:8123', 'user_pass': ''} ,
{'ip_port': '110.72.43.200:8123', 'user_pass': ''} ,
{'ip_port': '121.42.199.192:8888', 'user_pass': ''} ,
{'ip_port': '110.73.9.156:8123', 'user_pass': ''} ,
{'ip_port': '110.72.40.190:8123', 'user_pass': ''} ,
{'ip_port': '110.73.34.151:8123', 'user_pass': ''} ,
{'ip_port': '113.85.113.232:9999', 'user_pass': ''} ,
{'ip_port': '115.46.66.42:8123', 'user_pass': ''} ,
{'ip_port': '121.40.81.231:80', 'user_pass': ''} ,
{'ip_port': '182.88.212.141:8123', 'user_pass': ''} ,
{'ip_port': '110.72.16.103:8123', 'user_pass': ''} ,
{'ip_port': '110.72.46.163:8123', 'user_pass': ''} ,
{'ip_port': '119.29.107.85:443', 'user_pass': ''} ,
{'ip_port': '182.88.29.8:8123', 'user_pass': ''} ,
{'ip_port': '123.96.2.7:3128', 'user_pass': ''} ,
{'ip_port': '171.37.164.228:8123', 'user_pass': ''} ,
{'ip_port': '121.31.85.125:80', 'user_pass': ''} ,
{'ip_port': '110.72.24.244:8123', 'user_pass': ''} ,
{'ip_port': '182.88.228.79:8123', 'user_pass': ''} ,
{'ip_port': '222.132.28.8:8080', 'user_pass': ''} ,
{'ip_port': '182.90.66.14:80', 'user_pass': ''} ,
{'ip_port': '182.90.51.6:80', 'user_pass': ''} ,
{'ip_port': '182.92.85.42:80', 'user_pass': ''} ,
{'ip_port': '114.55.65.38:8080', 'user_pass': ''} ,
{'ip_port': '110.72.28.133:8123', 'user_pass': ''} ,
{'ip_port': '125.71.239.12:808', 'user_pass': ''} ,
{'ip_port': '111.161.65.85:81', 'user_pass': ''} ,
{'ip_port': '42.96.198.147:80', 'user_pass': ''} ,
{'ip_port': '110.72.28.69:8123', 'user_pass': ''} ,
{'ip_port': '182.90.2.175:8090', 'user_pass': ''} ,
{'ip_port': '110.72.16.118:8123', 'user_pass': ''} ,
{'ip_port': '121.31.146.254:8123', 'user_pass': ''} ,
{'ip_port': '123.206.196.184:80', 'user_pass': ''} ,
{'ip_port': '60.23.249.43:80', 'user_pass': ''} ,
{'ip_port': '182.90.8.231:80', 'user_pass': ''} ,
{'ip_port': '182.61.12.124:80', 'user_pass': ''} ,
{'ip_port': '182.88.231.168:8123', 'user_pass': ''} ,
{'ip_port': '121.5.19.20:808', 'user_pass': ''} ,
{'ip_port': '61.143.158.245:808', 'user_pass': ''} ,
{'ip_port': '218.76.253.131:8118', 'user_pass': ''} ,
{'ip_port': '58.253.186.61:8080', 'user_pass': ''} ,
{'ip_port': '182.88.191.145:8123', 'user_pass': ''} ,
{'ip_port': '121.31.49.44:8123', 'user_pass': ''} ,
{'ip_port': '42.227.126.89:808', 'user_pass': ''} ,
{'ip_port': '110.72.37.251:8123', 'user_pass': ''} ,
{'ip_port': '182.88.28.73:8123', 'user_pass': ''} ,
{'ip_port': '110.73.5.199:8123', 'user_pass': ''} ,
{'ip_port': '110.73.29.199:8123', 'user_pass': ''} ,
{'ip_port': '110.72.32.129:8123', 'user_pass': ''} ,
{'ip_port': '119.147.115.30:8088', 'user_pass': ''} ,
{'ip_port': '111.176.251.214:3128', 'user_pass': ''} ,
{'ip_port': '110.73.0.18:8123', 'user_pass': ''} ,
{'ip_port': '171.38.185.207:8123', 'user_pass': ''} ,
{'ip_port': '110.73.48.60:8123', 'user_pass': ''} ,
{'ip_port': '182.90.40.225:80', 'user_pass': ''} ,
{'ip_port': '110.73.30.163:8123', 'user_pass': ''} ,
{'ip_port': '110.72.25.204:8123', 'user_pass': ''} ,
{'ip_port': '182.90.13.142:80', 'user_pass': ''} ,
{'ip_port': '182.90.43.96:80', 'user_pass': ''} ,
{'ip_port': '121.31.100.28:8123', 'user_pass': ''} ,
{'ip_port': '110.73.2.49:8123', 'user_pass': ''} ,
{'ip_port': '182.88.229.41:8123', 'user_pass': ''} ,
{'ip_port': '110.73.12.195:8123', 'user_pass': ''} ,
{'ip_port': '182.90.17.233:80', 'user_pass': ''} ,
{'ip_port': '123.175.29.223:8888', 'user_pass': ''} ,
{'ip_port': '110.73.14.94:8123', 'user_pass': ''} ,
{'ip_port': '121.57.203.253:8888', 'user_pass': ''} ,
{'ip_port': '113.195.127.70:8888', 'user_pass': ''} ,
{'ip_port': '1.68.166.123:8888', 'user_pass': ''} ,
{'ip_port': '124.234.115.228:8888', 'user_pass': ''} ,
{'ip_port': '106.41.171.125:8888', 'user_pass': ''} ,
{'ip_port': '121.42.151.46:81', 'user_pass': ''} ,
{'ip_port': '123.185.109.86:8888', 'user_pass': ''} ,
{'ip_port': '182.61.19.148:80', 'user_pass': ''} ,
{'ip_port': '119.165.96.77:8888', 'user_pass': ''} ,
{'ip_port': '39.78.132.255:8888', 'user_pass': ''} ,
{'ip_port': '117.30.64.226:8888', 'user_pass': ''} ,
{'ip_port': '101.27.190.220:8888', 'user_pass': ''} ,
{'ip_port': '124.224.109.9:81', 'user_pass': ''} ,
{'ip_port': '123.166.4.119:8888', 'user_pass': ''} ,
{'ip_port': '125.78.7.215:81', 'user_pass': ''} ,
{'ip_port': '110.73.4.92:8123', 'user_pass': ''} ,
{'ip_port': '110.177.57.81:8888', 'user_pass': ''} ,
{'ip_port': '101.26.239.68:8888', 'user_pass': ''} ,
{'ip_port': '121.57.72.255:8888', 'user_pass': ''} ,
{'ip_port': '60.210.137.149:8888', 'user_pass': ''} ,
{'ip_port': '110.73.6.20:8123', 'user_pass': ''} ,
{'ip_port': '58.23.95.184:8888', 'user_pass': ''} ,
{'ip_port': '27.210.65.165:81', 'user_pass': ''} ,
{'ip_port': '140.246.19.86:8888', 'user_pass': ''} ,
{'ip_port': '121.25.115.148:8888', 'user_pass': ''} ,
{'ip_port': '60.9.239.38:8888', 'user_pass': ''} ,
{'ip_port': '171.38.241.12:8123', 'user_pass': ''} ,
{'ip_port': '123.244.184.241:8888', 'user_pass': ''} ,
{'ip_port': '210.44.128.140:80', 'user_pass': ''} ,
{'ip_port': '60.7.33.5:8888', 'user_pass': ''} ,
{'ip_port': '110.72.40.116:8123', 'user_pass': ''} ,
{'ip_port': '124.64.62.2:8118', 'user_pass': ''} ,
{'ip_port': '153.34.14.47:8888', 'user_pass': ''} ,
{'ip_port': '122.7.7.145:8888', 'user_pass': ''} ,
{'ip_port': '120.12.243.115:8888', 'user_pass': ''} ,
{'ip_port': '122.7.115.38:8888', 'user_pass': ''} ,
{'ip_port': '182.88.164.1:8123', 'user_pass': ''} ,
{'ip_port': '110.182.76.190:8888', 'user_pass': ''} ,
{'ip_port': '182.36.35.47:8888', 'user_pass': ''} ,
{'ip_port': '14.17.93.182:10000', 'user_pass': ''} ,
{'ip_port': '182.88.28.159:8123', 'user_pass': ''} ,
{'ip_port': '119.162.38.71:8888', 'user_pass': ''} ,
{'ip_port': '222.82.104.45:8888', 'user_pass': ''} ,
{'ip_port': '120.9.13.241:8888', 'user_pass': ''} ,
{'ip_port': '171.38.142.29:8123', 'user_pass': ''} ,
{'ip_port': '123.166.183.204:8888', 'user_pass': ''} ,
{'ip_port': '119.184.141.147:8888', 'user_pass': ''} ,
{'ip_port': '122.5.251.248:8888', 'user_pass': ''} ,
{'ip_port': '120.69.26.202:8888', 'user_pass': ''} ,
{'ip_port': '110.179.1.170:8888', 'user_pass': ''} ,
{'ip_port': '123.65.159.69:8888', 'user_pass': ''} ,
{'ip_port': '124.132.71.252:8888', 'user_pass': ''} ,
{'ip_port': '119.187.73.104:8888', 'user_pass': ''} ,
{'ip_port': '182.88.229.193:8123', 'user_pass': ''} ,
{'ip_port': '125.64.24.37:80', 'user_pass': ''} ,
{'ip_port': '123.165.28.222:8888', 'user_pass': ''} ,
{'ip_port': '182.90.67.251:80', 'user_pass': ''} ,
{'ip_port': '110.73.0.135:8123', 'user_pass': ''} ,
{'ip_port': '110.73.29.89:8123', 'user_pass': ''} ,
{'ip_port': '121.31.48.93:8123', 'user_pass': ''} ,
{'ip_port': '27.28.86.86:3128', 'user_pass': ''} ,
]
