#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s:' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2015-3-25')

def main():
	now()
	print(now.__name__)

main()