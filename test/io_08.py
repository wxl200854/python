#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
d = dict(name='Bob', age=20, score=88)
path = r'E:\study\python\python\test\dump.txt'
with open(path, 'wb') as f:
	pickle.dump(d, f)

with open(path, 'rb') as f:
	l = pickle.load(f)
	print(l)