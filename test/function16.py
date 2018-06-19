#!/usr/bin/env python
# -*- coding:utf-8 -*-
def is_palindrome(x):
	return str(x) == str(x)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(	list(output))
