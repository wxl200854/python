#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import namedtuple, deque
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point), isinstance(p, tuple))

print("-------------")

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
for i in q:
	print(i)