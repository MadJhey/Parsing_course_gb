from pprint import pprint
import requests
from lxml import html
import re
from pymongo import MongoClient

def load_data():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get('https://lenta.ru/', headers=header)
    dom = html.fromstring(response.text)
    # список главных новостей

    items = dom.xpath('//a[contains(@class,"_compact")]')
    # название источника,
    # наименование новости,
    # ссылку на новость,
    # дата публикации

    news = []
    for item in items:
        new = {}
        new['name'] = 'lenta.ru'
        new['title'] = item.xpath('.//span[contains(@class,"card-mini__title")]//text()')
        link = item.xpath('.//@href')[0]
        if 'http' not in link:
            link = 'https://lenta.ru/'+link
        new['link'] = link
        match = re.search(r'\d{4}/\d\d/\d\d', link)
        new['data'] = match[0] if match else 'Not found'
        news.append(new)

    pprint(news)
    return news
def main():

    data = load_data()
    client = MongoClient('127.0.0.1', 27017)
    db = client['news']
    news_data = db.news
    news_data.insert_many(data)

if __name__ == "__main__":
    main()



