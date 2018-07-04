#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib, random

db = {}
def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')

def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
	user = db[username]
	return user.password == get_md5(password + user.salt)