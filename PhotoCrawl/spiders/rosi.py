# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class ImageItem(scrapy.Item):
    '''
    Define here the models for your scraped items.
    define the fields for your item here like:
    name = scrapy.Field()
    See documentation in:
    http://doc.scrapy.org/en/latest/topics/items.html
    '''
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    images = scrapy.Field()

class PhotoSpider(scrapy.Spider):
    name = "PhotoSpider"
    allowed_domains = ['nanrencd.com']
    start_urls = ['http://www.nanrencd.com/',

                  ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                    errback=self.errback,
                                    dont_filter=True)


    def parse(self, response):
        yield self.parse_item(response)  # ok
        for a in response.css('a::attr(href)').extract():
            if not a:
                continue
            next_page = response.urljoin(a)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        il = ItemLoader(item=ImageItem(), response=response)
        il.add_css('image_urls', 'img::attr(src)')
        return il.load_item()

    def errback(self, failure):
        pass
