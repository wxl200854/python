#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess

print('$ nslookup www.python.com')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)