# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://www.douban.com/']
    start_urls = ['http://https://www.douban.com//']

    def parse(self, response):
        pass
