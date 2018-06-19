#!/usr/bin/env python
# -*- coding:utf-8 -*-
is_odd = lambda n: n % 2 ==1
L = list(filter(is_odd,range(1,20)))

print (L)