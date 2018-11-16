import requests

url = 'http://maoyan.com/board/4'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
response = requests.get(url, headers=header)
print(response.text)