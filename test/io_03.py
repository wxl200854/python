#!/usr/bin/env python
# -*- coding:utf-8 -*-
with open(r'E:\study\python\python\test\test.txt', 'w', encoding='gbk') as f:
	f.write('Hello')
with open(r'E:\study\python\python\test\test.txt', 'r') as f:
	print(f.read())