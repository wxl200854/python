import requests
from bs4 import BeautifulSoup 

def get_ip(url):
    for page in range(1,11):
        urls = url + str(page)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        response = requests.get(urls, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.find('table', id="ip_list").find_all('tr')
        print(trs)


if __name__ == "__main__":
    get_ip('https://www.xicidaili.com/nt/')