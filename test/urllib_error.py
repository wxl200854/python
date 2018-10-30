from urllib import request, error
try:
	reponse = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
	print(e.reason)