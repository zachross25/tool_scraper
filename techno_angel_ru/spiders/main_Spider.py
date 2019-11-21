# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MainSpiderSpider(CrawlSpider):
    name = 'main_Spider'
    allowed_domains = ['techno-angel.ru']
    start_urls = ['http://techno-angel.ru/']

    rules = (
        Rule(LinkExtractor(allow=r'catalog'), follow=True),
        Rule(LinkExtractor(allow=r'product/.*?/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        from techno_angel_ru.functions import products
        return products(response, url=response.url).load_item()
