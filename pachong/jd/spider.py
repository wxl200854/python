from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

#options = webdriver.ChromeOptions()
#options.add_argument('lang=zh_CN.UTF-8')
#options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
#options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"')
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search(url):
    browser.get(url)
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#key"))
    )
    submit= wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button"))
    )
    input.send_keys('美食')
    submit.click()

def main():
    search(URL)

if __name__ == "__main__":
    main()