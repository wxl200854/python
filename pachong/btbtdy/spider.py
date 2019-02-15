import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re 
import json

def get_index(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
             return response
        return None
    except RequestException:
        return None
    

def parse_index(response):
    soup = BeautifulSoup(response.text, 'lxml')
    html = soup.select('.new-ul')
    print(html)


def main():
    url = 'http://www.btbtdy.net/hot/'
    response = get_index(url)
    parse_index(response)
    


if __name__ == "__main__":
    main()
