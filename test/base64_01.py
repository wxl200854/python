#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
m = base64.b64encode(b'binary\x00string')
n = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
nn = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(m, "\t", n, "\t", nn)
print(base64.b64decode(m), "\t", base64.urlsafe_b64decode(nn))