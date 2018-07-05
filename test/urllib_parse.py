#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import parse

url = "https://docs.python.org/3.5/library/urllib.parse.html?highlight=parse#module-urllib.parse"
result = parse.urlparse(url)
m = result.query
print(m)
print(parse.parse_qs(m))
print(parse.parse_qsl(m))