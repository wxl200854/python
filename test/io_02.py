#!/usr/bin/env python
# -*- coding:utf-8 -*-
with open(r'E:\study\python\python\test\baidu.png', 'rb') as f:
	for line in f.readlines():
		print(line.strip())
