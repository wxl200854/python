import requests
from pyquery import PyQuery as pq 
from bs4 import BeautifulSoup 

res = requests.get('http://www.btbtdy.tv/downlist/14817-0-0.html')
soup = BeautifulSoup(res.text, 'lxml')
with open('456.txt', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())