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

            # if not object['addr'] is None:
            #     item['addr'] = object['addr']
            # else:
            #     object['addr'] = None
            item['addr'] = object['addr'] if 'addr' in object else ""

            # if not object['address_norm'] is None:
            #     item['address_norm'] = object['address_norm']
            # else:
            #     object['address_norm'] = None
            item['address_norm'] = object['address_norm'] if 'address_norm' in object else ""

            # if not object['alias'] is None:
            #     item['alias'] = object['alias']
            # else:
            #     object['alias'] = None
            item['alias'] = object['alias'] if 'alias' in object else ""

            # if not object['aoi'] is None:
            #     item['aoi'] = object['aoi']
            # else:
            #     object['aoi'] = None
            item['aoi'] = object['aoi'] if 'aoi' in object else ""

            # if not object['area_name'] is None:
            #     item['area_name'] = object['area_name']
            # else:
            #     object['area_name'] = None
            item['area_name'] = object['area_name'] if 'area_name' in object else ""

            # if not object['diPointX'] is None:
            #     item['diPointX'] = object['diPointX']
            # else:
            #     object['diPointX'] = None
            item['diPointX'] = object['diPointX'] if 'diPointX' in object else ""

            # if not object['diPointY'] is None:
            #     item['diPointY'] = object['diPointY']
            # else:
            #     object['diPointY'] = None
            item['diPointY'] = object['diPointY'] if 'diPointY' in object else ""

            # if not object['tag'] is None:
            #     item['tag'] = object['tag']
            # else:
            #     object['tag'] = None
            item['tag'] = object['tag'] if 'tag' in object else ""

            # if not object['name'] is None:
            #     item['name'] = object['name']
            # else:
            #     object['name'] = None
            item['name'] = object['name'] if 'name' in object else ""

            # if not object['std_tag'] is None:
            #     item['std_tag'] = object['std_tag']
            # else:
            #     object['std_tag'] = None
            item['std_tag'] = object['std_tag'] if 'std_tag' in object else ""

            # if not object['tel'] is None:
            #     item['tel'] = object['tel']
            # else:
            #     object['tel'] = None
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