#!/usr/bin/env python
# -*- coding:utf-8 -*-
with open(r'E:\study\python\python\test\123.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip())
