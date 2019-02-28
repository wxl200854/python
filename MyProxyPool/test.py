import requests
from bs4 import BeautifulSoup 
from urllib import request,error
import threading
import random

def get_ip(url, path):
    for page in range(1,11):
        urls = url + str(page)
        key = [
        'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
        'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
        ]
        headers={'User-Agent': keys[random.randint(0, len(keys)-1)]}
        response = requests.get(urls, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.find('table', id="ip_list").find_all('tr')
        for item in trs[1:]:
                tds = item.find_all('td')
                if tds[0].find('img') is None:
                        nation = '未知'
                        locate = '未知'
                else:
                        nation = tds[0].find('img')['alt'].strip()
                        locate = tds[3].text.strip()
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                anony = tds[4].text.strip()
                protocal = tds[5].text.strip()
                speed = tds[6].find('div')['title'].strip()
                time = tds[8].text.strip()
                with open(path, 'a') as f:
                        f.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocal, speed, time))

def identifyProxy(ip):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
        url = 'https://www.baidu.com'
        proxy = {'http': 'ip'}
        proxy_handler = request.ProxyHandler(proxy)
        proxy_opener = request.build_opener(proxy_handler)
        request.install_opener(proxy_opener)
        try:
                req = request.Request(url, headers=headers)
                rsq = request.urlopen(req, timeout=5.0)
                code = rsq.getcode()
                return code
        except error.URLError as e:
                return e

def identifyProxyList(path_proxy, path_identified):
        with open(path_proxy, 'r') as f:
                all = f.readlines().strip()
        for line in range(all):
                ll = line.split('|')
                ip = ll[1]
                port = ll[2]
                realip = ip + ':' + port
                code = identifyProxy(realip)
                if code == 200:
                        print('----Success:' + ip + ":" + port)
                        with open(path_identified, 'a') as f:
                                f.write(line + "\n")
                else:
                                print("--Failure:" + ip + ":" +port)
        

if __name__ == "__main__":
        path_proxy = r'E:\study\python\pythontest\python\MyProxyPool\proxyFile.txt'
        path_identified = r'E:\study\python\pythontest\python\MyProxyPool\identifiedProxy.txt'
        urls = ['https://www.xicidaili.com/nn/', 'https://www.xicidaili.com/nt/', 'https://www.xicidaili.com/wn/', 'https://www.xicidaili.com/wt/']
        for url in urls:
                get_ip(url, path_proxy)
        identifyProxyList(path_proxy, path_identified)