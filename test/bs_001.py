import requests
from bs4 import BeautifulSoup

#content = requests.get('http://www.btbtdy.net/').text
content = requests.get('http://www.btbtdy.net/btdy/dy13825.html').text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
print(soup.title.string)
#print(content)
#http://www.btbtdy.net/btdy/dy13825.html