from urllib import request, error
try:
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason, '\n', e.code, '\n', e.headers)