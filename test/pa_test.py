import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.btbtdy.net/play/*.html')
with open(r'E:\study\python\python\test\pa_test.html', 'w+') as f:
    f.write(str(r.data))
