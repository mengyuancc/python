# -*- coding: utf-8 -*-

# 定义数据结构
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    serial_number = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 星级
    start = scrapy.Field()
    # 电影的介绍
    introduce = scrapy.Field()
    # 评论数
    evaluate = scrapy.Field()
    # 描述
    describe = scrapy.Field()

    pass
