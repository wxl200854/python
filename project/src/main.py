from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pyquery import PyQuery as pq

browser = webdriver.Chrome()

def get_all_url():
        try:
                browser.get(URL)
                input = True
                while(input):
                        input = browser.find_element_by_class_name("next")
                        get_page_detail()
                        input.click()
                        time.sleep(1)
        finally:
                browser.close()

def get_page_detail():
        html = browser.page_source
        doc = pq(html)
        items = doc('.selected .entry .item').items()
        for item in items:
                name = item.find('.warp .t').text()
                intro = item.find('.warp .p').text()
                all = item.find('.warp .intro').text().replace('\n', '').split('|')
                author = all[0] 
                style = all[1]
                status = all[2]       
                img = item.find('.avatar a img').attr("src")
                url = item.find('.avatar a').attr('href')
                get_book_list(url)
                # print(name, author, style, status, intro, url, img)

def get_book_list(url):
        headers = {
                'User-Agent': UserAgent().random,
                'Cookie': 'PHPSESSID=4lj9a88236t7s44bas23str817; qrxs_auth=ee12%2FDwoP5R4P2Dcm1hjjrCeOoPYU%2FpRLbhmzFrnzL9M8XzUvmlMyZV%2Bxj6I9yBIk0ziKuDAg5eIgEmM1E9jWPynug; Hm_lvt_9ed2be7ae49dbc8829f60b2d671b5654=1553007861,1553009454; SERVERID=f4ac482318e2356f12270179e2238604|1553009764|1553007858; Hm_lpvt_9ed2be7ae49dbc8829f60b2d671b5654=1553009765'
        }
        url_booklist = URL_BASE + url + "list"
        res = requests.get(url_booklist, headers = headers)
        doc = pq(res.text)
        items = doc('.main.all_chapter.mar_top .item .ul .li').items()
        for item in items:
                name = item.find('a span').text()
                url_chapter = item.find('a').attr('href')
                print(name, url_chapter)







if __name__ == "__main__":
    get_all_url()

