import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
import re 
from bs4 import BeautifulSoup

def get_page_index(offset, keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery',
        'pd': ''
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错', url)
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    image_pattern = re.compile('gallery: JSON.parse((.*?),', re.S)
    result = re.search(image_pattern, html)
    if result:
        print(result.group(1))

def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            parse_page_detail(html)

if __name__ == "__main__":
    main()