import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    patten = re.compile('table.*?nbg.*?title="(.*?)">.*?src="(.*?)".*?pl">(.*?)</p>.*?rating_nums">(.*?)</span>.*?pl">((.*?))</span>', re.S)
    items = re.findall(patten, html)
    for item in items:
        yield{
            'title': item[0],
            'image': item[1],
            'actors': item[2],
            'score': item[3],
            'num': item[4]
        }

def main():
    url = 'https://movie.douban.com/chart'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)

if __name__ == '__main__':
    main()