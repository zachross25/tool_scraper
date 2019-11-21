# -*- coding: utf-8 -*-

from scrapy.loader.processors import TakeFirst, MapCompose, Join
import scrapy
import re


def filter_spaces(value):
    return value.strip()


def _add_site_prefix(value):
    return "https://techno-angel.ru" + value


def take_from_1(value):
    return ','.join(value[1:])


def take_sku(value):
    return value[0].split(':')[1].strip()


def replace_image_part(value):
    return _add_site_prefix(re.sub(r'pre|sm', 'source', value))


def only_digits(value):
    return re.sub(r'\D', '', value)


class TechnoAngelRuItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(filter_spaces), output_processor=TakeFirst())
    breadcrumbs = scrapy.Field(output_processor=take_from_1)
    sku = scrapy.Field(input_processor=MapCompose(filter_spaces), output_processor=take_sku)
    images = scrapy.Field(input_processor=MapCompose(filter_spaces), output_processor=MapCompose(replace_image_part))
    price = scrapy.Field(input_processor=MapCompose(only_digits), output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    brand = scrapy.Field(output_processor=TakeFirst())
    properties = scrapy.Field()
    video_id = scrapy.Field(output_procesor=TakeFirst())
    rating = scrapy.Field(output_processor=TakeFirst())
    availability = scrapy.Field(output_processor=TakeFirst())
    advantages = scrapy.Field(input_processor=MapCompose(filter_spaces), output_processor=Join())
    files = scrapy.Field(output_processor=MapCompose(_add_site_prefix))

