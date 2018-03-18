# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SsSpiderItem(scrapy.Item):
    US_IP = scrapy.Field()
    US_Port = scrapy.Field()
    US_PW = scrapy.Field()
    JP_IP = scrapy.Field()
    JP_Port = scrapy.Field()
    JP_PW = scrapy.Field()
    SG_IP = scrapy.Field()
    SG_Port = scrapy.Field()
    SG_PW = scrapy.Field()
    pass
