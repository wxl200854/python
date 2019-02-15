from fake_useragent import UserAgent
import requests
import random

ua = UserAgent()
url = 'http://www.hao123.com'
headers = {"User-Agent": ua.random}
response = requests.get(url=url, headers=headers)
#print(ua.data_randomize)
#print(response.text)
#print(response.status_code)
#print(response.headers)
print(dict(headers))