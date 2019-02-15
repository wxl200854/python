#coding = utf-8
#不同进制转文字

import chardet
a = b"\303\246\302\220\302\234\303\247\302\213\302\220\303\245\302\271\302\277\303\245\302\221\302\212"
#a = b"\345\260\274\345\217\244\346\213\211\346\226\257\350\265\265\345\233\233"
#a = b"\xc3\xa6\xc2\x90\xc2\x9c\xc3\xa7\xc2\x8b\xc2\x90\xc3\xa5\xc2\xb9\xc2\xbf\xc3\xa5\xc2\x91\xc2\x8a"
#a = b"\320\302\316\305\270\345"
fencoding = chardet.detect(a)
print(fencoding)
a = a.decode(fencoding['encoding'])
print(a) 