from urllib.parse import urlencode

base_url = 'https://weixin.sogou.com/weixin?'

def get_detail(url):
    

def get_index(keyword, page):
    data ={
        'query': keyword,
        'type': 2,
        'page': page,
        'ie': 'utf-8'
        'sug_type_': '', 
        's_from': 'input',
        '_sug_': 'n'
    }
    queries = urlencode(data)
    url = base_url + queries