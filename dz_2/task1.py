import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import re
import json

def removeNonAscii(s):
    if s == None:
        return None
    return "".join(i for i in s if ord(i)<128)
def getSalary(text):
    # text = removeNonAscii(text)
    # text = ''.join(text.split())
    min, max, cur = None, None, None
    if text == None:
        return min, max, cur

    ls = text.split(sep = " ")
    # '15 000 – 39 000 руб.'
    if not ls[-1].isnumeric():
        cur = ls[-1]
        text = ' '.join(ls[:-1])
    if '–' in text:
        min = text.split(sep=" ")[0]
        max = text.split(sep=" ")[2]
    else:
        # str1 = '(? <= от) \w +'  # lookbehind doesnt support in python 3.9
        # str2 = '(? <= до) \w +'
        # min = re.search(str1, text)
        # max = re.search(str2, text)
        if 'от' in text:
            min = text.split(sep=" ")[1]
        if 'до' in text:
            max = text.split(sep=" ")[1]

    return removeNonAscii(min), removeNonAscii(max), cur
def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/92.0.4515.159 Safari/537.36'}
    host = 'https://spb.hh.ru/search/vacancy'
    vacancy = 'Python'
    page = 0
    params = {'text': vacancy, 'from': 'suggest_post', 'area': '3', 'page': page,
              'hhtmFrom': 'vacancy_search_list', 'clusters': 'true', 'enable_snippets': 'true',
              }
    # url = f'https://spb.hh.ru/search/vacancy?area=3&clusters=true&enable_snippets=true&ored_clusters=true&
    # text=Python&search_period=7&page=0&hhtmFrom=vacancy_search_list'
    jobs = []
    while True:
        params['page'] = page
        response = requests.get(host, headers=headers, params=params)
        page += 1
        if response.ok:
            sp = bs(response.text, 'lxml')
            blocks = sp.find_all('div', {'class': 'serp-item'})
            if len(blocks) == 0:
                break
            for block in blocks:
                job_data = {}
                job_data['name'] = block.find('a').getText()
                job_data['link'] = block.find('a').get('href')
                try:
                    job_data['min'], job_data['max'], job_data['cur'] = \
                        getSalary(block.find('span',{'data-qa': 'vacancy-serp__vacancy-compensation'}).text)
                except AttributeError:
                    job_data['min'], job_data['max'], job_data['cur'] = None, None, None
                jobs.append(job_data)
        else:
            pprint(response.status_code)

        jobs.append(job_data)


    pprint(jobs)
    with open(r"response.txt", "w") as file:
        json.dump(jobs, file)
    file.close()

if __name__ == "__main__":
    main()
