import requests
def downloads_pic(**kw):
    pic_name = kw.get('pic_name', None)
    pic_path = r'E:\study\python\python\pic'
    url = ''
    res = requests.get(url, stream=True)
    with open(pic_path + pic_name + '.bmp', 'wb') as f:
        for chunk in res.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()