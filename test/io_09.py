#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
d = dict(name='Bob', age=20, score=88)
path = r'E:\study\python\python\test\dump.txt'
with open(path, 'w') as f:
	json.dump(d, f)

with open(path, 'r') as f:
	l = json.load(f)
	print(l)