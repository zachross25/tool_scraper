# coding: utf-8
# module with scraping functions
from scrapy.loader import ItemLoader
from techno_angel_ru.items import TechnoAngelRuItem


def products(response, url=None):
    item = ItemLoader(item=TechnoAngelRuItem(), response=response)
    item.add_xpath('name', '//h1[@itemprop="name"]/text()')
    item.add_xpath('breadcrumbs', '//div[@class="breadcrumbs"]//span[@itemprop="name"]/text()')
    item.add_xpath('sku', '//div[@class="product-head__title-code"]/text()')
    item.add_xpath('images', '//div[@class="product-gallery__thumb-slider-link"]/img/@src')
    item.add_xpath('price', '//span[@class="product__buy-price-val product__buy-price-val_new"]/text()')
    item.add_xpath('description', '//div[@itemprop="description"]/p/text()')
    item.add_xpath('brand', '//div[@itemprop="brand"]/span/text()')
    item.add_xpath('rating', '//input[@class="rating_val val"]/@value')
    item.add_xpath('advantages', '//div[contains(@class, "product-advantages")]//text()')
    item.add_xpath('video_id', '//a[contains(@onclick, "playVideo")]/@onclick', re="'(.*?)'")
    item.add_xpath('files', '//a[@class="product-file-tbl__link"]/@href')
    item.add_xpath('availability', '//div[contains(@class, "available")]/@class', re=r'available_(\w+)$')

    properties_source = response.xpath('//div[@class="product-properties__item-inner"]')
    properties = {}
    for prop in properties_source:
        name = prop.xpath('./div[@itemprop="name"]/text()').get()
        value = prop.xpath('./div[@itemprop="value"]/text()').get()
        properties[name] = value
    item.add_value('properties', properties)

    return item

