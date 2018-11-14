import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
url1 = 'http://maoyan.com/board/4'
response = requests.get(url1, headers=header)
#response = requests.get(url1)
print(response.text)