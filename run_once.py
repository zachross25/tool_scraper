# coding: utf-8
from grab import Grab
import requests
from techno_angel_ru.functions import products
from scrapy.http import HtmlResponse

g = Grab()
start_urls = [
    "https://techno-angel.ru/product/minimoika_vysokogo_davleniya_stihl_re_88/"
]

r = requests.get(start_urls[0])
response = HtmlResponse(url=start_urls[0], encoding='utf-8', body=r.text)
products_items = products(response, url=start_urls[0])
for item in products_items.load_item().items():
    print(item)


