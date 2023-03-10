from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from book24 import settings
from book24.spiders.book24 import Book24Spider

if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(Book24Spider, query='Сент-Экзюпери')

    process.start()