#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce
def prod(L):
	def  multi(x, y):
		return x * y

	return reduce(multi,L)

print(prod([3, 5, 7, 9]))	