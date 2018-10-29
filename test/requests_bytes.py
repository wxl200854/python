import requests

response = requests.get('https://github.com/favicon.ico')
print(type(response.text), type(response.content))
print(response.text)
print(response.content)
with open(r'E:\study\python\python\test\tmp.jpg', 'wb') as f:
	f.write(response.content)