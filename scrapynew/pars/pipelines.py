# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ParsPipeline:

    def __init__(self):
        print("DDDDDDDDDD")
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.spider1

    def process_item(self, item, spider):
        # обработка полей
        print(1)
        collection = self.mongo_base[spider.name]
        collection.insert_one(ItemAdapter(item).asdict())
        return item

class TestPipeline:

    def __init__(self):
        print("DDDDDDDDDD")
        # client = MongoClient('localhost', 27017)
        # self.mongo_base = client.spider1

    def process_item(self, item, spider):
        # обработка полей
        print(1)
        # collection = self.mongo_base[spider.name]
        # collection.insert_one(ItemAdapter(item).asdict())
        return item