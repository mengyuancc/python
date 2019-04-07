# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口的url 扔到调度器中
    start_urls = ['https://movie.douban.com/top250']

    # 默认的解析方法
    def parse(self, response):
        #print (response.text)
        # 获取列表
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        # 循环电影条目
        for movie in movie_list:
            # iterm文件导入
            douban_iterm = DoubanItem()
            # 数据处理
            douban_iterm['serial_number'] = movie.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_iterm['movie_name'] = movie.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = movie.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract_first()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_iterm['introduce'] = content_s
            douban_iterm['star'] = movie.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_iterm['evaluate'] = movie.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_iterm['describe'] = movie.xpath(".//p[@class='quote']//span/text()").extract_first()
            print(douban_iterm)
            # 将数据放入itermpipline
            yield douban_iterm
        # 解析下一页规则，取后面的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250'+next_link, callback=self.parse)


