#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image

im = Image.open('cat.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')