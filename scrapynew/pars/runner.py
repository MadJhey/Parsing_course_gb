# from Tools.scripts.fixnotice import process
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapynew.pars import settings

from spiders.spider1 import Spider1Spider

if __name__ == "__main__":
    spider1_settings = Settings()
    spider1_settings.setmodule(get_project_settings())
    process = CrawlerProcess(settings=spider1_settings)
    process.crawl(Spider1Spider)
    process.start()






