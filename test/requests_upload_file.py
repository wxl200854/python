import requests

files = {'wenjian': open('tmp.jpg', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)