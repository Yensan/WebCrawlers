# -*- coding: utf-8 -*-

# scrapy.cfg:
# project：是项目目录，内含settings和spiders。
# default：指明settings.py路径，project.settings

# settings.py：
# BOT_NAME:就是项目目录。spiders_modules：spider模块所在的目录。
# ITEM_PIPELINES:  指明一个Pipe类的路径


###########  Pycharm，运行配置说明: ##########
###### 用main.py驱动运行
#from scrapy import cmdline
#cmdline.execute("scrapy crawl PhotoSpider".split())
## PhotoSpider是class的属性，name="PhotoSpider"，然后直接运行main.py
###### 在Pycharm直接运行rosi（spider）
## //TODO

###########  更改目标网站，配置说明: ##########
###### 存储路径配置
## settings.py，更改IMAGES_STORE = '../../data/rosi/'，改成'../../data/XXX/'
###### 网址配置
## rosi.py ，更改目标网站
    # allowed_domains = ['rosiok.com']
    # start_urls = ['http://www.rosiok.com/',

from scrapy import cmdline
cmdline.execute("scrapy crawl PhotoSpider".split())