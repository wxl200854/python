#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil

print(psutil.net_io_counters())
#print(psutil.net_if_addrs())
#print(psutil.net_if_stats())
with open('tt.txt', 'w') as f:
	f.write(str(psutil.net_connections()))

#print(psutil.pids())
p = psutil.Process(860)
print(p.name())
#print(p.exe())
#print(p.cwd())
print(p.cpu_times())
print(p.create_time())
#print(p.terminal())
#print(p.username())
print(p.status())
print(p.memory_info())
#print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
#print(p.environ())
#print(p.terminate())
print(psutil.test())