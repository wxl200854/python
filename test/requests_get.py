import requests

data = {
	'name': 'john',
	'age': 22
}
response = requests.get('http://httpbin.org/get', params=data)
print(type(response.text))
print(response.json())
print(type(response.json()))