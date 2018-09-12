from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(10)
pageSource = driver.page_source
print(pageSource)
#driver.close()