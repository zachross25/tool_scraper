# -*- coding: utf-8 -*-

BOT_NAME = 'techno_angel_ru'
SPIDER_MODULES = ['techno_angel_ru.spiders']
NEWSPIDER_MODULE = 'techno_angel_ru.spiders'
ROBOTSTXT_OBEY = False
#CLOSESPIDER_PAGECOUNT = 100
#ITEM_PIPELINES = {
#    'techno_angel_ru.pipelines.TechnoAngelRuPipeline': 300,
#}

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
