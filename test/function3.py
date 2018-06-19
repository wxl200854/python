#!/usr/bin/env python
# -*- coding:utf-8 -*-
def person(name, age, *, city, job):
	print(name, age, city, job)

#print(person('Michael', 30))
#print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, 'kk', city='Beijing', job='Engineer'))