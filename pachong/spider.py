import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode

def get_page_index(offset, keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引失败")
        return None

def parse_page_index(html):
    

def main():
    html = get_page_index(0, "街拍")
    print(html)

if __name__ == "__main__":
    main()