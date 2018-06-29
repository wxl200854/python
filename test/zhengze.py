#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
test = "用户输入的字符串"
if re.match(r'正则表达式', test):
	print('ok')
else:
	print('failed')