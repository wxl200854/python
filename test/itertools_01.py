#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itertools

'''na = itertools.count(1)
for i in na:
	print(i)
	if i> 10:
		break

n = 0 
cs = itertools.cycle('ABC')
for c in cs:
	print(c)
	n = n + 1
	if(n>=20):
		break
ns = itertools.repeat('A', 3)
for i in ns:
	print(i)

na = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, na)
print(list(ns))'''
n = 0
for c in itertools.chain('abc', 'jjj'):
	print(c)
	