#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time, functools

def metric(fn):
	@functools.wraps(fn)
	def decorator(*args, **kw):
		print('%s executed in %s ms' % (fn.__name__, time.time()))
		return fn(*args, **kw) 
	return decorator

@metric
def now():
	print('hello')

now()

