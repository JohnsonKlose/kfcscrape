# -*- coding: utf-8 -*-
import scrapy
import json

from kfcscrape.items import baidukfcItem


class baidukfc(scrapy.Spider):
    name = "baidukfc"
    allowed_domains = ['baidu.com']

    def start_requests(self):
        for i in range(1, 15):
            url = "http://map.baidu.com/?newmap=1&reqflag=pcmap&qt=con&from=webmap&c=315&wd=%E5%8D%97%E4%BA%AC%E8%82%AF%E5%BE%B7%E5%9F%BA&pn=" + \
                  str(i) + "&on_gel=1&ie=utf-8&b=(13163180.95967742,3726294.55;13290796.95967742,3762646.55)"
            yield scrapy.Request(url)

    def parse(self, response):
        body = json.loads(response.body)
        content = body['content']
        for object in content:
            item = baidukfcItem()

            item['addr'] = object['addr'] if 'addr' in object else ""

            item['address_norm'] = object['address_norm'] if 'address_norm' in object else ""

            item['alias'] = object['alias'] if 'alias' in object else ""

            item['aoi'] = object['aoi'] if 'aoi' in object else ""

            item['area_name'] = object['area_name'] if 'area_name' in object else ""

            item['diPointX'] = object['diPointX'] if 'diPointX' in object else ""

            item['diPointY'] = object['diPointY'] if 'diPointY' in object else ""

            item['tag'] = object['tag'] if 'tag' in object else ""

            item['name'] = object['name'] if 'name' in object else ""

            item['std_tag'] = object['std_tag'] if 'std_tag' in object else ""

            item['tel'] = object['tel'] if 'tel' in object else ""

            if 'ext' in object:
                if 'detail_info' in object['ext']:
                    detail_info = object['ext']['detail_info']

                    item['cater_tag'] = detail_info['cater_tag'] if 'cater_tag' in detail_info else ""

                    item['comment_num'] = detail_info['comment_num'] if 'comment_num' in detail_info else ""

                    item['overall_rating'] = detail_info['overall_rating'] if 'overall_rating' in detail_info else ""

                    item['price'] = detail_info['price'] if 'price' in detail_info else ""
                else:
                    setextempty(item)
            else:
                setextempty(item)

            yield item

def setextempty(item):
    item['cater_tag'] = ""
    item['comment_num'] = ""
    item['overall_rating'] = ""
    item['price'] = ""