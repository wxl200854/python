import urllib.request 
reponse = urllib.request.urlopen('https://www.python.org')
#print(reponse.read().decode('utf-8'))
print(type(reponse))
print(reponse.getheaders())
print(reponse.getheader('Server'))