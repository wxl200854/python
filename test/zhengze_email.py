#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def is_valid_email(addr):
	str = r'^[0-9a-zA-Z]+?[0-9a-zA-Z\.]+?@[0-9a-zA-Z]+?\.com'
	m = re.match(str, addr)
	return m
