from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from selenium.common.exceptions import TimeoutException   
from selenium.common.exceptions import StaleElementReferenceException
import re 
from pyquery import PyQuery as pq
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def save(result):
    if db[MONGO_TABLE].insert(result):
            

def search():
    try:
        browser.get(URL)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#key"))
        )
        submit= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button"))
        )
        input.send_keys('美食')
        submit.click()
        page_num = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b'))
        )
        get_detail()
        return page_num.text
    except TimeoutException:
        return search()

def next_page(num):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input"))
        )
        submit= wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a"))
        )
        input.clear()
        input.send_keys(num)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(num))
        )
        get_detail()
    except TimeoutException:
        return next_page(num)
    except StaleElementReferenceException:
        return next_page(num)

def get_detail():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#J_goodsList .gl-warp .gl-item"))
    )
    html = browser.page_source
    result = pq(html)
    items = result("#J_goodsList .gl-warp .gl-item").items()
    for item in items:
        product = {
            'pic': item.find('.p-img a img').attr('data-lazy-img'),
            'price': item.find('.p-price').text(),
            'title': item.find('.p-name').text(),
            'deal': item.find('.p-commit').text(),
            'shop': item.find('.p-shop').text()
        }
        print(product)


def main():
    result = search()
    total = int(re.compile('(\d+)').search(result).group(1))
    for i in range(2, total + 1):
        next_page(i)

if __name__ == "__main__":
    main()