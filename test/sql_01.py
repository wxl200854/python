#/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user21(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user21(id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()