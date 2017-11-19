# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
import re

from kfcscrape.items import amapkfcItem


class amapkfc(scrapy.Spider):
    name = 'amapkfc'
    allowed_domains = ['amap.com']

    def start_requests(self):
        for i in range(1, 15):
            url = "http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=" + str(i) + \
                  "&need_utd=true&utd_sceneid=1000&city=320100&geoobj=118.694927%7C32.024763%7C119.009067%7C32.117861&keywords=南京肯德基"
            yield scrapy.Request(url)

    def parse(self, response):
        body = json.loads(response.body)
        poi_list = body['data']['poi_list']
        for object in poi_list:
            item = amapkfcItem()

            item['rating'] = object['rating'] if 'rating' in object else ""
            item['tel'] = object['tel'] if 'tel' in object else ""
            item['cityname'] = object['cityname'] if 'cityname' in object else ""
            item['address'] = object['address'] if 'address' in object else ""
            item['adcode'] = object['adcode'] if 'adcode' in object else ""
            item['name'] = object['name'] if 'name' in object else ""
            item['latitude'] = object['latitude'] if 'latitude' in object else ""
            item['longitude'] = object['longitude'] if 'longitude' in object else ""
            if 'domain_list' in object:
                item['tag'], item['business_area'], item['price'], item['aoi'] = "", "", "", ""

                for domain in object['domain_list']:
                    # pattern = re.compile('>([\w|\s]+)<')
                    if domain['name'] == 'tag' and 'value' in domain:
                        # item['tag'] = domain['value'].xpath('font/text()').extract()
                        taghtml = etree.HTML(domain['value'])
                        item['tag'] = taghtml.xpath('//font/text()')
                        # tagtext = ""
                        # for n in tagnode:
                        #     tagtext = tagtext + "," + n.text
                        # item['tag'] = tagtext
                        # item['tag'] = taghtml.xpath('//font/text()')
                        # item['tag'] = re.findall(pattern, domain['value'])
                        # item['tag'] = domain['value']
                    elif domain['name'] == 'business_area' and 'value' in domain:
                        item['business_area'] = domain['value']
                    elif domain['name'] == 'price' and 'value' in domain:
                        # item['price'] = domain['value'].xpath('font/last()/text()').extract()
                        pricehtml = etree.HTML(domain['value'])
                        item['price'] = pricehtml.xpath('//font[3]/text()')[0]
                        # item['price'] = re.findall(pattern, domain['value'])
                        # item['price'] = domain['value']
                    elif domain['name'] == 'aoi' and 'value' in domain:
                        item['aoi'] = domain['value']
                    else:
                        continue
            else:
                item['tag'], item['business_area'], item['price'], item['aoi'] = "", "", "", ""

            yield item

