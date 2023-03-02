import scrapy
from scrapy.http import HtmlResponse
from scrapynew.pars.items import ParserItem

class Spider1Spider(scrapy.Spider):
    name = "spider1"
    # allowed_domains = ["mail.yandex.ru"]
    # start_urls = ["http://mail.yandex.ru/"]
    allowed_domains = ["hh.ru"]
    # start_urls = ["http://mail.yandex.ru/"]
    start_urls = ["https://spb.hh.ru/search/vacancy?text=python&area=2"]

    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@class="serp-item__title"]/@href').extract()
        for link in links[0]:
            yield response.follow(link, callback=self.link_parse)
        next_page = response.xpath('//a[@class="bloko-button"]/@href').extract_first()
        # if next_page:
        #     yield response.follow('https://spb.hh.ru/'+next_page, callback=self.parse)

    def link_parse(selfself, response: HtmlResponse):
        name = response.css('h1::text').extract_first()
        # в css переход на более нижний уровень это пробел.
        salary = " ".join(response.xpath('//span[contains(@data-qa,"vacancy-salary-compensation")]/text()').extract())
        yield ParserItem(name=name, salary=salary)

