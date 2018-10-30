import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
file = r'E:\study\python\pythontest\python\pachong\cookies0.txt'
cookie.load(file, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))