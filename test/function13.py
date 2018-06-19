#/usr/bin/env python
# -*- coding:utf-8 -*-
def normalize(name):
	str1 = ''
	for i, ch in enumerate(name):
		if i == 0:
			str1 = str1 + ch.upper()
		else:
			str1 = str1 + ch.lower()
	return str1

def main():
	L1 = ['adam', 'LISA', 'barT']
	L2 = list(map(normalize, L1))

	print(L2)

main()
