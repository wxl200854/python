from pyquery import PyQuery as pq
import requests

#response = requests.get('http://book.douban.com')
doc = pq(url='https://book.douban.com/')
a = doc('ul')
print(a.img.attr.title)