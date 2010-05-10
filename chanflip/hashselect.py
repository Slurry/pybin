#!/usr/bin/python3.1
import sqlite3
conn = sqlite3.connect('/home/jayson/streams/streamtest.db')
cursor = conn.cursor()

query_ht = {}
query_ht['listgenre']="cursor.execute('select rowid, genre from genres;')"

res=eval(query_ht['listgenre'])
for l in res:
    print(l[0], l[1])

