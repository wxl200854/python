#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hmac

messages = b'Hello, world!'
key = b'secret'
h = hmac.new(key, messages, digestmod='MD5')
print(h.hexdigest())