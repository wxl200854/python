import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
import re 
from bs4 import BeautifulSoup
import codecs
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
    
def get_page_index(offset, keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
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
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        #'referer':'https://www.toutiao.com/a6602192672943768067/'
        'referer': url
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错', url)
        return None

def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    image_pattern = re.compile('gallery: JSON\.parse\("(.*?)"\),', re.S)
    result = re.search(image_pattern, html)
    if result:
        data_str = codecs.getdecoder('unicode_escape')(result.group(1))[0]
        json_data = json.loads(data_str)
        if json_data and 'sub_images' in json_data.keys():
            sub_images = json_data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            #data = json.loads(codecs.getdecoder('unicode_escape')(result.group(1)))        
            #if data and 'sub_images' in data.keys():
            # sub_images = data.get('sub_images')
            #images = [item.get('url') for item in sub_images]
            return {
                'title': title,
                'url': url,
                'images': images
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print("存储到mongodb成功", result)
        return True
    return False            

def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            save_to_mongo(result)

if __name__ == "__main__":
    main()