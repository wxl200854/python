import requests
import re
from requests_toolbelt import SSLAdapter


def open_url(url):
    adapter = SSLAdapter('TLSv1')
    session = requests.Session()
    session.mount('https://', adapter)
    req = requests.get(url)
    return req.text


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    for each in imglist:
        print(each)


if __name__ == '__main__':
    url = "https://www.387uu.com/htm/pic1/298137.htm"
    get_img(open_url(url))
