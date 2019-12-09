# -*- coding: utf-8 -*-

# Scrapy settings for ziroomuniversal project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ziroomuniversal'

SPIDER_MODULES = ['ziroomuniversal.spiders']
NEWSPIDER_MODULE = 'ziroomuniversal.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ziroomuniversal (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ziroomuniversal.middlewares.ZiroomuniversalSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ziroomuniversal.middlewares.ZiroomuniversalDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'ziroomuniversal.pipelines.ImagePipeline': 300,
    'ziroomuniversal.pipelines.GetPricesPipeline': 301,
    'ziroomuniversal.pipelines.MySQLPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'sxy199311'
MYSQL_DATEBASE = 'ziroom'
MYSQL_PORT = 3306
MYSQL_TABLE ='Hangzhou'
IMAGES_STORE = 'Hangzhou'
DIGIT_PX_LIST = ['-0', '-31.24', '-62.48', '-93.72', '-124.96', '-156.2', '-187.44', '-218.68', '-249.92', '-281.16']
IMG_NUMBER_MAP = {
'19003aac664523e53cc502b54a50d2b6.png': '4928730651',
'1b68fa980af5e85b0f545fccfe2f8af1.png': '8916702453',
'234a22e00c646d0a2c20eccde1bbb779.png': '1205837649',
'477571844175c1058ece4cee45f5c4b3.png': '2158097436',
'486ff52ed774dbecf6f24855851e3704.png': '4780169253',
'4eb5ebda7cc7c3214aebde816b10d204.png': '9570863124',
'5c6750e29a7aae17288dcadadb5e33b1.png': '4593162870',
'6f8787069ac0a69b36c8cf13aacb016b.png': '6197450832',
'73ac03bb4d5857539790bde4d9301946.png': '7190864523',
'7995074a73302d345088229b960929e9.png': '0742138659',
'7ce54f64c5c0a425872683e3d1df36f4.png': '5137689402',
'8e7a6d05db4a1eb58ff3c26619f40041.png': '3871290645',
'939205287b8e01882b89273e789a77c5.png': '8015739624',
'93959ce492a74b6617ba8d4e5e195a1d.png': '5430879621',
'a68621a4bca79938c464d8d728644642.png': '7034615982',
'a822d494f1e8421a2fb2ec5e6450a650.png': '3165849720',
'b2451cc91e265db2a572ae750e8c15bd.png': '9162853470',
'bdf89da0338b19fbf594c599b177721c.png': '3164795280',
'de345d4e39fa7325898a8fd858addbb8.png': '7263840195',
'eb0d3275f3c698d1ac304af838d8bbf0.png': '3650489217'
}
