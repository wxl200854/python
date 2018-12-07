#-*- coding:utf-8 -*-
import os,time
import re
 
#检查sqlpwd.py的进程，并关闭进程
def kill():
    lines = os.popen('ps -e|grep sqlpwd.py').readlines()
    pa = re.compile(r'(\d+) ')
    for line in lines:
        result = re.findall(pa,line)
        print(result[0])
        os.popen('kill -9 '+str(result[0]))
 
def check():
    with open('log.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            if 'FinishAll' in line:
                return True
        return False
'''
如果已经进行爬取了，则直接从上次扫描的地方开始
设置每半个小时重新扫描，解决之前扫描过程中进程掉的问题
'''
def runpwd():
    if os.path.exists('log.txt') == False:
        os.system('python sqlpwd.py 0 &')
        time.sleep(18000)
        kill()
 
    while True:
        print('-------------启动进程-------------------')
        os.system('python sqlpwd.py 1 &')
        time.sleep(60)
        print('-------------结束进程-------------------')
        kill()
        if check() == True:
            print('所有信息采集完成')
            break
        else:
            pass
 
if __name__ == '__main__':
    runpwd()
