#-*- coding:utf-8 -*-
import requests
import re
import random
from bs4 import BeautifulSoup
from multiprocessing import Process,Pool,Lock
import multiprocessing
import time
import sys
import logging
reload(sys)
sys.setdefaultencoding('utf-8')
 
def get_pwd(j,start,end):
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
 
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
 
    logger.addHandler(handler)
    logger.addHandler(console)
    user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    ]
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': user_agent[random.randint(0,5)]
    }
    #print(start,end)
    logger.info('进程'+str(j)+'任务从第'+str(start)+'页采集到'+str(end)+'页')
 
 
    for i in range(start,end):
        url = 'https://www.mysql-password.com/database/'+str(i)
        #print(url)
        logger.info(url)
        try:
            r = requests.get(url,headers=headers)
            r.encoding = 'utf8'
            html = r.text
            soup = BeautifulSoup(html,'lxml')
        except Exception as e:
            print('进程'+str(j)+'异常：原因如下')
            print(e)
            #log.write('进程'+str(j)+'异常：原因如下'+str(e)+'\n')
            logger.info('进程'+str(j)+'异常：原因如下'+str(e))
            time.sleep(10)
            continue
        filename = 'password'+str(j)+'.txt'
        try:
            for tag in soup.find('tbody').find_all('tr'):
                ss = str(tag.find_all('td')[2].string)
                #print(ss)
                with open(filename,'a') as f:
                    f.write(ss+'\n')
        except Exception as e:
            print('进程'+str(j)+'异常：原因如下')
            print(e)
            #log.write('进程'+str(j)+'异常：原因如下'+str(e)+'\n')
            logger.info('进程'+str(j)+'异常：原因如下'+str(e))
            time.sleep(10)
            continue
        #print('进程'+str(j)+'采集完成第'+str(i)+'页')
        logger.info('进程'+str(j)+'采集完成第'+str(i)+'页')
    
def check():
    num = []
    mul = []
    with open('log.txt','r') as f:
        lines = f.readlines()
        pa = re.compile(r'https://www.mysql-password.com/database/(\d+)')
        for line in lines:
            result = re.findall(pa,line)
            if len(result) != 0 :
                #print(result)
                num.append(int(result[0]))
    m = 10
    start = 20000
    cha = int(((180000-start)/m))
    for j in range(0,m):
        numList = []
        info = []
        end = 20000 + cha * (j+1)
        for n in num:
            if n > start and n < end:
                numList.append(n)
        print (str(j)+','+str(numList[-1])+','+str(end)+',')
        if numList[-1] + 1 == end:
            start = end + 1
            continue
        else:
            info.append(j)
            info.append(numList[-1])
            info.append(end)
            mul.append(info)
            start = end + 1
    return mul
 
def run(type):
    if type == 0:
        m = 10
        pool = multiprocessing.Pool(m)
        #start是开始爬行的页数，  下面写得是20000   180000 意思是从20000页爬到180000页，根据实际情况修改
        start = 20000
        cha = int(((180000-start)/m))
        for j in range(0,m):
            end = 20000 + cha * (j+1)
            pool.apply_async(get_pwd,args=(j,start,end,))
            #print(start,end)
            start = end + 1
        pool.close()
        pool.join()
    else:
        mul = check()
        #print(mul)
        if len(mul) == 0:
            print('所有进程都爬取完成')
            logger.info('FinishAll')
        else:
            pool = multiprocessing.Pool(len(mul))
            for mu in mul:
                pool.apply_async(get_pwd,args=(mu[0],mu[1],mu[2],))
        pool.close()
        pool.join()
 
 
if __name__ == '__main__':
    runtype = int(sys.argv[1])
    run(runtype)
