#!/usr/share/python3.1

query_ht={}
query_ht['listgenre']="\
cursor.execute('select rowid, genre\
from genres;')"
