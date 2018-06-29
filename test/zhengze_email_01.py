#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def name_of_email(addr):
	str = r'^<?([\w\s]+)>?\s*\w*@[a-zA-Z]+?\.[a-z]{3}'
	m = re.match(str, addr)
	if m:
		return m.group(1)
	return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')