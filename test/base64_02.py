#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
def safe_base64_decode(s):
	while len(s)%4:
		s = s + b'='
	return base64.b64decode(s)