#/usr/bin/env python
# -*- coding:utf-8 -*-
def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

nums = [1, 2, 3]
print(calc(*nums))