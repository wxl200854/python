#import urllib.parse
import urllib.request
import socket
import urllib.error

try:
	reponse = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
	if isinstance(e.reason, socket.timeout):
		print('TIME OUT')

#data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
#reponse = urllib.request.urlopen('http://httpbin.org/post', data=data)
#reponse = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
#print(reponse.read())