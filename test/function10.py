#!/usr/bin/env python
# -*- coding:utf-8 -*-
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b)
		yield(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

def main():
	print(fib(6))

main()