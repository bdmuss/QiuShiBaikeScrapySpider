# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsauto.items import QsautoItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        ua={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('http://www.qiushibaike.com/',headers=ua)

    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
        # 指定回调函数为parse_item，follow为True，就是说链接还要跟进
        # 就是说爬了页面后还要不断地从爬出来的页面中接着爬下去
    )
    # 这里跟普通爬虫不一样，提取链接提取的规律（方便自动翻页等操作时链接的变动自动变化）

    def parse_item(self, response):
        i = QsautoItem()
        i["content"]=response.xpath("//div[@class='content']/text()").extract()
        i["link"]=response.xpath("//link[@rel='canonical']/@href").extract()
        print(i["content"])
        print(i["link"])
        print("")
        return i
