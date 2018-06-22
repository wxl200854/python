#/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Sun.value)
print(Weekday.Sun.name)