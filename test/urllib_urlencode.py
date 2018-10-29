import urllib.parse

parm = {
	'name': 'john',
	'age': 24
}
base_url = 'http://www.baidu.com?'
data = base_url + urllib.parse.urlencode(parm)
print(data)