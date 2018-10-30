import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
hanler = urllib.request.HTTPCookieProcessor(cookie)
opener =urllib.request.build_opener(hanler)
reponse = opener.open('http://www.baidu.com')
for item in cookie:
	print(item.name+"="+item.value)