#!/usr/bin/env python
# -*-coding:utf-8 -*-
class Student(object):
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
	def set_gender(self, sex):
		if sex == 'male':
			self.__gender = sex
		elif sex == 'female':
			self.__gender = sex
		else:
			print("type error")
	def get_gender(self):
		return self.__gender