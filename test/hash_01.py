#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

md5 = hashlib.md5()
md5.update('你好'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('你好'.encode('utf-8'))
print(sha1.hexdigest())