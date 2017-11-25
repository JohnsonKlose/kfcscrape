# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class baidukfcItem(scrapy.Item):
    id = scrapy.Field()
    addr = scrapy.Field()
    address_norm = scrapy.Field()
    alias = scrapy.Field()
    aoi = scrapy.Field()
    area_name = scrapy.Field()
    diPointX = scrapy.Field()
    diPointY = scrapy.Field()
    tag = scrapy.Field()
    name = scrapy.Field()
    std_tag = scrapy.Field()
    tel = scrapy.Field()
    cater_tag = scrapy.Field()
    comment_num = scrapy.Field()
    overall_rating = scrapy.Field()
    price = scrapy.Field()

    pass

class amapkfcItem(scrapy.Item):
    id = scrapy.Field()
    rating = scrapy.Field()
    tel = scrapy.Field()
    cityname = scrapy.Field()
    address = scrapy.Field()
    adcode = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    tag = scrapy.Field()
    business_area = scrapy.Field()
    price = scrapy.Field()
    aoi = scrapy.Field()

    pass