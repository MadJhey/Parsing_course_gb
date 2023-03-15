import scrapy
from scrapy.http import HtmlResponse
from book24.items import Book24parserItem
from scrapy.loader import ItemLoader

class InstaSpider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
