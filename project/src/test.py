from fake_useragent import UserAgent
import requests
from pyquery import PyQuery as pq

headers = {
        'User-Agent': UserAgent().random,
        'Cookie': 'PHPSESSID=4lj9a88236t7s44bas23str817; qrxs_auth=ee12%2FDwoP5R4P2Dcm1hjjrCeOoPYU%2FpRLbhmzFrnzL9M8XzUvmlMyZV%2Bxj6I9yBIk0ziKuDAg5eIgEmM1E9jWPynug; Hm_lvt_9ed2be7ae49dbc8829f60b2d671b5654=1553007861,1553009454; SERVERID=f4ac482318e2356f12270179e2238604|1553009764|1553007858; Hm_lpvt_9ed2be7ae49dbc8829f60b2d671b5654=1553009765'
}

def get_book_list():
        # url_booklist = 'https://www.qirexiaoshuo.com/book/41915/list'
        url_booklist = 'https://www.qirexiaoshuo.com/book/13023/list/'
        res = requests.get(url_booklist, headers = headers)
        doc = pq(res.text)
        items = doc('.main.all_chapter.mar_top .item ul li').items()
        for item in items:
                name = item.find('a span').text()
                url_chapter = item.find('a').attr('href')
                print(name, url_chapter)

def get_charpter_detail():
        res = requests.get('https://www.qirexiaoshuo.com/book/11927/911378/', headers = headers)
        # print(res.text)
        # with open('123.txt', 'w', encoding='utf-8') as f:
        #         f.write(res.text)
        doc = pq(res.text)
        items = doc('#content_box').items()
        for item in items:
                charpter = item.find('.title h1').text()
                content = item.remove('.title').find('p').text()
                print(charpter)
                print(content)

if __name__ == "__main__":
    get_charpter_detail()