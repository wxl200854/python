import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(response.read().decode('utf-8'))