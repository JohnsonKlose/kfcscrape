# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import uuid
import logging

class KfcscrapePipeline(object):
    def process_item(self, item, spider):

        conn = psycopg2.connect(database='scarp', user='postgres', password='86732629jj', host='123.206.102.193',
                                port='5432')
        cur = conn.cursor()

        if spider.name == 'baidukfc':
            try:
                cur.execute(
                    """insert into "BAIDUKFC" (id, addr, address_norm, alias, aoi, area_name, dipointx, dipointy, tag, name, std_tag, tel, cater_tag, comment_num, overall_rating, price)
                    values(%(id)s, %(addr)s, %(address_norm)s, %(alias)s, %(aoi)s, %(area_name)s, %(dipointx)s, %(dipointy)s, %(tag)s, %(name)s, %(std_tag)s, %(tel)s, %(cater_tag)s, %(comment_num)s, %(overall_rating)s, %(price)s)""",
                    {
                        'id': str(uuid.uuid1()),
                        'addr': item['addr'],
                        'address_norm': item['address_norm'],
                        'alias': item['alias'],
                        'aoi': item['aoi'],
                        'area_name': item['area_name'],
                        'dipointx': item['diPointX'],
                        'dipointy': item['diPointY'],
                        'tag': item['tag'],
                        'name': item['name'],
                        'std_tag': item['std_tag'],
                        'tel': item['tel'],
                        'cater_tag': item['cater_tag'],
                        'comment_num': item['comment_num'],
                        'overall_rating': item['overall_rating'],
                        'price': item['price']
                    })
                conn.commit()
                logging.info("Data has added to database!")

            except Exception, e:
                print e

            finally:
                if cur:
                    cur.close()
            conn.close()

        elif spider.name == 'amapkfc':
            try:
                cur.execute(
                    """insert into "AMAPKFC" (id, rating, tel, cityname, address, adcode, name, latitude, longitude, tag, business_area, price, aoi)
                    values(%(id)s, %(rating)s, %(tel)s, %(cityname)s, %(address)s, %(adcode)s, %(name)s, %(latitude)s, %(longitude)s, %(tag)s, %(business_area)s, %(price)s, %(aoi)s)""",
                    {
                        'id': str(uuid.uuid1()),
                        'rating': item['rating'],
                        'tel': item['tel'],
                        'cityname': item['cityname'],
                        'address': item['address'],
                        'adcode': item['adcode'],
                        'name': item['name'],
                        'latitude': item['latitude'],
                        'longitude': item['longitude'],
                        'tag': item['tag'],
                        'business_area': item['business_area'],
                        'price': item['price'],
                        'aoi': item['aoi']
                    })
                conn.commit()
                logging.info("Data has added to database!")

            except Exception, e:
                print e

            finally:
                if cur:
                    cur.close()
            conn.close()

        return item
