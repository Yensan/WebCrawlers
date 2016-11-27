# -*- coding: utf-8 -*-

# scrapy.cfg:
# project：是项目目录，内含settings和spiders。
# default：指明settings.py路径，project.settings

# settings.py：
# BOT_NAME:就是项目目录。spiders_modules：spider模块所在的目录。
# ITEM_PIPELINES:  指明一个Pipe类的路径


from scrapy import cmdline
cmdline.execute("scrapy crawl rosi".split())