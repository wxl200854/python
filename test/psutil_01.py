#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

'''for x in range(10):
	print(psutil.cpu_percent(interval=1, percpu=True))
'''
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())