#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
print(os.path.abspath('.'))
m = os.path.abspath('.')
p = os.path.join(m, 'nihao')
os.rmdir(p)
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])