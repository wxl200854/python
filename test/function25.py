#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import functools

def log(txt):
	if(isinstance(txt, str)):
		def decorator(fn):
			@functools.wraps(fn)
			def wrapper(*args, **kw):
				print('begin ---- %s %s' % (txt, fn.__name__))
				a = fn(*args, **kw)
				print('end ---- %s %s' % (txt, fn.__name__))
				return a
			return wrapper
		return decorator
	else:
		@functools.wraps(txt)
		def decorator(*args, **kw):
			print('begin %s' % txt.__name__)
			a = txt(*args, **kw)
			print('end %s' % txt.__name__)
			return a
		return decorator

@log
def f():
	pass

@log('hello')
def m():
	pass

f()
m()