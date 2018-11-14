from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input1 = browser.find_element_by_id('zu-top-add-question')
input2 = browser.find_element_by_class_name('zu-top-link-logo')
input3 = browser.find_element_by_id('q')
input3.send_keys("局座")
button = browser.find_element_by_class_name('zu-top-search-button')
button.click()
print(input2.text)
print(input1.text)