# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


def cleaner_photo(value):
    if value[:2] == '//':
        return f'http:{value}'
    return value


class Book24parserItem(scrapy.Item):
    # можно использовать препроцессор и постпроцессор
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(cleaner_photo))  #
    # input_processor=MapCompose(cleaner_photo))
    _id = scrapy.Field()
    url = scrapy.Field()
