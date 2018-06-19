#!/usr/bin/env python
# -*- coding:utf-8 -*-
def createCounter():
	def next_num():
		n = 0
		while True:
			n = n + 1
			yield n
	it = next_num()
	def counter():
		return next(it)
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())