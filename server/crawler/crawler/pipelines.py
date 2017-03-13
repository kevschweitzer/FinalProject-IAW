# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]
        #self.collection = db[settings['MONGODB_COLLECTION']]




    def process_item(self, item, spider):
        valid = True
        if type(item).__name__.lower() == "infobaeportadaitem" or type(item).__name__.lower() == "telamportadaitem":
            self.collection = self.db["portadas"]
        if type(item).__name__.lower() == "infobaenoticiaitem" or type(item).__name__.lower() == "telamnoticiaitem":
            self.collection = self.db["noticias"]

        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Noticia agregada a la MongoDB! :)",
                    level=log.DEBUG, spider=spider)
        return item
