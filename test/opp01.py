#!/usr/bin/env python
# -*-coding:utf-8 -*-
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(lisa.get_name())
print(lisa.get_score())
