#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools

def log(txt):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s:' % (txt, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-3-25')

def main():
	now()
	print(now.__name__)

main()