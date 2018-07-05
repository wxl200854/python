#!/usr/bin/env python
# -*- coding:utf-8 -*-
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
	f = open(path, mode)
	yield f
	f.close()

with my_open(r'E:\study\python\python\test\abc.txt', 'w') as f:
	f.write('Hello')