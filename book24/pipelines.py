# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient

import scrapy


class Book24ParserPipeline:

    # def __init__(self):
    #     client = MongoClient('localhost', 27017)
    #     self.mongo_base = client.spider1

    def process_item(self, item, spider):
        # collection = self.mongo_base[spider.name]
        # collection.insert_one(ItemAdapter(item).asdict())
        return item


class Book24PhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(url=img, method='GET')
                except Exception as e:
                    print(e)

    # def file_path(self, request, response=None, info=None):
    #      return
    #
    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]  # перезаписываем photos на полученные результаты
        return item
