#/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user21 where id=?', ('1',))
value = cursor.fetchall()
print(value)
cursor.close()
conn.close()