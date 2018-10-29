import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345')
response = s.get('http://httpbin.org/cookies')
print(response.text)