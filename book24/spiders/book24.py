import scrapy
from scrapy.http import HtmlResponse
from book24.items import Book24parserItem
from scrapy.loader import ItemLoader


# https://book24.ru/search/?q=Сент-Экзюпери


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']

    def __init__(self, query):
        super(Book24Spider, self).__init__()
        self.start_urls = [f'https://book24.ru/search/?q={query}']

    def parse(self, response: HtmlResponse):
        head = 'https://book24.ru'
        books_links = response.xpath("//div[@class='product-list__item']"
                                     "//a[@class='product-card__image-link smartLink']/@href").extract()
        i = 0
        for link in books_links:
            i += 1
            if i == 3:
                break

            # response.xpath("//a[@class='pagination__item _link _button _next smartLink']")
            yield response.follow(head + link, callback=self.parse_book)

    def parse_book(self, response: HtmlResponse):
        # //div[contains(@class,'swiper-slide main-poster__slide')]//source[contains(@srcset,'jpg')]/@srcset
        loader = ItemLoader(item=Book24parserItem(), response=response)
        loader.add_xpath('photos', "//img[contains(@class, 'product-poster__main-image')]/@data-src")
        loader.add_value('url', response.url)
        loader.add_xpath('name', "//h1[@class = 'product-detail-page__title']/text()")
        yield loader.load_item()
        # photos = response.xpath("//img[contains(@class, 'product-poster__main-image')]/@data-src").extract()
        # name = response.xpath("//h1[@class = 'product-detail-page__title']/text()").extract_first()
        # url = response.url
        # yield Book24parserItem(name=name, url = url, photos=photos)
