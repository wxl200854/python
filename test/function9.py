#!/usr/bin/env python
# -*- coding:utf-8 -*-
L1 = ['Hello', 'world', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)