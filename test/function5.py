#!/usr/bin/env python
# -*- coding:utf-8 -*-
def product(*numbers):
	sum = 1
	for number in numbers:
		sum = sum * number
	return sum

def main():
	sum = product(1, 2, 34)
	print("the product of the numbers is {}".format(sum))

main()




