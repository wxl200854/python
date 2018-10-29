import http.cookiejar, urllib.request

filename = "cookie1.txt"
#cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
