#!/usr/bin/python3.1

import sqlite3

conn = sqlite3.connect('/home/jayson/data/people.db')
cursor = conn.cursor()


count = 0
while count < 6:
    res = cursor.execute("select first_name, last_name, pri_phone from people;")
    for row in res:
        first = row[0].capitalize()
        last = row[1].capitalize()
        phone_work = row[2]
        phone = phone_work[3:6] + '-' + phone_work[6:]
        
        print("{0:10}{1:15}{2:10}\t{0:10}{1:15}{2:10}\t"\
                  .format(first, last, phone))

    count += 1
    print()

