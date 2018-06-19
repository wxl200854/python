#!/usr/bin/env python
# -*- coding:utf-8 -*-
def findMinAndMax(L):
	if L != []:
		(min, max) = (L[0], L[0])
		for i in L:
			if max < i:
				max = i
			if min > i:
				min = i
		return (min, max)
	else:
		return (None, None)

def main():
	L = "djsakdkas"
	print(findMinAndMax(L))

main()