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
            get_page_url()

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
        print(author, style, status)


     



if __name__ == "__main__":
    get_all_url()



