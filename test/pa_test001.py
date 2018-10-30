import requests, re

response = requests.get('http://www.btbtdy.net')
with open('tmp.txt', 'w', encoding='utf-8') as f:
	f.write(response.text)