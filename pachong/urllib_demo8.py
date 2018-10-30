import http.cookiejar, urllib.request

filename = r'E:\study\python\pythontest\python\pachong\cookies0.txt'
#cookie =http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
hanler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hanler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)