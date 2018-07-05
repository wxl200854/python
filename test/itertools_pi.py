#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itertools

def pi(N):
	n = itertools.count(1, lambda x: x % 2 > 0)
	l = itertools.takewhile(lambda x: x <= 2N-1, n)
#failed