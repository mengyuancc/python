#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-16 02:18:24
# Project: douban

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250?start='
        self.page_num = 0
        self.total_num = 250

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            print(url)
            self.crawl(url, callback=self.index_page)
            self.page_num += 25

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.hd').items():
            print(each('a').attr.href)
            self.crawl(each('a').attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            'sort': response.doc('.rating_num').text(),
        }