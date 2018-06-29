#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

str = r'^(\d{3})-(\d{3,8}$)'
m = re.match(str, '010-123456')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))