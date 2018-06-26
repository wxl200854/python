#!/usr/bin/env python
# -*- coding:utf-8 -*-
path = r'C:\Windows\system.ini'
with open(path, 'r') as f:
	print(f.read())
