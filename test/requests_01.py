#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
with open('requests_test.txt', 'w', encoding='utf-8') as f:
	f.write(r.text)
print(r.cookies['ll'])

r2 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r2.url)
print(r2.encoding)
#print(r2.content)
r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
with open('requests_test.json', 'w', encoding='utf-8') as f:
	f.write(str(r3.json()))

r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
with open('requests_r4.txt', 'w', encoding='utf-8') as f:
	f.write(r4.text)

r5 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
with open('requests_r5.txt', 'w', encoding='utf-8') as f:
	f.write(r5.text)
